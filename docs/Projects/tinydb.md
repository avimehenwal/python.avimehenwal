---
title: TinyDB
tags:
- tinydb
- database
- opensource
---

# TinyDB

<TagLinks />

## What will you learn?

Reflection | Topic
:---------:|---------
NA | Writing Sphinx Documentation
NA | System design
NA | pytest 100% code coverage

* 100% code coverage
* Replace setup.py call with pip `pip install .`
  * pip will track version, as it stores other metadata
  * pip can both install and remove. Setup.py hard to uninstall/remove operation

PIP can install python packages from multiple sources

- PyPI (and other indexes) using requirement specifiers.
- VCS project urls.
- Local project directories.
- Local or remote source archives.

* [Middleware](https://en.wikipedia.org/wiki/Middleware)
* [Hook](https://en.wikipedia.org/wiki/Hooking)

There's no real notion of table schemas in TinyDB.
It's basically just an object storage and it's the reponsibility of the user to make sure the object has the expected format.

### How to implement LRU Cache in Python?

Had a cache size, when size is full, least recently used space is evicted. How to find least recently
used space to evict?

* Disadvantage, more overhead, we need to keep track of when the pages were used.

<Footer />
