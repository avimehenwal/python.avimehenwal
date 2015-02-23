#!/usr/bin/env python

__author__ = 'avimehenwal'
__date__ = '20-Feb-2015'
__purpose__ = 'Decorator Design Pattern'

"""
1. Whenever we want to add extra functionality to an object, we have a number of different options. We can:
    (a) Add the functionality directly to the class the object belongs to, if it makes sense (for example, add a new method)
    (b) Use composition
    (c) Use inheritance
Composition should generally be preferred over inheritance, because inheritance makes code reuse harder, it's static, and applies to an entire class and all instances of it [GOF95, page 31], [j.mp/decopat].

2. Python that is used for extending the behavior of a class, method, or function without using inheritance. In terms of implementation, a Python decorator is a callable (function, method, class) that accepts a function object fin as input, and returns another function object fout [j.mp/conqdec]. This means that any callable that has these properties can be treated as a decorator.

3. There is no one-to-one relationship between the Decorator pattern and Python decorators. also known as Wrapper, an alternative naming shared with the Adapter pattern) is a design pattern that allows behavior to be added to an individual object, either statically or dynamically, without affecting the behavior of other objects from the same class

4. The Decorator pattern is generally used for extending the functionality of an object. Real examples of such extensions are: adding a silencer to a gun, using different camera lenses (in cameras with removable lenses), and so on.

5. The Decorator pattern shines when used for implementing cross-cutting concerns [Lott14, page 223], [j.mp/wikicrosscut]. Examples of cross-cutting concerns are:
    Data validation
    Transaction processing (A transaction in this case is similar to a database transaction, in the sense that either all steps should be completed successfully, or the transaction should fail.)
    Caching
    Logging
    Monitoring
    Debugging
    Business rules
    Compression
    Encryption
Another popular example of using the Decorator pattern is Graphical User Interface (GUI) toolkits. In a GUI toolkit, we want to be able to add features such as borders, shadows, colors, and scrolling to individual components/widgets

http://python-3-patterns-idioms-test.readthedocs.org/en/latest/PythonDecorators.html

"""

# Using Class as Decorator

# PythonDecorators/entry_exit_class.py
class entry_exit(object):

    def __init__(self, f):
        self.f = f

    def __call__(self):
        print("Entering", self.f.__name__)
        self.f()
        print("Exited", self.f.__name__)

@entry_exit
def func1():
    print("inside func1()")

@entry_exit
def func2():
    print("inside func2()")

##################################################################################

# Using function as a decorator

# PythonDecorators/entry_exit_function.py
def entry_exit(f):
    def new_f():
        print("Entering", f.__name__)
        f()
        print("Exited", f.__name__)
    return new_f

@entry_exit
def func1():
    print("inside func1()")

@entry_exit
def func2():
    print("inside func2()")

func1()
func2()
print(func1.__name__)

"""
Decorators with Arguments
The decorator mechanism behaves quite differently when you pass arguments to the decorator.
"""

# PythonDecorators/decorator_with_arguments.py
class decorator_with_arguments(object):

    def __init__(self, arg1, arg2, arg3):
        """
        If there are decorator arguments, the function
        to be decorated is not passed to the constructor!
        """
        print("Inside __init__()")
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

    def __call__(self, f):
        """
        If there are decorator arguments, __call__() is only called
        once, as part of the decoration process! You can only give
        it a single argument, which is the function object.
        """
        print("Inside __call__()")
        def wrapped_f(*args):
            print("Inside wrapped_f()")
            print("Decorator arguments:", self.arg1, self.arg2, self.arg3)
            f(*args)
            print("After f(*args)")
        return wrapped_f

@decorator_with_arguments("hello", "world", 42)
def sayHello(a1, a2, a3, a4):
    print('sayHello arguments:', a1, a2, a3, a4)

print("After decoration")

print("Preparing to call sayHello()")
sayHello("say", "hello", "argument", "list")
print("after first sayHello() call")
sayHello("a", "different", "set of", "arguments")
print("after second sayHello() call")

"""
Review: Decorators without Arguments
If we create a decorator without arguments, the function to be decorated is passed to the constructor, and the __call__() method is called whenever the decorated function is invoked:
"""

# PythonDecorators/decorator_without_arguments.py
class decorator_without_arguments(object):

    def __init__(self, f):
        """
        If there are no decorator arguments, the function
        to be decorated is passed to the constructor.
        """
        print("Inside __init__()")
        self.f = f

    def __call__(self, *args):
        """
        The __call__ method is not called until the
        decorated function is called.
        """
        print("Inside __call__()")
        self.f(*args)
        print("After self.f(*args)")

@decorator_without_arguments
def sayHello(a1, a2, a3, a4):
    print('sayHello arguments:', a1, a2, a3, a4)

print("After decoration")

print("Preparing to call sayHello()")
sayHello("say", "hello", "argument", "list")
print("After first sayHello() call")
sayHello("a", "different", "set of", "arguments")
print("After second sayHello() call")