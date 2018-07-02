#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def printSeparator():
    print('*****************************************************************')

class Animal:
    # Note: We have not defined _type, _name and _sound as class variables
    # e.g.
    # _type = 'Animal type'
    # _name = 'Animal name'
    # _sound = 'Animal sound'
    # hence, these variables are created when object of Animal class is created
    # they are not present in class Animal but only in its objects
    # so we cannot say Animal._type or Animal._name
    # we must first create object of Animal and then use objectName._type etc.

    # __init__ method acts as constructor
    def __init__(self, type, name, sound):
        self._type = type
        self._name = name
        self._sound = sound

    def type(self):
        return self._type

    def name(self):
        return self._name

    def sound(self):
        return self._sound

def print_me(o):
    if not isinstance(o, Animal) and not isinstance(o, Bird):
        raise TypeError('print_me(): requires an Animal or Bird')
    print('The {} is named "{}" and says "{}".'.format(o.type(), o.name(), o.sound()))

class Bird:
    # we can use keyword arguments
    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'UnknownBirdType'
        self._name = kwargs['name'] if 'name' in kwargs else 'NoName'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'NoSound'

    def type(self):
        return self._type

    def name(self):
        return self._name

    def sound(self):
        return self._sound

def main():
    print('Animals....')
    a0 = Animal('kitten', 'fluffy', 'rwar')
    a1 = Animal('duck', 'donald', 'quack')
    print_me(a0)
    print_me(a1)
    print_me(Animal('velociraptor', 'veronica', 'hello'))
    printSeparator()

    print('Birds....')
    chicken = Bird(type='chicken', name='Chick', sound='cok cok')
    # since we use keyword arguments, we can change the order of arguments
    crow = Bird(name='Carl', type='crow', sound='ca ca')
    print_me(chicken)
    print_me(crow)
    print_me(Bird())

if __name__ == '__main__': main()
