---
title: Dunder Methods
tags:
  - dunder
  - python
---

# Dunder Methods

<TagLinks />

What is `__all__` in `__init__.py`?

: It's a list of public objects of that module, as interpreted by `import *`. It overrides the default of hiding everything that begins with an underscore.

    When yo do `import * from XYZ` all methods mentioned explicitly in `__all__` will be imported

What is `__init.py__` in python modules?

: required for Python to treat the directories as containing packages

    ==Python defines two types of packages, regular packages and namespace packages.== Regular packages are traditional packages as they existed in Python 3.2 and earlier. A regular package is typically implemented as a directory containing an __init__.py file. When a regular package is imported, this __init__.py file is implicitly executed, and the objects it defines are bound to names in the package’s namespace. The __init__.py file can contain the same Python code that any other module can contain, and Python will add some additional attributes to the module when it is imported.

<Footer />
