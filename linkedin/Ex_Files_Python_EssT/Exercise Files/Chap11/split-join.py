#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# Python allows to split / join string based on separator character

s = 'This is a long string with a bunch of words in it.'

# splits based on spaces, tabs and new lines
print(s.split())

s = 'This is a long     string \t with a bunch of      words in it.'
print(s.split())

s = '''
This is a \t
 long        string
  with a bunch of      words in it.'''
print(s.split())

print(s.split('i')) # this will split on letter i and spaces/tabs/newlines will remain as they are

s = 'This is a long string with a bunch of words in it.'
l = s.split()
print(':'.join(l)) # This:is:a:long:string:with:a:bunch:of:words:in:it.
