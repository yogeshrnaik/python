#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Duck:
    sound = 'Quaaack like a duck!'
    walking = "Walks like a duck!"

    # first parameter of every method of class must be "self"
    # we can name it whatever we want but it is common practice to name it "self"
    # "self" is reference to the object being created
    def quack(self):
        print("inside quack()...")
        print(f"self.sound={self.sound}")
         # one can change the variables of class using self.<variable_name>
        self.sound = "Quaaack Quaaack!"

    def walk(self):
        print("inside walk()...")
        print(f"self.walking={self.walking}")

def main():
    donald = Duck()
    donald.quack() # "self" refers to donald object in this case
    donald.walk()
    print("calling quack() again...")
    donald.quack()

if __name__ == '__main__': main()
