#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import platform

version = platform.python_version()

print('This is python version {}'.format(version))

# semicolon is optional. it is required when we have more than one statement on a single line
x = 10; print(x); print("Another string")
