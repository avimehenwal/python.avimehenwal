---
title: CPython
tags:
- python
- source
- code
- interpreter
- github
---

# CPython

<TagLinks />

## Reading python source code

* [Start with Python C API](https://nedbatchelder.com/text/whirlext.html)
  * Py_INCREF

## Tasks

* [ ] [Compiler python from source](https://stackoverflow.com/questions/8097161/how-would-i-build-python-myself-from-source-code-on-ubuntu)

## Python C API

> Use inside of python to build new python


### Hello World Extension

Why write in C?
:   * speed
    * Legacy
    * Integration
    * Community

* Used to build Python
* ~600 Entrypoints
* only applies to CPython
* Any built-in function or type
* Deal with with C messyness
  * write something and then say we wrote it.
* Building C Extensions - distutils know how to do that
  * `ext_modules`
* `PyObject*` pointer
* Type-specific functions
  * bunch of dedicated `C` functions, just for `dicts`
  * lists etc.
* `Py_BuildValues` like `sprintf`
* `PyArg_ParseTuples` - reading arguments

```py
def hello_world():
    return "Hello World"
```

```c
#include "python.h"

static PyObject *

```

### Memory Management

> most messy part

* Reference counting protocol
  * counting borrowed references
  * `Pt_DECREF`

### Making a Type

1. Create structure
2. Write `init` and `dealloc`
3. decalre members
4. Write functions
5. Declare functions
6. Make the type ready

## References

* [POSIX](https://en.wikipedia.org/wiki/POSIX)


<Footer />
