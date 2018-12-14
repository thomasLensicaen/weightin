#!/usr/bin/env sh

# TODO : move script ?

LOCAL_DIR=$(dirname $(readlink -f $0))
cd "${LOCAL_DIR}/.."
PYTHON_VERSION=3
PYTHON_BIN=/usr/local/bin/python${PYTHON_VERSION}
VENV=".venv_weightin"
${PYTHON_BIN} -m venv ${VENV}
#${VENV}/bin/pip install --upgrade pip --trusted-host pypi.org --trusted-host files.pythonhosted.org
${VENV}/bin/pip install -r scripts/requirements.txt
