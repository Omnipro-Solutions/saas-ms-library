import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

from omni.pro.check_migration import AlembicMigrateCheck


class TestAlembicMigrateCheck(unittest.TestCase):

    def setUp(self):
        self.path = Path("/fake/path")
        self.handler = AlembicMigrateCheck(self.path)
        self.handler.redis_manager = MagicMock()
        self.handler.engine = MagicMock()

    @patch("omni.pro.check_migration.AlembicMigrateCheck.ensure_database_exists")
    @patch("omni.pro.check_migration.AlembicMigrateCheck.check")
    @patch("omni.pro.check_migration.AlembicMigrateCheck.get_current_version")
    @patch("omni.pro.check_migration.AlembicMigrateCheck.is_database_up_to_date", return_value=False)
    @patch(
        "omni.pro.check_migration.AlembicMigrateCheck.apply_revision",
        return_value=(True, MagicMock(revision="rev_123")),
    )
    @patch("omni.pro.check_migration.AlembicMigrateCheck.no_changes_detected", return_value=False)
    @patch("omni.pro.check_migration.AlembicMigrateCheck.upgrade_head")
    def test_apply_success(
        self,
        mock_upgrade_head,
        mock_no_changes,
        mock_apply_revision,
        mock_is_db_up_to_date,
        mock_get_current_version,
        mock_check,
        mock_ensure_db,
    ):
        self.handler.apply()
        mock_check.assert_called_once()
        mock_get_current_version.assert_called()
        mock_upgrade_head.assert_called_with("rev_123")
        mock_apply_revision.assert_called_once()

    @patch("omni.pro.check_migration.AlembicMigrateCheck.get_current_version", return_value="version_1")
    @patch("omni.pro.check_migration.AlembicMigrateCheck.is_database_up_to_date", return_value=True)
    @patch("omni.pro.check_migration.AlembicMigrateCheck.apply_revision")
    def test_apply_no_upgrade_needed(self, mock_apply_revision, mock_is_db_up_to_date, mock_get_current_version):
        self.handler.apply()
        mock_apply_revision.assert_called_once()
        mock_is_db_up_to_date.assert_called_once()

    @patch("omni.pro.check_migration.AlembicMigrateCheck.get_postgres_config")
    def test_get_postgres_config(self, mock_get_postgres_config):
        self.handler.get_postgres_config("service_id", "tenant_code")
        mock_get_postgres_config.assert_called_once_with("service_id", "tenant_code")

    @patch("omni.pro.check_migration.command.upgrade")
    @patch("omni.pro.check_migration.logger")
    def test_upgrade_head(self, mock_logger, mock_upgrade):
        self.handler.upgrade_head()
        mock_upgrade.assert_called_once_with(self.handler.alembic_config, "head")

    @patch("omni.pro.check_migration.inspect_sqlalchemy")
    def test_check_alembic_version_table(self, mock_inspect):
        mock_inspector = MagicMock()
        mock_inspect.return_value = mock_inspector
        mock_inspector.has_table.return_value = False
        result = self.handler.check()
        self.assertFalse(result)
        mock_inspector.has_table.assert_called_once()


if __name__ == "__main__":
    unittest.main()
