#!/bin/bash

set -x
set -e
set -o pipefail

dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
pushd $dir

docker-compose \
    -p mellon \
    -f $dir/docker-compose.yaml \
    up

popd
