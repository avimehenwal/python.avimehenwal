---
title: Study material
tags:
  - python
  - resources
  - study
  - material
---

# :snake: Python study material

<TagLinks />

## :office: Official resources

- https://www.python.org/about/gettingstarted/
- https://docs.python.org/3/tutorial/index.html

## :family: Others

- https://gist.github.com/sloria/7001839
- https://github.com/willmcgugan/rich
- https://www.priceintelligently.com/
- https://www.google.com/search?q=SaaS&newwindow=1&hl=en&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjciOvMtdrpAhUcZxUIHXqyBmIQ_AUoAXoECDoQAw&biw=1294&bih=641#imgrc=Qwze79n_6S-sMM
- http://effbot.org/pyfaq/

## :woman_office_worker: Interview Prep

- https://github.com/MaximAbramchuck/awesome-interview-questions

```mermaid
stateDiagram-v2
    Still :  Still moving description
    note left of Still : This is the note to the left

    [*] --> Still
    Still --> [*]

    Still --> Moving
    Moving --> Still
    Moving --> Crash : A transition
    Crash --> [*]
```

![Python programming logo](/logo.svg)

::: theorem Principle of Science and Engineering

:cowboy_hat_face: Try to do ==good science== rather than :money_mouth_face: popular science.

Liberal Education
: Learn something about everything and everything about something.

:::

# :bug: Pythonic

- $Generators \subset Iterators$ All generators are iterators BUT not all iterators are generators
- Generators are usually attached to functions have `next()` method and `yield`
- Iterator creates a list generator generates ONE item at a time for computation
  - Iterator _advantages_ Creates item for computation one at a time and does not consumes more memory. <Badge type="tip" vertical="middle" text="Lazy Loading" />
- [Lazy Loading](https://stackoverflow.com/questions/39140348/python-lazy-loading)
- Python supports <Badge type="error" vertical="middle" text="Multiple Inheritance" />
  - Problem - cyclic dependency in case same method in both base classes

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

## :lock: GIL - Global Interpreted Lock

Python's GIL is intended to serialize access to interpreter internals from different threads. On multi-core systems, it means that multiple threads can't effectively make use of multiple cores. (If the GIL didn't lead to this problem, most people wouldn't care about the GIL - it's only being raised as an issue because of the increasing prevalence of multi-core systems.)
Note that Python's GIL is only really an issue for
<Badge type="warning" vertical="middle" text="CPython" />
, the reference implementation. Jython and IronPython don't have a GIL. As a Python developer, you don't generally come across the GIL unless you're writing a C extension. C extension writers need to release the GIL when their extensions do blocking I/O, so that other threads in the Python process get a chance to run.

## :unicorn: OOP - Object Oriented Programming

[Examples](https://github.com/CoreyMSchafer/code_snippets/tree/master/Object-Oriented)

### Python Operator Overloading

Python operators work for built-in classes. But same operator behaves differently with different types.

**For example,** the `+` operator will, perform arithmetic addition on two numbers, merge two lists and concatenate two strings. This feature in Python, that allows same operator to have different meaning according to the context is called operator overloading.

```py
class person:
    def __init__(self):
        self.__name=''
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name=value
    @name.deleter
    def name(self, value):
        print('Deleting..')
        del self.__name
```

The above person class includes two methods with the same name `name()`, but with a different number of parameters. This is called method overloading.

### Polymorphism

A common real example in Python is **file-like objects**. Besides actual files, several other types, including `StringIO` and `BytesIO`, are file-like. A method that acts as files can also act on them because they support the required methods (e.g. read, write).

### Encapsulation (Accessibility)

private attributes are defined by special syntax `self.__a` same with methods.
`def __methodName(self):`

Major Difference between Python 2 and Python 3:

1. print is now a function instead of keyword
2. xrange (iterable) is now replaced with range()
3. python 3 supports Unicode
4. `raw_input()` is replaced by `input()` method

### Python Classes and Functions

> Classes Encapsulates data and related operation functions

- New Classes and old classes. Difference ?
- Though classmethod and staticmethod are quite similar, there's a slight difference in usage for both entities: classmethod must have a reference to a class object as the first parameter, whereas staticmethod can have no parameters at all.
- Classmethods leads to **Factory Design pattern** in python
- Instance attributes/variables and class attributes

### Python @staticmethod

Static methods are a special case of methods. Sometimes, you'll write code that belongs to a class, but that doesn't use the object itself at all. For example:

> Used when `self` is not used in the class. There is no point in adding self to a method signature of its not being used. Declare your method static and it uses less memory if many classes instantiated.

```python
class Pizza(object):
    @staticmethod
    def mix_ingredients(x, y):
        return x + y

    def cook(self):
        return self.mix_ingredients(self.cheese, self.vegetables)
```

In such a case, writing mix_ingredients as a non-static method would work too, but it would provide it a self argument that would not be used. Here, the decorator @staticmethod buys us several things:

::: tip @staticmethod
Python doesn't have to instantiate a bound-method for each Pizza object we instantiate.
Bound methods are objects too, and creating them has a cost. Having a static method avoids that:
:::

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

### Python @classmethods

> Methods which accepts class as 1st positional argument

Having said that, what are class methods? Class methods are methods that are not bound to an object, but to… a class!

- Used to alter class attributes
- ==used as alternatives constructors?== What does it mean?
- parse the input before calling and returning the constructors

```python
>>> class Pizza(object):
...     radius = 42
...     @classmethod
...     def get_radius(cls):
...         return cls.radius
...
>>>
>>> Pizza.get_radius
<bound method type.get_radius of <class '__main__.Pizza'>>
>>> Pizza().get_radius
<bound method type.get_radius of <class '__main__.Pizza'>>
>>> Pizza.get_radius is Pizza().get_radius
True
>>> Pizza.get_radius()
42
```

Whatever the way you use to access this method, it will be always bound to the class it is attached too, and its first argument will be the class itself (remember that classes are objects too).
When to use this kind of methods? Well class methods are mostly useful for two types of methods:
Factory methods, that are used to create an instance for a class using for example some sort of pre-processing. If we use a @staticmethod instead, we would have to hardcode the Pizza class name in our function, making any class inheriting from Pizza unable to use our factory for its own use.

```python
class Pizza(object):
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def from_fridge(cls, fridge):
        return cls(fridge.get_cheese() + fridge.get_vegetables())
```

Static methods calling static methods: if you split a static methods in several static methods, you shouldn't hard-code the class name but use class methods. Using this way to declare our method, the Pizza name is never directly referenced and inheritance and method overriding will work flawlessly

```python
class Pizza(object):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    @staticmethod
    def compute_area(radius):
         return math.pi * (radius ** 2)

    @classmethod
    def compute_volume(cls, height, radius):
         return height * cls.compute_area(radius)

    def get_volume(self):
        return self.compute_volume(self.height, self.radius)
```

### Abstract methods

An abstract method is a method defined in a base class, but that **may not provide any implementation**. In Java, it would describe the methods of an interface.
So the simplest way to write an abstract method in Python is:

```python
class Pizza(object):
    def get_radius(self):
        raise NotImplementedError
```

Any class inheriting from Pizza should implement and override the get_radius method, otherwise an exception would be raised.
This particular way of implementing abstract method has a drawback. If you write a class that inherits from Pizza and forget to implement get_radius, the error will only be raised when you'll try to use that method.

```python
>>> Pizza()
<__main__.Pizza object at 0x7fb747353d90>
>>> Pizza().get_radius()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in get_radius
NotImplementedError
```

There's a way to triggers this way earlier, when the object is being instantiated, using the abc module that's provided with Python.

```python
import abc

class BasePizza(object):
    __metaclass__  = abc.ABCMeta

    @abc.abstractmethod
    def get_radius(self):
         """Method that should do something."""
```

Using abc and its special class, as soon as you'll try to instantiate BasePizza or any class inheriting from it, you'll get a TypeError.

```python
>>> BasePizza()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't instantiate abstract class BasePizza with abstract methods get_radius
```

### Mixing static, class and abstract methods

When building classes and inheritances, the time will come where you will have to mix all these methods decorators. So here's some tips about it.
Keep in mind that declaring a method as being abstract, doesn't freeze the prototype of that method. That means that it must be implemented, but i can be implemented with any argument list.

```python
import abc

class BasePizza(object):
    __metaclass__  = abc.ABCMeta

    @abc.abstractmethod
    def get_ingredients(self):
         """Returns the ingredient list."""

class Calzone(BasePizza):
    def get_ingredients(self, with_egg=False):
        egg = Egg() if with_egg else None
        return self.ingredients + egg
```

This is valid, since Calzone fulfil the interface requirement we defined for BasePizza objects. That means that we could also implement it as being a class or a static method, for example:

```python
import abc

class BasePizza(object):
    __metaclass__  = abc.ABCMeta

    @abc.abstractmethod
    def get_ingredients(self):
         """Returns the ingredient list."""

class DietPizza(BasePizza):
    @staticmethod
    def get_ingredients():
        return None
```

This is also correct and fulfill the contract we have with our abstract BasePizza class. The fact that the get_ingredients method don't need to know about the object to return result is an implementation detail, not a criteria to have our contract fulfilled.

Therefore, you can't force an implementation of your abstract method to be a regular, class or static method, and arguably you shouldn't. Starting with Python 3 (this won't work as you would expect in Python 2, see issue5867), it's now possible to use the @staticmethod and `@classmethod` decorators on top of @abstractmethod:

```python
import abc

class BasePizza(object):
    __metaclass__  = abc.ABCMeta

    ingredient = ['cheese']

    @classmethod
    @abc.abstractmethod
    def get_ingredients(cls):
         """Returns the ingredient list."""
         return cls.ingredients
```

Don't misread this: if you think this going to force your subclasses to implement get_ingredients as a class method, you are wrong. This simply implies that your implementation of get_ingredients in the BasePizza class is a class method.

An implementation in an abstract method? Yes! In Python, contrary to methods in Java interfaces, you can have code in your abstract methods and call it via `super()`:

```python
import abc

class BasePizza(object):
    __metaclass__  = abc.ABCMeta

    default_ingredients = ['cheese']

    @classmethod
    @abc.abstractmethod
    def get_ingredients(cls):
         """Returns the ingredient list."""
         return cls.default_ingredients

class DietPizza(BasePizza):
    def get_ingredients(self):
        return ['egg'] + super(DietPizza, self).get_ingredients()
```

In such a case, every pizza you will build by inheriting from BasePizza will have to override the get_ingredients method, but will be able to use the default mechanism to get the ingredient list by using super().

<Footer />

#### :v: Get in touch with me

> I am looking for Jobs ... :sunglasses:

- [Github](https://github.com/avimehenwal/)
- [My Website](https://avimehenwal.in)
- [My Blog v2](https://avimehenwal2.netlify.app/)
- [Twitter Handle](https://twitter.com/avimehenwal)
- [LinkedIn](https://in.linkedin.com/in/avimehenwal)
- [Stackoverflow](https://stackoverflow.com/users/1915935/avi-mehenwal)

<a href="https://www.buymeacoffee.com/F1j07cV" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" style="height: 51px !important;width: 217px !important;" ></a>

Spread Love :hearts: and not :no_entry_sign: hatred [![Twitter Follow](https://img.shields.io/twitter/follow/avimehenwal.svg?style=social)](https://twitter.com/avimehenwal)
