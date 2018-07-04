#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def printSeparator():
    print('*****************************************************************')

class MyString(str):
    def __str__(self):
        return self[::-1]

def string_methods():
    print('Hello, World.'.upper())
    print('Hello, World.'.swapcase())
    print('Hello, World.'.capitalize())
    print('hello, world.'.title())
    print('Hello, World. {}'.format(42*2))
    printSeparator()

def multiline_string():
    # Using triple single or double quotes to have multi-line string
    print("""
        Hello, 
        World. 
        {}
        """
        .format(42*2))
    printSeparator()

def string_inheritance():
    print(MyString('Hello world'))
    s = 'Hello'
    print(MyString(s))
    printSeparator()

def immutable_string():
    # String is immutable in Python
    s1 = 'Hello'
    s2 = s1.upper()
    print(f'ID of {s1}: {id(s1)}\nID of {s2}: {id(s2)}')
    printSeparator()

    s3 = 'Hi'
    s4 = 'Hi'
    # s3 and s4 will have same ID because they point to same string literal
    print(f'ID of {s3}: {id(s3)}\nID of {s4}: {id(s4)}')
    printSeparator()

    s3 = 'HEY'
    s4 = s3.upper() # creates a new object
    # s3 and s4 will have different IDs even though their values are same
    print(f'ID of {s3}: {id(s3)}\nID of {s4}: {id(s4)}')
    printSeparator()

def concat_strings():
    # concat strings
    s1 = 'this string'
    s2 = 'that string'
    print(s1 + ' ' + s2)
    printSeparator()

    # concat string literal without + operator
    s3 = 'this' ' that'
    print(s3)
    printSeparator()

def string_format():
    x = 10
    y = 20
    print('x={} y={}'.format(x, y))
    print(f'x={x} y={y}')
    
    print('x={xx} y={yy}'.format(yy = y, xx = x)) # with named arguments
    print(f'x={x} y={y}')
    
    print('x={1} y={0} x={1}'.format(y, x)) # with positional arguments
    print(f'x={x} y={y} x={x}')
    printSeparator()

def left_right_justify():
    x = 12
    y = 234
    print('x=[{0:<5}] and y=[{1:>5}]'.format(x, y))     # x=[12   ] and y=[  234]
    print('x=[{0:<05}] and y=[{1:>05}]'.format(x, y))   # x=[12000] and y=[00234]
    print('x=[{0:<+05}] and y=[{1:>+08}]'.format(x, y)) # x=[+1200] and y=[0000+234]
    print('x=[{0:<+05}] and y=[{1:>+}]'.format(x, y))   # x=[+1200] and y=[+234]
    printSeparator()
    print('with f strings instead of string.format()')
    print(f'x=[{x:<5}] and y=[{y:>5}]')     # x=[12   ] and y=[  234]
    print(f'x=[{x:<05}] and y=[{y:>05}]')   # x=[12000] and y=[00234]
    print(f'x=[{x:<+05}] and y=[{y:>+08}]') # x=[+1200] and y=[0000+234]
    print(f'x=[{x:<+05}] and y=[{y:>+}]')   # x=[+1200] and y=[+234]
    printSeparator()

def number_formatting():
    x  = 876 * 7 * 209
    # use comma as thousand separator 
    print('x={:,}'.format(x)) # x=1,281,588
    print('x={:,}'.format(x).replace(',', '.')) # x=1.281.588
    
    print(f'x={x:,}') # x=1,281,588
    print(f'x={x:,}'.replace(',', '.')) # x=1.281.588
    printSeparator()
    
    y = 6.9789
    print('y={:f}'.format(y)) # y=6.978900
    print('y={:.3f}'.format(y)) # y=6.979
    
    print(f'y={y:f}') # y=6.978900
    print(f'y={y:.3f}') # y=6.979
    printSeparator()

    x = 42
    print('x in hexadecimal = [{:x}]'.format(x)) # x in hexadecimal = [2a]
    print('x in octal = [{:o}]'.format(x)) # x in octal = [52]
    print('x in binary = [{:b}]'.format(x)) # x in binary = [101010]
    printSeparator()
    print(f'x in hexadecimal = [{x:x}]') # x in hexadecimal = [2a]
    print(f'x in octal = [{x:o}]') # x in octal = [52]
    print(f'x in binary = [{x:b}]') # x in binary = [101010]

def main():
    string_methods()
    multiline_string()
    string_inheritance()
    immutable_string()
    concat_strings()
    string_format()
    left_right_justify()
    number_formatting()


if __name__ == '__main__': main()
