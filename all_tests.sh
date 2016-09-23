#!/bin/bash

set -euo pipefail

while read d; do
    pushd "test/$d" > /dev/null
    while read t; do
        echo "Running $t..."
        python "$t"
    done < <(ls test_*.py)
    popd > /dev/null
done < <(ls test)

echo "All tests OK!"
