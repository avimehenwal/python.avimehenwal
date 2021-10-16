---
title: Polymorphism
tags:
  - polymorphism
  - oop
---

# Polymorphism

<TagLinks />

deeply connected with [Type Systems](https://en.wikipedia.org/wiki/Type_system)

Duck Typing is also a form of Polymorphism

## Types

1. Ad-hoc Polymorphism
2. Parametric Polymorphism
3. Subtyping Polymorphism, Context Based Polymorphism

## Polymorphism in Python

[Theorytical vs pythonic polymorphism?](https://softwareengineering.stackexchange.com/questions/335704/how-many-types-of-polymorphism-are-there-in-the-python-language)

### Built-in methods

```py
# len() being used for a string
print(len("geeks"))

# len() being used for a list
print(len([10, 20, 30]))
```

### Polymorphism with class methods

Multiple classes with same method signatures.

### Polymorphism with Inheritance

```py
class Animal:
  def type(self):
    print("Various types of animals")

  def age(self):
    print("Age of the animal.")

class Rabbit(Animal):
  def age(self):
    print("Age of rabbit.")

class Horse(Animal):
  def age(self):
    print("Age of horse.")
```

### Monomorphic

The `typeclass` decorator will add an `instance` attribute to the method. Use that to decorate monomorphic implementations, giving it the type argument:

```py
T = typing.TypeVar('T')
@typeclass(T)
def to_json(value: T) -> str:
    """Serialize a value to JSON."""

@to_json.instance(str)
def _to_json_str(s):
    return f'"{s}"'

@to_json.instance(int)
@to_json.instance(float)
def _to_json_number(n):
    return str(n)

@to_json.instance(typing.Iterable, protocol=True)
def _to_json_iterable(xs):
   return '[' + ','.join(to_json(x) for x in xs) + ']'

@to_json.instance(Person)
def _to_json_person(person):
    return f'{{"name":{to_json(person.name)}}}'

# usage API
to_json([Person(name='John')])
```

## Static Dispatch

- @compile-time
- compiler polymorphically decide which implementaion to execute?

> Python is **dynamically typed** language, hence it does not have Functional Overloading

- **CPython** is Single Dispatched language by default. Does not support dynamic dispatch (@runtime)

## Questions

- [Why python doesn't support functional overloading?](https://stackoverflow.com/questions/6434482/python-function-overloading)

## References

- [Typings in python](https://www.python.org/dev/peps/pep-0484/)

<Footer />
