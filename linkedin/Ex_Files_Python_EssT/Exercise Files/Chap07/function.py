#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def printSeparator():
    print('*****************************************************************')

def main():
    x = kitten()
    # x = None as kitten() is not returning any value
    print(x)

    puppies(10) # 2nd and 3rd param will get default value
    puppies(10, 20) # 3rd param will get default value
    puppies(10, 20, 30)

    # Python has 'call by value' approach just like in Java
    # so even if we change the value of a parameter inside function
    # the value of variable passed to it by caller
    # does not change in case of immutable objects like integers
    # but in case of mutable objects like list this changes
    a = 10
    names = ['name1', 'name2'] # names is a mutable list
    cubs(a, names)
    print(f'a is {a} in main()') # a is still 10 here
    print(f'names is {names} in main()') # names[0] changed by cubs()

# all functions always return a value
# when no return is mentioned inside function
# then it returns None as value
def kitten():
    print('Meow.')

# We can provide default values to function parameters
# params having default values has to be the last parameters
# e.g. we cannot add param 'd' without default value after c 
# def puppies(a, b=1, c=0, d): # non-default argument follows default argument 
def puppies(a, b=1, c=0, d='dog'):
    printSeparator()
    print("Wof wof!")
    print(a, b, c, d)

# Python has 'call by value' approach just like in Java
# so even if we change the value of a parameter inside function
# the value of variable passed to it by caller
# does not change in case of immutable objects like integers
# but in case of mutable objects like list this changes
def cubs(a, names):
    printSeparator()
    print(f'Roar! a passed to me is {a} and names passed to me is {names}')
    a = 3
    names[0] = 'changed-name'
    print(f'I modified a to {a} in cubs()') # a becomes 3 now
    print(f'I modified names[0] to [{names[0]}] in cubs()') # names[0] = 'changed-name'

# __name__ will be initialized to the name of the module 
# when this module is imported in another module
# in case if we are running this file directly then
# __name__ will be initialized to '__main__'
# hence we have this condition below
if __name__ == '__main__': main()
# another reason is that since Python is interpreted at runtime
# we cannot use a function/variable before it is declared
# in this file, we have kitten() declared after it is used inside main() already
# this works here because we have above if condition
# so python reads the complete file and then runs main() when it 
# encouters above condition
