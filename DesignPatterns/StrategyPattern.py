#!/usr/bin/env python

__author__ = 'avimehenwal'
__date__ = '11-March-2015'
__purpose__ = 'Strategy Design Pattern'


"""
1. In computer programming, the strategy pattern (also known as the policy pattern) is a software design pattern that enables an algorithm's behavior to be selected at runtime. The strategy pattern
defines a family of algorithms,
encapsulates each algorithm, and
makes the algorithms interchangeable within that family.
Strategy lets the algorithm vary independently from clients that use it.[1] Strategy is one of the patterns included in the influential book Design Patterns by Gamma et al. that popularized the concept of using patterns in software design.

2. Selecting best mode of transport (car, bus, taxi) to destination based on criteria like time and price and comfort.

3. Strategy is generally used when we want to be able to use multiple solutions for the same problem transparently
"""

import pprint
from collections import namedtuple
from operator import attrgetter

if __name__ == '__main__':
    ProgrammingLang = namedtuple('ProgrammingLang', 'name ranking')

    stats = ( ('Ruby', 14), ('Javascript', 8), ('Python', 7),
                   ('Scala', 31), ('Swift', 18), ('Lisp', 23) )

    lang_stats = [ProgrammingLang(n, r) for n, r in stats]
    pp = pprint.PrettyPrinter(indent=5)
    pp.pprint(sorted(lang_stats, key=attrgetter('name')))
    print()
    pp.pprint(sorted(lang_stats, key=attrgetter('ranking')))


##############################################################################

import time

SLOW = 3                        # in seconds
LIMIT = 5                         # in characters
WARNING = 'too bad, you picked the slow algorithm :('

def pairs(seq):
    n = len(seq)
    for i in range(n):
        yield seq[i], seq[(i + 1) % n]

def allUniqueSort(s):
   if len(s) > LIMIT:
       print(WARNING)
       time.sleep(SLOW)
   srtStr = sorted(s)
   for (c1, c2) in pairs(srtStr):
       if c1 == c2:
           return False
   return True

def allUniqueSet(s):
    if len(s) < LIMIT:
        print(WARNING)
        time.sleep(SLOW)





    return True if len(set(s)) == len(s) else False

def allUnique(s, strategy):
    return strategy(s)

def main():
    while True:
        word = None
        while not word:
            word = input('Insert word (type quit to exit)> ')

            if word == 'quit':
                print('bye')
                return

            strategy_picked = None
            strategies = { '1': allUniqueSet, '2': allUniqueSort }
            while strategy_picked not in strategies.keys():
                strategy_picked = input('Choose strategy: [1] Use a set, [2] Sort and pair> ')

                try:
                    strategy = strategies[strategy_picked]
                    print('allUnique({}): {}'.format(word, allUnique(word, strategy)))
                except KeyError as err:
                    print('Incorrect option: {}'.format(strategy_picked))
            print()

if __name__ == '__main__':
    main()