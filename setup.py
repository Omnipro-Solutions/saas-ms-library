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
    "protobuf==4.23.4",
    "grpcio==1.56.0",
    "grpcio-tools==1.56.0",
    "boto3==1.28.4",
    "mongoengine==0.27.0",
    "marshmallow==3.19.0",
    "hiredis==2.2.3",
    "redis==4.6.0",
    "peewee==3.16.2",
    "fakeredis[json]==2.17.0",
]

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
