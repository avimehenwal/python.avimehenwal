#!/usr/bin/env python

# DATE      :   24-Feb-2015
# AUTHOR    :   avimehenwal
# PURPOSE   :   Difference between __init__ and __call__ method python

"""
__init__ would be treated as Constructor where as __call__ methods can be called with objects any number of times. Both __init__ and __call__ functions do take default arguments.
"""

class A:
    def __init__(self):
        print("init")

    def __call__(self):
        print("call")

if __name__ == '__main__':
    A()
    A()()
