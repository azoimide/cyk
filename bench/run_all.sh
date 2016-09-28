#!/bin/bash

if ! [ -d out ]; then
    mkdir out
fi

while read g; do
    for mode in gen rand; do
        for alg in td bu naive; do
            name="$alg""_""$mode""_""$g"".csv"
            echo "$name"
            python bench.py "$alg" "$mode" < "$g" > "out/$name"
        done
    done
done < <(/bin/ls grammar*)
