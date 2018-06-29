#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def printSeparator():
    print('*****************************************************************')

def main():
    printSeparator()
    print("Variable Keyword arguments...")
    variableKeywordArgsExample(Buffy = 'meow', Zilla = 'grr', Angel = 'rawr')

    printSeparator()
    print("Variable Keyword arguments using dictonary variable...")
    d1 = dict(formal = 'Hello', informal = 'Hey', neutral = 'Hi')
    variableKeywordArgsExample(**d1)

    printSeparator()
    print("Variable Keyword arguments using dictonary variable...")
    d2 = {'one': 1, 'two': 2, 'three': 3}
    variableKeywordArgsExample(**d2)

    printSeparator()
    print("Variable Keyword arguments but nothing passed...")
    variableKeywordArgsExample()
    

# Keyword arguments are dictonary instead of tuple when we use **
# This allows to have variable number of named arguments
def variableKeywordArgsExample(**kwargs):
    print(f'Type of **kwargs is: {type(kwargs)}') # type is dictonary
    if len(kwargs):
        for k in kwargs:
            print('[{}] says [{}]'.format(k, kwargs[k]))
    else: print('No argument passed.')

if __name__ == '__main__': main()
