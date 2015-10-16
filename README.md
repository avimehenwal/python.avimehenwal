## Pythonic

- All generators are iterators BUT not all iterators are generators
- Generators are usually attached to functions have next() method and yield
- Iterator creates a list generator generates ONE item at a time for computation
- Python supports MULTIPLE INHERITANCE

*ADANTAGES*
Creates item for computation one at a time and does not consumes more memory.

**GIL**
Python's GIL is intended to serialize access to interpreter internals from different threads. On multi-core systems, it means that multiple threads can't effectively make use of multiple cores. (If the GIL didn't lead to this problem, most people wouldn't care about the GIL - it's only being raised as an issue because of the increasing prevalence of multi-core systems.) 
Note that Python's GIL is only really an issue for CPython, the reference implementation. Jython and IronPython don't have a GIL. As a Python developer, you don't generally come across the GIL unless you're writing a C extension. C extension writers need to release the GIL when their extensions do blocking I/O, so that other threads in the Python process get a chance to run.


```python
class Base1:
    pass

class Base2:
    pass

class MultiDerived(Base1, Base2):
    pass

class Base:
    pass

class Derived1(Base):
    pass

class Derived2(Derived1):
    pass
```

**Python Operator Overloading**
Python operators work for built-in classes. But same operator behaves differently with different types. For example, the + operator will, perform arithmetic addition on two numbers, merge two lists and concatenate two strings. This feature in Python, that allows same operator to have different meaning according to the context is called operator overloading.

**POLYMORPHISM WITH PYTHON**
A common real example in Python is file-like objects. Besides actual files, several other types, including StringIO and BytesIO, are file-like. A method that acts as files can also act on them because they support the required methods (e.g. read, write).

**ENCAPSULATION (Accessability)**
private attributes are defined by special syntax self.__a same with methods.
def __methodName(self):

Major Difference between Python 2 and Python 3:
1. print is now a function instead of keyword
2. xrange (iterable) is now replaced with range()
3. python 3 supports Unicode
4. raw_input() is replaced by input() method

#### Python @staticmethod and @classmethod
Static methods are a special case of methods. Sometimes, you'll write code that belongs to a class, but that doesn't use the object itself at all. For example:

```python
class Pizza(object):
    @staticmethod
    def mix_ingredients(x, y):
        return x + y
 
    def cook(self):
        return self.mix_ingredients(self.cheese, self.vegetables)
```

In such a case, writing mix_ingredients as a non-static method would work too, but it would provide it a self argument that would not be used. Here, the decorator @staticmethod buys us several things:

Python doesn't have to instantiate a bound-method for each Pizza object we instiantiate. Bound methods are objects too, and creating them has a cost. Having a static method avoids that:

```python
>>> Pizza().cook is Pizza().cook
False
>>> Pizza().mix_ingredients is Pizza.mix_ingredients
True
>>> Pizza().mix_ingredients is Pizza().mix_ingredients
True
```

It eases the readability of the code: seeing @staticmethod, we know that the method does not depend on the state of object itself;
It allows us to override the mix_ingredients method in a subclass. If we used a function mix_ingredients defined at the top-level of our module, a class inheriting from Pizza wouldn't be able to change the way we mix ingredients for our pizza without overriding cook itself.
