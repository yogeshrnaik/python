#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def printSeparator():
    print('*****************************************************************')

def main():
    animals = { 'kitten': 'meow', 'puppy': 'ruff!', 'lion': 'grrr',
        'giraffe': 'I am a giraffe!', 'dragon': 'rawr' }
    print_dict(animals)
    printSeparator()
    
    # another way to create dictonary
    # this is convenient only when using keys are strings.
    # anything else as key not possible with this way of creating dictonary
    animals = dict(kitten = 'meow', puppy = 'ruff!', lion = 'grrr',
        giraffe = 'I am a giraffe!', dragon = 'rawr')
    print_dict(animals)
    printSeparator()

    # another way of iterating dictonary
    for k,v in animals.items():
        print(f'{k}: {v}')    
    printSeparator()

    # we can get just keys or just values
    print(animals.keys(), type(animals.keys())) # <class 'dict_keys'>
    print(animals.values(), type(animals.values())) # <class 'dict_values'>
    printSeparator()

    # access particular value
    print(animals['lion'])
    animals['lion'] = 'I am Lion!'
    print(animals['lion'])

    # add new item in dictonary
    animals['monkey'] = 'I am Monkey'
    print(animals)
    printSeparator()

    # check if a value exists
    print('lion' in animals)
    print('lion found' if 'lion' in animals else 'no lion found')

    # accessing by a key that does not exist throws KeyError
    # print(animals['godzilla']) # throws KeyError: 'godzilla'
    # to avoid this error use dict.get('key') instead
    print('Godzilla:', animals.get('godzilla')) # returns None if key does not exist

def print_dict(d):
    for key in d: print(f'{key}: {d[key]}')

if __name__ == '__main__': main()
