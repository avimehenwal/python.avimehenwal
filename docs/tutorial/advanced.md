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

# 1. Advanced Python Concepts

<TagLinks />

## 1.1. Generators

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

### 1.1.1. Generator Expression

```python
>>> sum(i*i for i in range(10))                 # sum of squares
285
```

## 1.2. Iterators

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

## 1.3. [Closure]

A [closure] is a function object that remembers values in enclosing scopes even if they are not present in memory.

::: warning Nested Functions
It's very important to note that the nested functions can access the variables of the enclosing scope.
However, at least in python, they are only readonly.
:::

## 1.4. Decorators

> Preprocessing the arguments to decorated function

* Can add multiple decorators to a function

## 1.5. Coroutines

Coroutines can be entered, exited, and resumed at many different points.
They can be implemented with the `async def` statement.

## 1.6. Memory Management

Python does automatic memory management (reference counting for most objects and **garbage collection**
to eliminate cycles). The memory is freed shortly after the last reference to it has been eliminated.

## 1.7. GIL - Global Interpreted Lock

### 1.7.1. References

* [Parent pointer tree/ Spaghetti/cactus stack](https://en.wikipedia.org/wiki/Parent_pointer_tree)
* [Python Grammer Specification](https://docs.python.org/3/reference/grammar.html)




[closure]: https://en.wikipedia.org/wiki/Closure_(computer_programming)


<Footer />
