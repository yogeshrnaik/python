#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# Ternary operator available since Python 2.5

hungry = True
x = 'Feed the bear now!' if hungry else 'Do not feed the bear.'
print(x)

x = 'Feed' if False else 1
print(x)