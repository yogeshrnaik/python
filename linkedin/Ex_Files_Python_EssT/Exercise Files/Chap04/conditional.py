#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

if True:
    print('if true')
elif False:
    print('elif true')
else:
    print('neither true')

def printSeparator():
    print('*****************************************************************')

def comparisonOperators():
    printSeparator()
    print('comparisonOperators()')
    a = 10
    b = 10
    print(f'a={a}, b={b}: a == b : ', a == b)
    print(f'a={a}, b={b}: a != b : ', a != b)
    print(f'a={a}, b={b}: a > b : ', a > b)
    print(f'a={a}, b={b}: a < b : ', a < b)
    print(f'a={a}, b={b}: a >= b : ', a >= b)
    print(f'a={a}, b={b}: a <= b : ', a <= b)

def logicalOperators():
    printSeparator()
    print('logicalOperators()')
    a = 10
    b = 5
    if a % 5 == 0 and b % 5 == 0:
        print(f'Both {a} and {b} are divisible by 5')

    if a % 10 == 0 or b % 10 == 0:
        print(f'Either {a} and {b} is divisible by 10')
    
    if not b % 10 == 0:
        print(f'{b} is not divisible by 10')

def identityOperators():
    printSeparator()
    print('identityOperators()')
    x = 1
    y = 1
    if x is y:
        print(f'x={x} and y={y} are same objects')
    
    y = 2
    if x is not y:
        print(f'x={x} and y={y} are not same objects')


def membershipOperators():
    printSeparator()
    print('membershipOperators()')
    l = [1,2,3]
    if 1 in l:
        print(f'1 is present in {l}')
    if 4 not in l:
        print(f'4 is not present in {l}')

    s = {1, 2, 3, 3}
    if 2 in s:
        print(f'2 is present in {s}')
        
    if 4 not in s:
        print(f'4 is not present in {s}')

    d = {1: '1', 2: '2'}
    if 2 in d:
        print(f"Key 2 is present in {d}")
    
    if (1, '1') in d.items():
        print("{1 : '1'} is present in ", d)
    
    if (2, '1') not in d.items():
        print("{2 : '1'} is not present in ", d)

def main():
    comparisonOperators()
    logicalOperators()
    identityOperators()
    membershipOperators()

if __name__ == "__main__":
    main()
