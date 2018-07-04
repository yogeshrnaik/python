#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    infile = open('./Chap12/berlin.jpg', 'rb') # read and binary mode (text mode is default)
    outfile = open('./Chap12/berlin-copy.jpg', 'wb') # write and binary mode (text mode is default)

    while True:
        buf = infile.read(10240) # 10KB
        if buf:
            outfile.write(buf)
            print('.', end='', flush=True)
        else: break

    outfile.close()
    infile.close()
    print('\ndone.')

if __name__ == '__main__': main()
