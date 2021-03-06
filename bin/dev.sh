#!/bin/bash
cd $(dirname $(dirname $(realpath $0)))

find -type f \
     | grep -v -e .backup -e .git -e egg -e pycache \
     | grep -vE "\.c$|\.o$|\.so$" \
     | sudo -E entr -r bash -c '

find -type f \
    | grep -E "\.c$|\.o$|\.so$" \
    | xargs rm -fv

./bin/tinysnitchd

'
