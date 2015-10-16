#!/usr/bin/env python

# DATE      :   24-Feb-2015
# AUTHOR    :   avimehenwal
# PURPOSE   :   Difference between __init__ and __call__ method python

"""
__init__ would be treated as Constructor where as __call__ methods can be called with objects any number of times.
Both __init__ and __call__ functions do take default arguments.
"""

class A:
    """
    Python bound and UnBound methods
    >>> Pizza()
    init
    <__main__.Pizza object at 0x1055cc518>
    >>> Pizza
    <class '__main__.Pizza'>
    >>> Pizza().get_a
    init
    <bound method Pizza.get_a of <__main__.Pizza object at 0x1055cc080>>
    >>> Pizza().get_a()
    init
    get_a
    >>> Pizza.get_a
    <function Pizza.get_a at 0x1055c7488>
    >>> Pizza.get_a()
    Traceback (most recent call last):
      File "<pyshell#265>", line 1, in <module>
        Pizza.get_a()
    TypeError: get_a() missing 1 required positional argument: 'self'
    >>> Pizza.get_a(Pizza)
    get_a
    >>> 
    """

    def __init__(self):
        print("init")

    def __call__(self):
        print("call")
    
    def get_method(self):
        print("get_method")


if __name__ == '__main__':
    print("A()\t", A())
    print("A()()\t", A()())
    print("A\t", A)
    print("A().get_method\t", A().get_method)
    print("A().get_method()\t", A().get_method())
    print("A.get_method(A)\t", A.get_method(A))
    print("A.get_method()\t", A.get_method())


