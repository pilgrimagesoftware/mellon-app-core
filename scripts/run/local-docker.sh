#!/bin/bash

set -x
set -e
set -o pipefail

dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

pushd $dir/../..

docker run \
    -d \
    --env-file .env \
    -e HOST=0.0.0.0 \
    --rm \
    --name mellon-app \
    -p 5000:5000 \
    sweetrpg/mellon-app

popd
