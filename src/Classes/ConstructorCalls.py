#!/usr/bin/env python

__author__ = 'avimehenwal'
__date__ = '20-Feb-2015'
__purpose__ = 'Python Class and contructor initialization'


class Bar: pass

class Foo(object):
    """ Global Class Attributes
    Visible and accessable to all class and its attributes.
    Any change in these is made throughout all instances
    """
    x = "a"

    def __init__(self):
        y = "p"         # Local Variable : not accessable to instances
        self.z = "z"    # Class attribute : available to class instances
        print("{} y={}".format(__name__, y))


if __name__ == '__main__' :

    print(Foo.x)
    f = Foo()
    print(f.x)
    f2 = Foo()
    print(f2.x)
    f2.x = 'b'
    print(f.x)
    Foo.x = 'c'
    print(f.x)
    print(f2.x)
    Foo.x = 'd'
    print(f2.x)
    print(f.x)
    f3 = Foo()
    print(f3.x)
    Foo.x = 'e'
    print(f3.x)
    print(f2.x)
