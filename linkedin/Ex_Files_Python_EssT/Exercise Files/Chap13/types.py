#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def printSeparator():
    print('*****************************************************************')

# this is a decorator
def conversion(conversionFunc):
    def wrapper(argsToConvert):
        print(f'argsToConvert={argsToConvert} and type(argsToConvert)=[{type(argsToConvert)}]')
        convertedValue = conversionFunc(argsToConvert)
        print(f'convertedValue={convertedValue} and type(convertedValue)=[{type(convertedValue)}]')
        printSeparator()
    return wrapper

@conversion
def convertToInt(x):
    return int(x)

@conversion
def convertToFloat(x):
    return float(x)

@conversion
def absExample(x):
    return abs(x)

@conversion
def divModByThree(x):
    return divmod(x, 3) # returns tuple (quotient, reminder)

@conversion
def convertToComplex(x):
    return x + 73j # Python uses j for imaginary part instead of i
    
@conversion
def complexWithConstructor(x):
    return complex(x, 45)
    
def main():
    convertToInt('47')
    convertToFloat('47')
    absExample(-47)
    absExample(-47.3)
    divModByThree(47)
    convertToComplex(10)
    complexWithConstructor(55)

if __name__ == '__main__': main()
