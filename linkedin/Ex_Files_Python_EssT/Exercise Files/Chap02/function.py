#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def function(n = 1): # n is given a default value
    print(n)

function(47)

 # since n is given a default value, we can call this function without any parameter as well
function()

# all functions return value
# for function that do not explicitly return any value, they return "None"
x = function(10)
print(f"Function returned: {x}") # x is None in this case

def divide(x, y):
    if (y != 0): return x / y

z = divide(10, 5)
print(f"divide(10, 5) returned: {z}") # z here is 2.0
z = divide(10, 0)
print(f"divide(10, 0) returned: {z}") # z here is "None"

