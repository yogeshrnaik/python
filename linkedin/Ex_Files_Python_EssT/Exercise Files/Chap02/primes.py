#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
import math

def isprime(n):
    if n <= 1:
        return False
    for x in range(2, 1 + math.floor(math.sqrt(n))):
        if n % x == 0:
            return False
    else:
        return True

n = 5
if isprime(n):
    print(f'{n} is prime')
else:
    print(f'{n} not prime')

print("Prime numbers between 1 to 100 are:")
for i in range(101):
    if isprime(i):
        print(i, end = ' ', flush = True)
