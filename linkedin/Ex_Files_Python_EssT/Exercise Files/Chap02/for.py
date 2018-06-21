#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

words = ['one', 'two', 'three', 'four', 'five']

for w in words:
    print(w)

# w variable remains in scope outside the loop
print(f"Last word: {w}")
