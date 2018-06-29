#!/usr/bin/env python3
def printSeparator():
    print('--------------------------------------------------------------')

def idOfValueAtIndex(collName, coll, index):
    print(f'id({collName}[{index}]): {id(coll[index])}, ' + 
        f'value at {collName}[{index}] = {coll[index]}')

def areSameObjects(o1, o2): 
    # check to see if two objects are exactly the same
    return o1 is o2

def type_and_id_example():
    x = (1, 'two', 3.0, [4, 'four'], 5)
    y = (1, 'two', 3.0, [4, 'four'], 5)

    # ID function returns an unique identifier for each object
    print(f'id(x): {id(x)}')
    print(f'id(y): {id(y)}')
    printSeparator()
    
    # this prints same unique identifier as both x[0] and y[0] = 1
    idOfValueAtIndex('x', x, 0)
    idOfValueAtIndex('y', y, 0)
    printSeparator()

    idOfValueAtIndex('x', x, 1)
    idOfValueAtIndex('y', y, 1)
    printSeparator()

    # check to see if they are exactly same objects
    if x[0] is y[0]: print('same')
    else: print('not same')

    if x is y: print('same')
    else: print('not same')

def checkInstanceOf(x):
    if isinstance(x, tuple):
        print(f'{x} is tuple')
    elif isinstance(x, list):
        print(f'{x} is list')
    elif isinstance(x, set):
        print(f'{x} is set')
    elif isinstance(x, dict):
        print(f'{x} is dict')
    else:
        print(f'{x} is neither tuple nor list nor set nor dict')

def instanceOfExample():
    printSeparator()
    print('instanceOfExample()')
    x = (1, 'two', 3.0, [4, 'four'], 5)
    y = [1, 'two', 3.0, [4, 'four'], 5]
    checkInstanceOf(x)
    checkInstanceOf(y)
    checkInstanceOf([1,2])
    checkInstanceOf({'1', '2'})
    checkInstanceOf({1: '1', 2: '2'})

def main():
    type_and_id_example()
    instanceOfExample()

if __name__ == "__main__":
    main()