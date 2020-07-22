---
title: New Python Features
tags:
- new
- latest
- walrus
- operator
- features
---

# :star2: New Python Features

<TagLinks />

The Walrus Operator
:    `:=` assigns values to variables as part of a larger expression

    ```py
    # Handle a matched regex
    if (match := pattern.search(data)) is not None:
        # Do something with match

    # A loop that can't be trivially rewritten using 2-arg iter()
    while chunk := file.read(8192):
       process(chunk)
   ```

Positional and keyword Parameters
:    `def f(a, b, /, c, d, *, e, f):`

    ```py
    def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only
    ```

Parameter | Argument
:   ==Parameter== is variable in the declaration of function.

    <Badge type="tip" vertical="middle" text="Argument" /> is the actual value of this variable that gets passed to function.

    ```java
    public void MyMethod(string myParam) { }

    string myArg1 = "this is my argument";
    myClass.MyMethod(myArg1);
    ```


