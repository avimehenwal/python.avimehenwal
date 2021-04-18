---
title: Associative Array
tags:
  - associative
  - array
  - hashmap
  - hashing
  - dictionary
---

# Associative Arrays

<TagLinks />

> aka **Hash Maps** in java, **dictionaries** in python world, **Objects** in javascript and **Maps** in clojure

Python’s dictionaries are implemented as <Badge type="error" vertical="middle" text="resizable hash tables" />.
Compared to <Badge type="tip" vertical="middle" text="B-trees" />, this gives better performance for lookup (the most common operation by far) under most circumstances, and the implementation is simpler.

![Associate array or hash map](../.vuepress/public/img/associative-array.png)

Dictionaries work by computing a hash code for each key stored in the dictionary using the
built-in `hash()` function. The hash code varies widely depending on the key; for example, “Python”
hashes to -539294296 while “python”, a string that differs by a single bit, hashes to 1142331976.
The hash code is then used to calculate a location in an internal array where the value will be stored.
Assuming that you’re storing keys that all have different hash values, this means that dictionaries
take constant time — $O(1)$, in computer science notation — to retrieve a key. It also means that no
sorted order of the keys is maintained, and traversing the internal array as the dict.keys
and dict.items methods do will output the dictionary’s content in some arbitrary jumbled order.

::: warning Hash function in python
But bear in mind the hash function is implemented for each kind of objects differently.

`hash()` calls `__hash__()` fn internally

::: right
[Python hash implementation](http://effbot.org/zone/python-hash.htm)
:::

- [Hash function implementation in python](https://github.com/ncorbuk/Python-Tutorial---Dictionaries-Hash-Table-Hash-Map-Code-Walk-through-/blob/master/HashTable.py)

Python lists are actually arrays — contiguous chunks of memory.
The name "list" may be misleading to people who know about double-linked lists but are unfamiliar with Python.
You can picture a Python list as a row of slots, where each slot can hold a ==Python object==:

## Usecases

Sending large file from one computer to another?

- Send multiple times and check - naive approach
- Used to verify secure downloads from internet.

Hash Function

1. Avalanch Effect
2. MD5 is badly broken
   1. google search "md5 hash cracker"

## Security vurnabilities

Username - password data stores.

> Prefer 3rd party like Google, Facebook to do it for you

Strategies:

1. Naive approach, store password in plain text and match them on login
2. Use secret key to encrypt and decrypt passwords.
   1. Broken using [Rainbow Tables](https://en.wikipedia.org/wiki/Rainbow_table)
   2. adobe database was hacked using this technique
3. Hashing Algorithms
4. Hashing and Salting

- https://en.wikipedia.org/wiki/Rainbow_table

## Resources

- https://en.wikipedia.org/wiki/Hash_table
- https://en.wikipedia.org/wiki/Associative_array
- https://stackoverflow.com/questions/327311/how-are-pythons-built-in-dictionaries-implemented
- https://www.python.org/dev/peps/pep-0456/
- https://just-taking-a-ride.com/inside_python_dict/chapter4.html

<iframe width="560" height="315" src="https://www.youtube.com/embed/YR7Vp7HcAgs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<Footer />
