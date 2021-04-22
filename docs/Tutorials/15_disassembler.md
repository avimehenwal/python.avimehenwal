---
title: Disassembler
tags:
  - python
  - dis
  - disassembler
---

# Disassembler

<TagLinks />

## PVM Python Virtual Machine

- Python Objects
- Code/Compiled Objects
- Frame Objects
- Abstract Syntax Tree
- MRO Method Resolution Order

Identify how `{}` is better than `dict()`

```py
import dis
dis.dis("{}")
          0 BUILD_MAP                0
          2 RETURN_VALUE
dis.dis("dict()")
          0 LOAD_NAME                0 (dict)
          2 CALL_FUNCTION            0
          4 RETURN_VALUE

# python compiler objects
hello.__code__
<code object hello at 0x104e46930, file "<stdin>", line 1>
hello.__code__.co_consts
(None, 'Hello, World!')
hello.__code__.co_varnames
()
hello.__code__.co_names
('print',)
```

<Footer />
