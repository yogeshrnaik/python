#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import sys
import os
import random
from datetime import datetime

def printSeparator():
    print('*****************************************************************')

def main():
    v = sys.version_info
    print('Python version {}.{}.{}'.format(*v))
    print(sys.platform)
    printSeparator()

    print(os.name)
    print(os.getenv('JAVA_HOME'))
    print(os.getcwd())
    print(os.urandom(20).hex())
    printSeparator()

    x = random.randint(1, 1000)
    print(x)

    l = list(range(25))
    random.shuffle(l)
    print(l)
    printSeparator()

    now = datetime.now()
    print(now)
    print(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)

if __name__ == '__main__': main()
