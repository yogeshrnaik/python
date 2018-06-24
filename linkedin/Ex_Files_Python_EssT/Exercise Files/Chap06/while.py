#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

secret = 'swordfish'
pw = ''
auth = False
count = 0
max_attempts = 5


while pw != secret:
    count += 1
    if count > max_attempts: break
    if count == 3: continue
    pw = input(f"{count}: What's the secret word? ")
else: # else clause gets executed when while condition is no longer true i.e. loops exits normally
    print('Correct password was entered...')
    auth = True

print("Authorized" if auth else "Not authorized")