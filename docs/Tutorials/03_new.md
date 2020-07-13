---
title: New Python Features
tags:
- new
- latest
- walrus
- operator
- features
---

# :new: New Python Features

<TagLinks />

The Walrus Operator `:=`
:   assigns values to variables as part of a larger expression

Positional and keyword Parameters `def f(a, b, /, c, d, *, e, f):`
:   ```
    def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only
    ```

Parameter
: is variable in the declaration of function.

Argument
: is the actual value of this variable that gets passed to function.

```
public void MyMethod(string myParam) { }

string myArg1 = "this is my argument";
myClass.MyMethod(myArg1);
```


