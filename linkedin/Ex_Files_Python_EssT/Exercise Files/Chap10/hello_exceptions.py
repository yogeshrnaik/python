#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
import sys

def main():
    try:
        # x = int('foo') # ValueError
        # x = 5/0 # ZeroDivisionError
        x = 5/3

        nums = [1]; nums[1] = 0 # trying to access index that is not present
    except ValueError:
        print('Got ValueError')
    except ZeroDivisionError:
        print('Got ZeroDivisionError')
    except:
        # default catch for unknown errors
        print(f'Unknown error: {sys.exc_info()}')
    else:
        # this else block will be executed when there is no error 
        print(f'No error today and x = {x}')

if __name__ == '__main__': main()
