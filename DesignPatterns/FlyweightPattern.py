#!/usr/bin/env python

__author__ = 'avimehenwal'
__date__ = '23-Feb-2015'
__purpose__ = 'Flyweight Design Pattern'

"""
1. The Flyweight design pattern is a technique used to minimize memory usage and improve performance by introducing data sharing between similar objects

2. A Flyweight is a shared object that contains state-independent, immutable (also known as intrinsic) data. The state-dependent, mutable (also known as extrinsic) data should not be part of Flyweight because this is information that cannot be shared since it differs per object. If Flyweight needs extrinsic data, they should be provided explicitly by the client code.

3. n Counter-Strike, for instance, all soldiers of the same team (counter-terrorists versus terrorists) look the same (representation). In the same game, all soldiers (of both teams) have some common actions, such as jump, duck, and so forth (behavior). This means that we can create a Flyweight that will contain all the common data. Of course, the soldiers also have many mutable data that are different per soldier and will not be a part of the Flyweight, such as weapons, health, locations, and so on.

4. (think of embedded systems) and systems that focus on performance, such as graphics software and electronic games. The Exaile music player for GTK+ uses Flyweight to avoid object duplication, and the Peppy text editor uses it to share the properties of the status bar.

5. and it is common practice to hold them in external data structures and pass them to the flyweight objects temporarily when they are used.

6. String interning and String interning Pool.
    hash consing is a technique used to share values that are structurally equal
"""

import random
from enum import Enum

TreeType = Enum('TreeType', 'apple_tree cherry_tree peach_tree')

class Tree:
    pool = dict()

    def __new__(cls, tree_type):
        obj = cls.pool.get(tree_type, None)
        if not obj:
            obj = object.__new__(cls)
            cls.pool[tree_type] = obj
            obj.tree_type = tree_type
        return obj

    def render(self, age, x, y):
        print('render a tree of type {} and age {} at ({}, {})'.format(self.tree_type, age, x, y))


def main():
    rnd = random.Random()
    age_min, age_max = 1, 30    # in years
    min_point, max_point = 0, 100
    tree_counter = 0

    for _ in range(10):
        t1 = Tree(TreeType.apple_tree)
        t1.render(rnd.randint(age_min, age_max),
                  rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point))
        tree_counter += 1

    for _ in range(3):
        t2 = Tree(TreeType.cherry_tree)
        t2.render(rnd.randint(age_min, age_max),
                  rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point))
        tree_counter += 1

    for _ in range(5):
        t3 = Tree(TreeType.peach_tree)
        t3.render(rnd.randint(age_min, age_max),
                  rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point))
        tree_counter += 1

    print('trees rendered: {}'.format(tree_counter))
    print('trees actually created: {}'.format(len(Tree.pool)))

    t4 = Tree(TreeType.cherry_tree)
    t5 = Tree(TreeType.cherry_tree)
    t6 = Tree(TreeType.apple_tree)
    print('{} == {}? {}'.format(id(t4), id(t5), id(t4) == id(t5)))
    print('{} == {}? {}'.format(id(t5), id(t6), id(t5) == id(t6)))


if __name__ == '__main__':
    main()

#################################################################################################
# Gang Of Four GoF implementation
# http://yloiseau.net/articles/DesignPatterns/flyweight/

class Spam(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

class SpamFactory(object):
    def  __init__(self):
        self.__instances = dict()

    def get_instance(self, a, b):
        if (a, b) not in self.__instances:
            self.__instances[(a, b)] = Spam(a, b)
        return self.__instances[(a, b)]


class Egg(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class EggFactory(object):
    def __init__(self):
        self.__instances = dict()

    def get_instance(self, x, y):
        if (x, y) not in self.__instances:
            self.__instances[(x, y)] = Egg(x, y)
        return self.__instances[(x, y)]

#----------------------------------------------------------

spamFactory = SpamFactory()
eggFactory = EggFactory()

assert spamFactory.get_instance(1, 2) is spamFactory.get_instance(1, 2)
assert eggFactory.get_instance('a', 'b') is eggFactory.get_instance('a', 'b')
assert spamFactory.get_instance(1, 2) is not eggFactory.get_instance(1, 2)
