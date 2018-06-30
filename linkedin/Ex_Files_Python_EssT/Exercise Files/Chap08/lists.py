#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def printSeparator():
    print('*****************************************************************')

def main():
    game = [ 'Rock', 'Paper', 'Scissors', 'Lizard', 'Spock' ]
    print_list(game)
    printSeparator()

    # we can access individual element of list using index
    print(game[0])
    print(game[1])
    printSeparator()

    # we can provide range of index to get a sub-list
    print(game[1:3]) # end index is exclusive
    print(f'Type of game[1:3] is: {type(game[1:3])}') # type of sub-list is 'list'
    printSeparator()

    print('Start at index 1, Stop at index 5 and step by 2')
     # start index, end index (exclusive) and step
    print(game[1:5:2]) # prints ['Paper', 'Lizard']
    printSeparator()

    print('Search list using list.index() and it returns the index of the item')
    print(game.index('Paper')) # it does case sensitive search
    # print(game.index('Test')) # throws error if item is not in the list
    printSeparator()

    print('Append item to list using list.append()')
    game.append('Laptop')
    print(game)
    printSeparator()

    print('Inserting item at a particular index using list.insert(index, item)')
    game.insert(1, 'New Item')
    print(game)
    printSeparator()
    
    print('Removing item by value')
    game.remove('New Item')
    print(game)
    printSeparator()
    
    print('Removing item from end of list using list.pop()')
    lastItem = game.pop() # returns the item removed
    print(f'Item removed: {lastItem}')
    print(game)
    printSeparator()
    
    print('Removing item from a particular index using list.pop(index)')
    itemRemoved = game.pop(3) # returns the item removed
    print(f'Item removed: {itemRemoved}')
    print(game)
    printSeparator()
    
    print('Removing item from a particular index using "del list[index]"')
    del game[1]
    print(game)
    printSeparator()
    
    print('Removing item from a particular index using "del list[startIndex:endExclusiveIndex]"')
    game = [ 'Rock', 'Paper', 'Scissors', 'Lizard', 'Spock' ]
    print(f'Before: {game}')
    del game[1:3]
    print(f'After: {game}')
    printSeparator()
    
    print('Removing item from a particular index using "del list[startIndex:endExclusiveIndex:step]"')
    game = [ 'Rock', 'Paper', 'Scissors', 'Lizard', 'Spock' ]
    print(f'Before: {game}')
    del game[1:5:2]
    print(f'After: {game}')
    printSeparator()
    
    print('Joining list')
    game = [ 'Rock', 'Paper', 'Scissors', 'Lizard', 'Spock' ]
    print(', '.join(game))
    printSeparator()
    
    print('Lenght of list')
    game = [ 'Rock', 'Paper', 'Scissors', 'Lizard', 'Spock' ]
    print(f'Lenght of list: {game} = {len(game)}')
    printSeparator()
    
def print_list(o):
    for i in o: print(i, end=' ', flush=True)
    print()

if __name__ == '__main__': main()
