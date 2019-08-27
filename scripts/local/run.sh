#!/bin/bash

set -x
set -e
set -o pipefail

srcdir=${1:-src}

dir=$(pwd)
scriptdir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
pushd $srcdir

# . $dir/.env
pipenv run ./run.py --debug

popd
