#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# This file has examples of list, set, range, dictonary data types 

def printSeparator():
    print('*****************************************************************')

def printCollection(coll):
    print('------------------------')
    print(f'Type of collection: {type(coll)} - Collection: {coll}')
    for i in coll:
        print(i, end = ' ', flush = True)
    print()

def printHetrogenous(coll):
    print('------------------------')
    print(f'Type of collection: {type(coll)} - Collection: {coll}')
    for i in coll:
        print(f'type of {i} is {type(i)}')
    print()

def printHetrogenousDictonary(d):
    print('------------------------')
    print(f'Type of collection: {type(d)} - Collection: {d}')
    for k, v in d.items():
        print(f'key: {k}, keyType: {type(k)} and value: {v}, valueType: {type(v)}')
    print()

def printDictonary(d):
    for k, v in d.items():
        print(f'key: {k} and value: {v}')

def listExample():
    printSeparator()
    print('listExample()')
    x = [ 1, 2, 3, 4, 5 ]
    # Index starts at 0
    x[2] = 42
    printCollection(x)

def setExample():
    printSeparator()
    print('setExample()')
    # every element of set has to be hashable
    # TypeError: unhashable type: 'list'
    # s = {'1', 2, 3.5, ['a', 'b']}
    # this set contains a 'list' and hence we get above error

    # same error when we try to put set inside set
    # s = {'1', 2, 3.5, 2, {'a', 2.5, 'c'}}

    s = {'1', 2, 3.5, 'd'}
    printHetrogenous(s)

def tupleExample():
    printSeparator()
    print('tupleExample()')
    # Tuple is immutable list. use parenthesis to denote Tuple
    t = (1, 2, 3, 4, 5)
    # t[2] = 42 # This gives error: 'tuple' object does not support item assignment
    printCollection(t)

def rangeExample():
    printSeparator()
    print('rangeExample()')
    # range starts with 0 and last element is exclusive
    r = range(5) # this creates range from 0 to 4
    printCollection(r)

    # we can specify the start of the range
    r = range(5, 10)
    printCollection(r)

    # we can specify by how much we want to step by
    r = range(5, 50, 10) # step by 10
    printCollection(r)

    # range is immutable
    r = range(10)
    # r[2] = 10 # this gives error: 'range' object does not support item assignment

def listFromRangeExample():
    printSeparator()
    print('listFromRangeExample()')
    # if we want mutable range then we create a list from the range
    listFromRange = list(range(1, 6))
    listFromRange[2] = 10
    printCollection(listFromRange)

def dictonaryExample():
    printSeparator()
    print('dictonaryExample()')
    d = {'one': 1, 'two': 2, 'three': 3}
    printCollection(d) # this will only print keys
    printDictonary(d)

    # dictory is mutable
    d['three'] = 33
    printDictonary(d)

def hetrogenous():
    printSeparator()
    print('hetrogenous()')
    # list, tuple can contain hetrogenous types
    # each element of these collections can be of different type
    l = ['1', 2, 3.5, ['a', 'b'], {1: 'a', 2.0: 'b'}, ('tuple1', 'tuple2')]
    printHetrogenous(l)

    t = ('1', 2, 3.5, ['a', 'b'], {1: 'a', 2.0: 'b'}, ('tuple1', 'tuple2'))
    printHetrogenous(t)

def hetrogenousDictonary():
    # we can have all kinds of keys and values inside dictonary
    # but it is not allowed to have dictonary as key inside dictonary
    d = {
            'one': 1, 
            2: 2.0001, 
            3.0: [3], 
            (4, 5): (3.99, 4.00, 4.01),
            6: 'six',
            6.5: {'6.5': 6.5} # dictonary as a value is allowed but not as a key
            #,{'7': 7} : {8: '8'} # TypeError: unhashable type: 'dict' - dictonary as key not allowed
        }
    printHetrogenousDictonary(d)

def main():
    listExample()
    setExample()
    tupleExample()
    rangeExample()
    listFromRangeExample()
    dictonaryExample()
    hetrogenous()
    hetrogenousDictonary()

if __name__ == "__main__":
    main()