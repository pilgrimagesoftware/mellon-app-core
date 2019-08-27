#!/bin/bash

set -x
set -e
set -o pipefail

dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
pushd $dir

ngrok http 5000

popd
