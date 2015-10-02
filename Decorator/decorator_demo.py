#!/usr/env python

"""      
new_f() is defined within the body of entry_exit(),
so it is created and returned when entry_exit() is called.
Note that new_f() is a closure, because it captures the actual value of f.
Notice that __init__() is the only method called to perform decoration, and __call__() is called every time you call the decorated sayHello()
http://python-3-patterns-idioms-test.readthedocs.org/en/latest/PythonDecorators.html
"""

class myDecorator(object):

    def __init__(self, fn):
        self.fn = fn        
        print("inside myDecorator.__init__()")

    def __call__(self):
        print("inside myDecorator.__call__()")
        self.fn()
        print("Exited", self.fn.__name__)
        

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
print(func1.__name__, "\n")


@myDecorator
def function1():
    print("inside function_1")
    
@myDecorator
def function2():
    print("inside function_2")


if __name__ == '__main__':
    function1()
    function2()
    print("Finished processing")
