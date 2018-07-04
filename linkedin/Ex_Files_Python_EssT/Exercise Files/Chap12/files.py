#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def printSeparator():
    print('*****************************************************************')

def readFile(fileName):
    print('Reading file...')
    f = open(fileName) # by default opens in read-only mode
    readFromFile(f)
    f.close()
    printSeparator()

def writeFile(fileName):
    print('Writing file...')
    f = open(fileName, 'w') # 2nd param for mode (read 'r', write 'w' and append 'a')
    # In write mode, file will be emptied if present or new file created if file not present 
    writeToFile(f, 'w', 2)
    f.close()
    printSeparator()

def appendFile(fileName):
    print('Appending to file...')
    f = open(fileName, 'a') # 2nd param for mode (read 'r', write 'w' and append 'a')
    # In append mode, file will be appended if present or new file created if file not present 
    writeToFile(f, 'a', 3)
    f.close()
    printSeparator()

def readFromFile(f):
    print('Reading from file..............................................')
    print(f'Type of Read File object [f] is: [{type(f)}]') # class '_io.TextIOWrapper'
    for line in f:
        print(f'Line from file: {line.rstrip()}') # rstrip removes the trailing whitespaces including newline
    print('Finished reading from file.')

def writeToFile(f, mode, count):
    print('Writing to file..............................................')
    print(f'Type of Write File object [f] is: [{type(f)}]') # class '_io.TextIOWrapper'
    print(f'Writing [{count}] lines in file in [{mode}] mode...')
    for num in range(count):
        f.write(f'Line {num}.\n')
    print('Finished writing to file.')

def readWrite(fileName, mode):
    print(f'In readWrite() method with mode: [{mode}]')
    f = open(fileName, mode) # also works with w+ and a+
    readFromFile(f)
    writeToFile(f, mode, 4)
    f.close()
    printSeparator()

def main():
    readFile('./Chap12/lines.txt')
    writeFile('./Chap12/lines.txt')
    appendFile('./Chap12/lines.txt')
    readWrite('./Chap12/lines.txt', 'r+') # r+ works as append mode
    printSeparator()
    readWrite('./Chap12/lines.txt', 'w+') # w+ will overwrite existing file if present
    printSeparator()
    readWrite('./Chap12/lines.txt', 'a+') # a+ works as append mode
    printSeparator()

if __name__ == '__main__': main()

# to read text file we can use 'rt' (by default it is text mode)
# to write or append to text file we can use 'wt' or 'at' (by default it is text mode)

# to read binary file we can use 'rb'
# to write or append to binary file, we can use mode as 'wb' or 'ab'

# to read and write, we can use 'r+t', 'r+b', 'w+t', 'w+b', etc.
