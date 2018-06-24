#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def printSeparator():
    print('*****************************************************************')

x = 5
y = 3

# Addition operator +
printSeparator()
print('Additional Operator +')
z = x + y
print(f'result is {z}')

# Substraction operator -
printSeparator()
print('Substraction operator -')
z = x - y
print(f'result is {z}')

# Multiplication operator *
printSeparator()
print('Multiplication operator *')
z = x * y
print(f'result is {z}')

# Division operator /
printSeparator()
print('Division operator /')
z = x / y
print(f'result is {z}')

# Integer Division operator //
printSeparator()
print('Integer Division operator //')
z = x // y
print(f'result is {z}')

# Reminder operator %
printSeparator()
print('Reminder operator %')
z = x % y
print(f'result is {z}')

# Unary negative
printSeparator()
print('Unary negative')
z = -2
print(f'z is {z}')
z = -z
print(f'result is {z}')

# Unary positive
printSeparator()
print('Unary positive')
z = 2
print(f'z is {z}')
z = +z
print(f'result is {z}')
z = -2
print(f'z is {z}')
z = +z
print(f'result is {z}')

# Exponent operator **
printSeparator()
print('Exponent operator **')
z = x ** y
print(f'result is {z}')

