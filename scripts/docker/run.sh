#!/bin/bash

set -x
set -e
set -o pipefail

dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
pushd $dir

docker run \
    -it \
    -e VAR=value \
    -p 5000:5000 \
    mellon-app

popd
