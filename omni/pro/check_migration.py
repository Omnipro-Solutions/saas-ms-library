import ast
import inspect as inspect_ast
from datetime import datetime
from pathlib import Path
from typing import Tuple, List

from alembic import command
from alembic.config import Config as AlembicConfig
from alembic.script import Script, ScriptDirectory
from omni.pro.config import Config
from omni.pro.logger import configure_logger
from omni.pro.redis import RedisManager
from sqlalchemy import Column, String, create_engine
from sqlalchemy import inspect as inspect_sqlalchemy
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy_utils import database_exists, create_database

logger = configure_logger(name=__name__)


class Base(DeclarativeBase):
    pass


class AlembicVersionModel(Base):
    __tablename__ = "alembic_version"

    version_num = Column(String(32), primary_key=True)


class AlembicMigrateCheck(object):
    def __init__(self, path: Path, postgres_url: str = None) -> None:
        self.redis_manager = RedisManager(
            host=Config.REDIS_HOST, port=Config.REDIS_PORT, db=Config.REDIS_DB, redis_ssl=Config.REDIS_SSL
        )
        self.tenants = self.redis_manager.get_tenant_codes()
        self.alembic_config = AlembicConfig(path / "alembic.ini")
        self.alembic_config.set_main_option("script_location", str(path / "alembic"))
        self.versions_path = path / "alembic" / "versions"
        self.postgres_url = postgres_url
        self.changes = False

    def main(self):
        logger.info("Starting validation process")
        last_version = None
        validations = []
        for idx, tenant in enumerate(self.tenants):
            logger.info(f"Migrating tenant: {tenant}")
            try:
                host, port, user, password, name = self.get_postgres_config(Config.SERVICE_ID, tenant)
                if not all([host, port, user, password, name]):
                    raise ValueError(f"Invalid database config for tenant: {tenant}")
                sql_connect = f"postgresql://{user}:{password}@{host}:{port}/{name}"
                self.postgres_url = sql_connect
                if idx == 0:
                    last_version = self.apply()
                else:
                    self.upgrade_head(last_version)
            except Exception as e:
                logger.error(f"Failed to migrate tenant {tenant}: {e}")

        if self.changes:
            repo_url = self.redis_manager.get_json(f'SETTINGS', f'repos.{Config.SERVICE_ID}.url')
            logger.info(f"Repository URL: {repo_url}")
            logger.info("RUN=1")
            print(f"REPO_URL={repo_url}")
            print(f"RUN=1")

    @property
    def postgres_url(self) -> str:
        return self._postgres_url

    @postgres_url.setter
    def postgres_url(self, postgres_url) -> None:
        self._postgres_url = postgres_url
        if postgres_url:
            self.ensure_database_exists()
            self.alembic_config.set_main_option("sqlalchemy.url", postgres_url)
            self.engine = create_engine(postgres_url)
            self.Session = sessionmaker(bind=self.engine)

    def get_postgres_config(self, service_id, tenant_code):
        postres_config = self.redis_manager.get_postgres_config(Config.SERVICE_ID, tenant_code)
        host, port, user, password, name = postres_config.values()
        if all([host, port, user, password, name]):
            return host, port, user, password, name
        logger.error(f"Postgres config not found for tenant: {tenant_code}")

    def check(self) -> bool:
        # Comprobar si la tabla alembic_version existe
        inspector = inspect_sqlalchemy(self.engine)
        if not inspector.has_table(AlembicVersionModel.__tablename__):
            AlembicVersionModel.metadata.create_all(self.engine)
            return False
        return True

    def get_current_version(self) -> str:
        with self.Session() as session:
            latest_version = session.query(AlembicVersionModel).order_by(AlembicVersionModel.version_num.desc()).first()
            return latest_version.version_num if latest_version else None

    def apply_revision(self, message="auto-generated revision") -> tuple[bool, Script | None | list[Script | None]] | \
                                                                   tuple[bool, Exception]:
        # Formato del mensaje con fecha y hora en formato ISO
        message = f"{message} {datetime.now().isoformat()}"
        try:
            # Intenta crear la revisión de Alembic
            new_revision = command.revision(self.alembic_config, autogenerate=True, message=message)
            return True, new_revision
        except Exception as e:
            # Registra el error específico si no se puede encontrar la tabla referenciada
            print(f"Failed to create revision due to a missing referenced table: {e}")
            return False, e

    def no_changes_detected(self, script: Script) -> bool:
        code = inspect_ast.getsource(script.module.upgrade)
        tree = ast.parse(code)
        clean_code = ast.unparse(tree)

        lines = clean_code.split("\n")
        l = [line for line in lines if line.strip() not in ["", "def upgrade():", "def upgrade() -> None:", "pass"]]
        return not l

    def upgrade_head(self, revision=None) -> None:
        # Usa la librería alembic para hacer las migraciones
        command.upgrade(self.alembic_config, revision or "head")

    def is_database_up_to_date(self):
        # Esta función verifica si la base de datos está actualizada
        script_directory = ScriptDirectory.from_config(self.alembic_config)
        head_revision = script_directory.get_current_head()
        current_version = self.get_current_version()

        return current_version == head_revision

    def apply(self):
        try:
            self.check()  # Asegúrate de que la base de datos esté preparada para migraciones
            current_version = self.get_current_version()

            if not self.is_database_up_to_date():
                logger.info("Database is not up to date. Upgrading to head.")
                self.upgrade_head("head")  # Actualiza la base de datos si no está al día

            script_directory = ScriptDirectory.from_config(self.alembic_config)
            if current_version is None and list(script_directory.walk_revisions()):
                self.upgrade_head()
                current_version = self.get_current_version()
            status, script = self.apply_revision()
            if not status:
                logger.exception(f"Error creating revision: \n{script}")
                return
            if self.no_changes_detected(script):
                self.last_version = current_version
                Path(script.path).unlink()  # Elimina la revisión si no hay cambios
            else:
                self.last_version = script.revision
                self.changes = True
                self.upgrade_head(self.last_version)  # Aplica la nueva migración
            return self.last_version
        except Exception as e:
            logger.error(f"Error apply revision: {e}")

    def ensure_database_exists(self):
        db_name = self.postgres_url.split('/')[-1]
        temp_url = self.postgres_url.replace(f'/{db_name}', '/postgres')  # Usa 'postgres' o cualquier DB predeterminada

        engine = create_engine(temp_url)
        conn = engine.connect()

        if not database_exists(self.postgres_url):
            logger.info(f"Database {db_name} does not exist. Creating...")
            create_database(self.postgres_url)
            logger.info(f"Database {db_name} successfully created.")
        else:
            logger.info(f"Database {db_name} already exists.")
        conn.close()
