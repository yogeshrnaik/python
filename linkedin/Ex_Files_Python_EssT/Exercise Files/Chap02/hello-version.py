#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import platform

print('This is python version {}'.format(platform.python_version()))

# Syntax available in Python 3
print('I like python {} as well as python {}'.format(2, 3))
print(f'python {platform.python_version()} is better than {2}')

# This Syntax is from Python 2
print('And, I prefer to use python %d over %d' % (3, 2))
