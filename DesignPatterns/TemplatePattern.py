#!/usr/bin/env python

__author__ = 'avimehenwal'
__date__ = '12-March-2015'
__purpose__ = 'Template Design Pattern'


"""
1. In software engineering, the template method pattern is a behavioral design pattern that defines the program skeleton of an algorithm in a method, called template method, which defers some steps to subclasses.[1] It lets one redefine certain steps of an algorithm without changing the algorithm's structure.

2.In the template method of this design pattern, one or more algorithm steps can be overridden by subclasses to allow differing behaviors while ensuring that the overarching algorithm is still followed.

3. code refactoring using the Template pattern with the BFS and DFS algorithms.
"""

from cowpy import cow

def dots_style(msg):
    msg = msg.capitalize()
    msg = '.' * 10 + msg + '.' * 10
    return msg

def admire_style(msg):
    msg = msg.upper()
    return '!'.join(msg)

def cow_style(msg):


    msg = cow.milk_random_cow(msg)
    return msg

def generate_banner(msg, style=dots_style):
    print('-- start of banner --')
    print(style(msg))
    print('-- end of banner --\n\n')

def main():
    msg = 'happy coding'
    [generate_banner(msg, style) for style in (dots_style, admire_style, cow_style)]

if __name__ == '__main__':
    main()

-----------------------------------------------------------------------------------------

class AbstractBase(object):
    """ Organising methods, doesnt know what they do """
    def orgMethod(self):
        # Calling the methods in a structured/logical way
        self.doThis()
        self.doThat()

class Concrete(AbstractBase):
    """ Only implements. Execution flow comes from AbstractBase """
    # Hook Methods
    def doThis(self): ...
    def doThat(self): ...
