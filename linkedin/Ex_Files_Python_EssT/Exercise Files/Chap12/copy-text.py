#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    infile = open('./Chap12/lines.txt', 'rt') # read and text mode (text mode is default)
    outfile = open('./Chap12/lines-copy.txt', 'wt') # write and text mode (text mode is default)
    for line in infile:
        print(line.rstrip(), file=outfile)
        # to write to outfile we can also use outfile.write(line)
        # the differece is that with print() function 
        # we are stripping the trailing new line (using rstrip())
        # and then print() adds the default new line 
        # for the operating system on which we are running this program
        print('.', end='', flush=True)
    outfile.close()
    infile.close()
    print('\ndone.')

if __name__ == '__main__': main()
