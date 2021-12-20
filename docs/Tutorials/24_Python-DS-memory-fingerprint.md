---
title: Python Data Sctructure memory Fingerprint
tags:
  - python
  - data
  - structure
  - memory
  - fingerprint
---

# Python Data Sctructure memory Fingerprint

<TagLinks />

```python
import sys
from decimal import *

d = {
    "int": 0,
    "float": 0.0,
    "dict": dict(),
    "set": set(),
    "tuple": tuple(),
    "list": list(),
    "str": "a",
    "unicode": u"a",
    "decimal": Decimal(0),
    "object": object(),
}

for k, v in sorted(d.items()):
    print("{: >10} {: >10} bytes".format(k, sys.getsizeof(v)))

# OUTPUT -----------------------------------------------------
   decimal        104 bytes
      dict        232 bytes
     float         24 bytes
       int         24 bytes
      list         56 bytes
    object         16 bytes
       set        216 bytes
       str         50 bytes
     tuple         40 bytes
   unicode         50 bytes
```

<Footer />
