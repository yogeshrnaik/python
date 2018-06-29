#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def printSeparator():
    print('*****************************************************************')

def f1():
    print('this is f1')

x = f1
x()

print(f'Type of x is: {type(x)}') # type is 'function'
printSeparator()

def function1(func):
    y = 10
    # we can define function inside function in python
    def function2():
        print('this is function2 - before function call')
        func()
        print('this is function2 - after function call')

    # function can return another function
    return function2

# using @function1 will decorate function3
# this is: it function1() take a function as argument. 
# function3() will be passed to function1() when we call function3()
# it is equivalent to doing following
# function3 = function1(function3)
# function3() # this will call the function2() returned by function1()
@function1
def function3():
    print('this is function3')

printSeparator()
print('calling function3()')
 # this actually executes the code inside function2(). 
 # inside function2() there is call to func() which executes the code inside function3() above
function3()
# output of above function3() call:
# this is function2 - before function call
# this is function3
# this is function2 - after function call
printSeparator()
