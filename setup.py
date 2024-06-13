from pathlib import Path

from setuptools import find_packages, setup

# The directory containing this file
HERE = Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()
DESCRIPTION = "Python library designed to be a utility for OMS microservices"
VERSION = "0.0.0"
PACKAGE_NAME = "omni-pro"
AUTHOR = "OMNI.PRO"
AUTHOR_EMAIL = "development@omni.pro"
URL = "https://github.com/Omnipro-Solutions/saas-ms-library"
INSTALL_REQUIRES = [
    "boto3==1.34.101",
    "mongoengine==0.27.0",
    "marshmallow==3.21.2",
    "SQLAlchemy==2.0.24",
    "sqlalchemy-utils==0.41.1",
    "networkx==3.1",
    "unidecode==1.3.8",
    "omni-pro-base>=0.0.0,<=2.0.0",
    "omni-pro-redis>=0.0.0,<=2.0.0",
    "omni-pro-grpc>=0.0.0,<=2.0.0",
    "apache-airflow-client==2.8.0",
    "newrelic==9.10.0",
    "alembic==1.11.2",
    "blinker==1.7.0",
]
# with open(HERE / "requirements.txt") as f:
#     INSTALL_REQUIRES = f.read().splitlines()

# This call to setup() does all the work
setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type="text/markdown",
    url=URL,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="MIT",
    packages=find_packages(exclude=("tests",)),
    package_data={"": ["*.pyi", "data/*.csv"]},
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
    ],
    extras_require={
        "dev": [
            "pytest",
        ]
    },
    test_suite="tests",
    python_requires=">=3.9",
)
