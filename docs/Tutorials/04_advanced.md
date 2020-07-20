---
title: Advanced Python Concepts
tags:
- advanced
- python
- concepts
- generator
- iterator
- closure
- decorators
---

# :eyes: Advanced Python Concepts

<TagLinks />

## :fire_engine: Generators

Generators are used to create iterators, but with a different approach.
Generators are simple functions which return an iterable set of items, one at a time, in a special way.

::: tip yield
Generators are always accompanied by `yield`
:::

```python
import random

def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40)

    # returns a 7th number between 1 and 15
    yield random.randint(1,15)

for random_number in lottery():
       print("And the next number is... %d!" %(random_number))
```

### :ambulance: Generator Expression

Some simple generators can be coded succinctly as expressions using a syntax similar to list comprehensions but with parentheses instead of square brackets.

```python
>>> sum(i*i for i in range(10))                 # sum of squares
285
```

## :family_man_girl_girl: Iterators

* `for` calls `iter()`, `__iter__()` which called `next()` and subsequently `__next__()`
* Writing your own iterators?

```python
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

>>> rev = Reverse('spam')
>>> iter(rev)
<__main__.Reverse object at 0x00A1DB50>
>>> for char in rev:
...     print(char)
...
m
a
p
s
```

## :diamond_shape_with_a_dot_inside: [Closure]

A [closure] is a function object that remembers values in enclosing scopes even if they are not present in memory.

::: warning Nested Functions
It's very important to note that the nested functions can access the variables of the enclosing scope.
However, at least in python, they are only readonly.
:::

## :crown: Decorators

> Preprocessing/Postprocessing the arguments/returns to decorated function

* Can add multiple decorators to a function
* Decorators in Python are used to modify or inject code in functions or classes. Using decorators, you can wrap a class or function method call so that a piece of code can be executed before or after the execution of the original code. Decorators can be used to check for permissions, modify or track the arguments passed to a method, logging the calls to a specific method, etc.

## :carousel_horse: Coroutines

Coroutines can be entered, exited, and resumed at many different points.
They can be implemented with the `async def` statement.

## :memo: Memory Management

Python does automatic memory management (reference counting for most objects and **garbage collection**
to eliminate cycles). The memory is freed shortly after the last reference to it has been eliminated.

Python memory is managed by Python **private heap space**. All Python objects and data structures are located in a private heap. The programmer does not have an access to this private heap and interpreter takes care of this Python private heap.

## :lock: GIL - Global Interpreted Lock


## :computer: [Metaprogramming]

> treat other programs as data

* [Metaclasses](https://en.wikipedia.org/wiki/Metaclass) are provided by python
  * a metaclass is a class whose instances are classes.
  * instance of a normal class is an bounded object in memory
* https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python

## :monkey_face: [Monkey Patching]

> What is monkey patching? How to use it in Python? Example? Is it ever a good idea?

Default car doesnt have a harness to carry bicycles. We monkey patch it to a car.

## :crossed_swords: Descriptors

> used to describe something

* https://docs.python.org/3/howto/descriptor.html

## :smile: Good Questions

*  Is it possible to have a producer thread reading from the network and a consumer thread writing to a file, really work in parallel? What about GIL?
   * [Why GIL still exists in CPython?](https://wiki.python.org/moin/GlobalInterpreterLock)
* Dependency
  * Functional Dependencies **FDs**
    * If ( t1(A) == t2(A)) then ( t1(B) = t2(B) )
    * duplicated are acceptable as long as the condition is satisfied
  * Direct Dependency
  * [Transitive Dependency](https://en.wikipedia.org/wiki/Transitive_dependency)
    * Third Normal Form **3NF** - Avoid transitive dependency to save space
  * Partial Dependency **2NF**
  * **1NF** remove all Multivalued (multiple phone nos) and Composite (Residence Address) date entries
    * by breaking/decomposing data into atomic values seperate tables
* What are the wheels and eggs? What is the difference?
* When to change version? Major | Minor version change
  * When not backward compatible => Major change
    * Example python 2 and python 3

## :1234: Types

[Types in > python 3.5](https://docs.python.org/3/library/typing.html)

```py
def infinite_stream(start: int) -> Generator[int, None, None]:
    while True:
        yield start
        start += 1
```


## :selfie: References

* [Parent pointer tree/ Spaghetti/cactus stack](https://en.wikipedia.org/wiki/Parent_pointer_tree)
* [Python Grammer Specification](https://docs.python.org/3/reference/grammar.html)




[closure]: https://en.wikipedia.org/wiki/Closure_(computer_programming)
[Metaprogramming]: https://en.wikipedia.org/wiki/Metaprogramming
[monkey patching]: https://en.wikipedia.org/wiki/Monkey_patch


