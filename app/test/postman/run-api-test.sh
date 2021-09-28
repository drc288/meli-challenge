#!/usr/bin/env bash

SCRIPTDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"

npx newman run $SCRIPTDIR/meli-test.postman_collection.json
