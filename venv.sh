#!/usr/bin/env bash

cd -P "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")"

if [ ! -d ./venv ]; then
	virtualenv -p python3.6 venv
	. ./venv/bin/activate
	./venv/bin/pip3 install -r requirements.txt
else
	. ./venv/bin/activate
fi

export PYTHONPATH=`pwd`/src
export PATH=`pwd`/bin:"$PATH"
