---
title: Rudimentary Python
tags:
- Strings
- manupulation
- substitution
- formatting
- fundamentals
- comprehension
---

# 1. Strings

<TagLinks />

> batteries included” philosophy

* zen of python

## 1.1. General

* immutable basic types (numbers, strings, tuples)
* mutable objects such as lists, dictionaries, and most other types)


## 1.2. String Formatting

1. using C-style string formatting using `%`, old-style
2. using Python `.format()`, new-style

## 1.3. String Manipulation

Since strings are stored as an array of type `char` in memory, these could be manupulated using **list comprehensions**

List comprehensions
: which creates a new list based on another list, in a single, readable line.

## 1.4. Manupulation Techniques

* Type checking using `is` or `instance` keyword
* pickeling and [serialization]/Jsonify of string types

## 1.5. Classes

* old-style Classes
* new-style classes

::: tip Aliasing
Objects have individuality, and multiple names (in multiple scopes) can be bound
to the same object. This is known as aliasing in other languages.
:::

* scopes and Namespaces

Namespace created by interpreter
: is a mapping from names to objects. Most namespaces are currently implemented as Python dictionaries, but that’s normally not noticeable in any way (except for performance), and it may change in the future.

* global namespace at startup
* local namespace when function is called, deleted, exception, modified etc.

Scope
: is a textual region of a Python program where a namespace is directly accessible. “Directly accessible”

* When a class definition is entered, a new namespace is created, and used as the local scope — thus, all assignments to local variables go into this new namespace. In particular, function definitions bind the name of the new function here.
* Class objects support two kinds of operations
  * Attribute references and
  * Instantiation
* class Attributes
  * shared between all instances
  * local instances Attributes
* class Methods
  * python functions bounded to classname
* Python support **Multiple Inheritance**
  * MRO - Method Resolution Order
  * [Diamond Relationship Problem](https://en.wikipedia.org/wiki/Multiple_inheritance#The_diamond_problem)
* “Private” instance variables that cannot be accessed except from inside an object don’t exist in Python.


### 1.5.1. References

* https://pyformat.info/


[serialization]: https://en.wikipedia.org/wiki/Serialization


<Footer />
