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

# :snake: Python Rudiments

<TagLinks />

> batteries included philosophy

Python Enhancement Proposal - [PEP]
:   This is how python language is evolved since 1990.

    Python's development is conducted largely through the Python Enhancement Proposal ([PEP])
    process, the primary mechanism for proposing major new features, collecting community
    input on issues and documenting Python design decisions

[PEP]: https://www.python.org/dev/peps/

## :shield: General

* **immutable** basic types (numbers, strings, tuples), are also Primitive types generally
* **mutable** objects such as lists, dictionaries, and most other types, are generally derieved types
* python [REPL](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop) interpreter
* callable means which can be called using <Badge type="error" vertical="middle" text="special method" /> `__call__()`
* [Mixin](https://en.wikipedia.org/wiki/Mixin)
  * **included** rather than being **inherited**
  * vue mixins
* <Badge type="warning" vertical="middle" text="Dunder" /> (as in double underscore) /Magic/Special methods in Python
  * double underscore methods
* [How are dict implemented in python?](http://effbot.org/pyfaq/how-are-dictionaries-implemented.htm)
* Arguments vs Parameters
  * [call by assignment](https://docs.python.org/3/faq/programming.html#how-do-i-write-a-function-with-output-parameters-call-by-reference)
  * call by references, howto in python?
  * call by value
* Python reads program text as [Unicode code points](https://en.wikipedia.org/wiki/UTF-8)

::: tip Python Argument(s) Unpacking
Although, there is no formal rule on calling them `*args/**kwargs`,
people tend to name them that way. When a function is declared `def my_func(*args, **kwargs)`,
args is a **tuple** with all <Badge type="tip" vertical="middle" text="positional arguments" /> passed to the function and kwargs is a
with all <Badge type="warning" vertical="middle" text="keyword arguments" />. They can be named anything as long as the <Badge type="error" vertical="middle" text="unpack operators" /> `*` and `**` are used.
So `*` unpacks a tuple and `**` unpacks a dict.
:::

Pickeling/Unpickeling | Marshalling/Unmarshalling | Serialised/Unserialized | jsonify
:   Pickling is converting an object to a string representation in python.
    Generally used for caching and transferring objects between hosts/processes.

    ```mermaid
    graph LR
      A(Object form):::yellow
      B(String form):::blue
      A -- Pickeling --> B
      B -- Unpickeling --> A
      classDef yellow fill:#FFE873,stroke-width:0px;
      classDef blue fill:#b8d4ff,stroke-width:0px;
    ```

Lambda Function
:   Lambda in Python is an anonymous function created at runtime.
    <Badge type="tip" vertical="middle" text="E.g." />

    ```py
    x = lambda a, b : a * b
    print(x(5, 6))
    ```

Introspection
:   is the ability to examine an object at runtime.

    Python has a `dir()` function that
    supports examining the attributes of an object, `type()` to check the object type,
    `isinstance()`, etc. While introspection is passive examination of the objects,

    [reflection](https://www.geeksforgeeks.org/reflection-in-python/)
    is a more powerful tool where we could modify objects at runtime and
    access them dynamically. <Badge type="tip" vertical="middle" text="E.g." />
    `setattr()` adds or modifies an object's attribute;
    `getattr()` gets the value of an attribute of an object.
    It can even invoke functions dynamically - `getattr(my_obj, "my_func_name")()`


## :flags: Data Types

> Deals with memory-space management and how garbage collection will work

[Python Data Model](https://docs.python.org/3/reference/datamodel.html)

```mermaid
graph LR
PT[int, string, float, boolean, byte, file]:::yellow
CT[set, dictionary, array, tuple]:::blue
LT[class, object]:::green

subgraph Language Data Types
  LT
  subgraph Composite Data Type
    CT
    subgraph Primitive Data Type
      PT
    end
  end
end

classDef green fill:#1f9,stroke-width:0px;
classDef yellow fill:#FFE873,stroke-width:0px;
classDef blue fill:#b8d4ff,stroke-width:0px;

click PT "https://docs.python.org/3/reference/datamodel.html" "Python Data Model"
click CT "https://docs.python.org/3/reference/datamodel.html" "Python Data Model"
click LT "https://docs.python.org/3/reference/datamodel.html" "Python Data Model"
```

Python Primitive Data Types
:   Basic Building blocks

    A <Badge type="tip" vertical="middle" text="Byte" /> object is an ==immutable array==

    * The items are **8-bit** bytes, represented by integers in the range $0 <= x < 256$
    * Bytes literals (like `b'abc'`) and the built-in `bytes()` constructor can be used to create bytes objects.
    * Also, bytes objects can be decoded to strings via the `decode()` method.

Python compound / [composite] Data Structures
:   built using primitive data types for ease of use in programming

    Arrays | Lists | Tuples | Dictionary | Sets | <Badge type="tip" vertical="middle" text="File" />

    `open()`, `readline()`, `close()`, `read()`, `write()`

Lists - [Linked](https://realpython.com/linked-lists-python/) Lists
:   Akin to arrays in other languages

    * [composite] / compund data structure
      * built using primitive data types
    * Slicing operations
    * Indexed
    * List Manipulation
    * List Comprehensions

Shallow Copy
:   [shallow copy](https://en.wikipedia.org/wiki/Object_copying) of the list. Equivalent to `a[:]`

    ```py
    list.copy()
    ```
    ![Python list indexing ans slicing](https://railsware.com/blog/wp-content/uploads/2018/10/first-slice.png)

List comprehensions
:   creates a new list based on another list, in a single, readable line. aka ==one-liners==

    ```py
    some_list = [1, 2, 'avi', 'mehenwal']
    print([ type(item) for item in some_list ])
    ```

Dictionaries - [Hash Maps](https://en.wikipedia.org/wiki/Hash_table)
:   It stores key-value pairs, where keys are unique and it has $O(1)$ access time.

    The most important <Badge type="error" vertical="middle" text="limitation" />
    for a `dict` is that the keys must be hashable/immutable.
    Meaning, we can use a tuple as a key, but not a list.

Comprehensions in Python
:   Comprehensions in Python provide us with a short and concise way to construct new sequences
    (such as lists, set, dictionary etc.)

    ```mermaid
    graph LR
      A{Pythonic Coprehensions}:::blue
      A --> B(List Comprehension):::green
      A --> E(Set Comprehension):::yellow
      A --> C(Dictionary Comprehension):::orange
      A --> D(Generator Comprehension):::purple

      classDef green fill:#1f9,stroke-width:0px;
      classDef orange fill:#f96,stroke-width:0px;
      classDef blue fill:#b8d4ff,stroke-width:0px;
      classDef purple fill:#f9f,stroke:#333,stroke-width:0px;
      classDef yellow fill:#FFE873,stroke-width:0px;
    ```

## :prayer_beads: Strings

1. ==C-style== string formatting using `%` aka old-style
2. New-style Python `.format()`

Since strings are stored as an array of type `char` in memory, these could be manupulated using
<Badge type="tip" vertical="middle" text="list comprehensions" />


* Type checking using `is` or `instance` keyword

## :envelope_with_arrow: Packages and Modules

Modules for [Modular Programming](https://en.wikipedia.org/wiki/Modular_programming)
:   definitions from a module can be imported into other modules or into the main module

    * Executing modules as scripts
    * views on using `import *`. Are there any dramatic performance changes?
    * Modules search path
    * compiler version of modules saved in `__pycache__` directory
    * `dir()`

Packages
:   collection of modules

    * structuring python module namespace by using dotted module names
    * Packages support one more special attribute, `__path__`. This is initialized to be a list containing the name of the directory holding the package’s __init__.py before the code in that file is executed.
    * `__init__.py` will treat the directory it is in as a loadable module.

## :snail: Exceptions Handling

The `try...except` statement has an optional `else` clause, which, when present, must follow all except clauses.
[It is useful for code that must be executed if the try clause does not raise an exception.](https://stackoverflow.com/questions/855759/python-try-else)

```py
try:
    raise ExcetionName
except ExcetionName:
    pass
    $ multiple exceptions
else:
    # we don't want to catch the ExcetionName exception if it's raised
    another_operation_that_can_throw_ioerror()
finally:
    print('Runs under all circumstances')
```

## :building_construction: Classes

* [old-style vs new-style classes difference](https://realpython.com/python-metaclasses/)

::: tip Aliasing
Objects have individuality, and multiple names (in multiple scopes) can be bound
to the same object. This is known as aliasing in other languages.
:::

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


## :department_store: Scopes and Namespaces

Namespace created by interpreter
:   is a mapping from names to objects.

    Most namespaces are currently implemented as ==Python dictionaries==, but that’s normally not noticeable in any way (except for performance), and it may change in the future. It is like a box where a variable name is mapped to the object placed. Whenever the variable is searched out, this box will be searched, to get corresponding object.

    * <Badge type="tip" vertical="middle" text="global namespace" /> at startup
    * <Badge type="error" vertical="middle" text="local namespace" /> when function is called, deleted, exception, modified etc.
    * When a class definition is entered, a new namespace is created, and used as the local scope — thus, all assignments to local variables go into this new namespace. In particular, function definitions bind the name of the new function here.

Scope
:   is a textual region of a Python program where a namespace is directly accessible. “Directly accessible”


## :closed_book: Standard Library Interfaces

Function | Library name
---------|--------------
File System | `os`, `shutil`, `glob`, `datetime`
i/p, o/p, error streams and CLI args | `sys`
Pattern Matching | `re`
Mathematics | `math`, `random`, `statistics`
Internet and Web | `urllib`
Data Compression | `gzip`, `bz2`
Performance Measurement | `timeit`, `pstats`, `profile`
Quality Control | `doctest`, `unittest`
Threading | `multithreading`

## :question: General Questions

* Modules and Packages
  * modules for business logic-BL  and module for GUI combined together to form a Packages

What is the difference between `'` and `"` quotes in python?
:   As far as language syntax is concerned, there is no difference in single or double quoted string.

    However, if either single or double quote is a part of the string itself,
    then the string must be placed in double or single quotes respectively.

    ```py
    str1='Hello "Python"'
    ```

Difference between `/`, `//` and `%`?
:   `/` classical division return a **float**

    `//` Floor division return an **int**

## :paperclip: References

* https://pyformat.info/


[serialization]: https://en.wikipedia.org/wiki/Serialization
[composite]: https://en.wikipedia.org/wiki/Composite_data_type
[ast]: https://en.wikipedia.org/wiki/Abstract_syntax_tree


