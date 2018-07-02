#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# str is built in Python class for String representation
class RevStr(str):
    def __str__(self):
        # this returns slice of string where the step goes backwards
        # so it reverses the string
        return self[::-1]

def main():
    hello = RevStr('Hello, World.')
    print(hello)

if __name__ == '__main__': main()
