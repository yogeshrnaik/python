#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def printSeparator():
    print('*****************************************************************')

class Duck:
    # This are class level variables.
    sound = 'Quack quack.'
    movement = 'Walks like a duck.'

    # first param of every method of class has to be reference to object
    # we can name it anything we want 
    # but it is general practice to name it 'self'
    def quack(self):
        print(self.sound)

    def move(self):
        print(self.movement)

def print_sound(duckName, duck):
    print(f'{duckName}.sound : {duck.sound}')

def main():
    print('Creating donald object of Duck class and calling its methods')
    donald = Duck()
    donald.quack()
    donald.move()
    printSeparator()

    donaldsBrother1 = Duck()
    print("Change sound in Duck class. " + 
        "All sound variables in all objects of Duck class will change because of this...")
    # this changes the class level variable 'sound' 
    # for all objects of Duck class created before this and any object created after this
    Duck.sound = "We sound like Donald"
    donaldsBrother2 = Duck() # Brother 2 will also have 'We sound like Donald' as sound
    print(f'Duck.sound: {Duck.sound}')
    print(f'donald.sound : {donald.sound}')
    print(f'donaldsBrother1.sound : {donaldsBrother1.sound}')
    print(f'donaldsBrother2.sound : {donaldsBrother2.sound}')
    printSeparator()
    
    print("Change sound for Donald's brother 1")
    # This changes sound only for Donald's brother 1 object
    donaldsBrother1.sound = "Donald's brother 1 sound"
    print(f'Duck.sound: {Duck.sound}')
    print(f'donald.sound : {donald.sound}')
    print(f'donaldsBrother1.sound : {donaldsBrother1.sound}')
    print(f'donaldsBrother2.sound : {donaldsBrother2.sound}')
    printSeparator()

    print('Type of class vs type of object of class')
    print(f'type(Duck) = {type(Duck)}') # <class 'type'>
    print(f'type(donald) = {type(donald)}') # <class '__main__.Duck'>
    print(f'type(donaldsBrother1) = {type(donaldsBrother1)}') # <class '__main__.Duck'>

if __name__ == '__main__': main()
