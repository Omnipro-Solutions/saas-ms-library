#!/bin/bash

set -e

pip uninstall omni-pro -y

rm -Rf build/ dist/ omni_pro.egg-info/

python setup.py sdist bdist_wheel

pip install dist/omni_pro-0.0.0-py3-none-any.whl

rm -Rf build/ dist/ omni_pro.egg-info/