#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Animal:
    x = [1,2,3] # this is class variable and not object variable

    def __init__(self, **kwargs):
        # all variables define as self.variableName as object level variables
        self._type = kwargs['type'] if 'type' in kwargs else 'kitten'
        self._name = kwargs['name'] if 'name' in kwargs else 'fluffy'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'meow'

    def type(self, t = None):
        if t: self._type = t
        return self._type

    def name(self, n = None):
        if n: self._name = n
        return self._name

    def sound(self, s = None):
        if s: self._sound = s
        return self._sound

    def __str__(self):
        return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}".'

def main():
    a0 = Animal(type = 'kitten', name = 'fluffy', sound = 'rwar')
    a1 = Animal(type = 'duck', name = 'donald', sound = 'quack')
    print(a0)
    print(a1)

    # we can access the class level variable using any object.variableName
    a0.x[0] = 10
    print(a0.x)

    # can also access it as ClassName.variableName syntax
    Animal.x[1] = 20
    print(Animal.x)

if __name__ == '__main__': main()
