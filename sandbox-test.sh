#!/bin/bash

set -e 

rm -rf tst || true
mkdir tst
pushd tst
# test installation of module in virtual environment
virtualenv my-venv
source my-venv/bin/activate

pip3 install printb
python3 ../test-bidi.py

echo "everything is fine. test passed"

deactivate

#rm -rf my-venv

popd tst
