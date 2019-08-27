#!/bin/bash

set -x
set -e
set -o pipefail

dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
pushd $dir

docker build \
    --no-cache \
    -f ../install/docker/Dockerfile \
    -t mellon-app \
    ..

popd
