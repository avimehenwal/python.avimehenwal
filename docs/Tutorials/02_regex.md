---
title: Regular Expressions
tags:
- regex
- python
- text
- match
- analysis
- pattern
---

# :eye_speech_bubble: Regular Expressions

<TagLinks />

## :3rd_place_medal: Vocabulary

* Qualifiers, Meta-characters, Meta-classes
* RE works on characters
  * `[0-9]` valid
  * `[0-255]` will get translated to `[0-2]`
* `(?` waits for next character to assign a meaning

Pattern | Description
--------|-------------
`(?:...` | non returning grouping, non capturing version
`(?=...)` | Positive Look ahead Assertion
`(?!...)` | Negative Look ahead Assertion
`(?<=...)` | Positive Look behind Assertion
`(?<!...)` | Negative Look behind Assertion
`(?P<name>)` | named RE pattern
`(?P=name)` | named RE pattern reference

## :1st_place_medal: RE Repetition Qualifiers

* Non-greedy variants (usually followed by `?`)

Greedy Qualifiers | Non-greedy variants
------------------|---------------------
`ab*` | `*?`
`ab+` | `+?`
`ab?` | `??`
`a{6}` | `a{3,5}?`

```py
(.*)    # 0..N Any charter (except space) matching 0 to n number of times
(.+)    # 1..N Match at least 1 to n number of times
(.?)    # 0..1 Match either O or 1 number of time
```

## :baby: Qualifiers

The question mark character, ?, matches either once or zero times; you can think of it as marking something as being optional. For example, home-?brew matches either 'homebrew' or 'home-brew'.

## :footprints: Meta-characters and Meta-character Classes

> Remember in duality

Meta-characters

* `.`, `?`, `*`
* `^`, `$`
* `[...]`, `(...)`, `{...}`
* `(?:...)`, `(?=...)`, `(?!...)`, `(?<=...)`, `(?<!...)`, `(?P<name>...)`, `(?P=name...)`

Meta-character Classes

* `\w`, `\W`
* `\d`, `\D`
* `\a`, `\A`
* `\s`, `\S`


## :four: IP pattern

IP generation Rules

1. 4 octets
2. each octet value between `0-255`
3. Boundary Values `0.0.0.0`, `255.255.255.255`

```python
"""
^                       # first character match after space
(?:[0-9]{1,3}\.)        # non capturing group returning numbers 0-9
                        #     matched 1,2 or 3 times followed by a .
{3}                     # use previous group pattern match exactly 3 times
[0-9]{1,3}
$                       # last character match followed by a space
"""

// Using named group repetition
/^(?:(?P<octet>[0-9]{1,3})\.){3}(?P=octet)$/
```

## :dress: Regex Assertions

Matching and returning the matches based on assertions either by looking forward in the blob or
by looking backward

#### :fast_forward: Positive Look ahead Assertion

Consider the case where use want to match **only** *Issac Asimov* and **not** *Issac Newton*

Pattern | Match return
:------:|--------------
Issac Asimov | :heavy_check_mark: Issac
Issac Newton | :x:

```py
Issac (?=Asimov)
```

#### :rewind: Negative Look ahead Assertion

Reverse the above situation, we want all other *Issacs* which are **not** followed by *Asimov*.
We want *Issac* from *Issac Newton* this time.

Pattern | Match return
:------:|--------------
Issac Asimov | :x:
Issac Newton | :heavy_check_mark: Issac

```py
Issac (?!Asimov)
```

#### :next_track_button: Positive Look behind Assertion

Blob | Patton Match return
:------:|--------------
Avi Mehenwal | :ballot_box_with_check:
Shubhranshu Mehenwal | :x:

Consider we want *Mehenwal* **only** from *Avi Mehenwal* and **not** from *Shubhranshu Mehenwal*

```py
(?<=Avi) Mehenwal
```

#### :previous_track_button: Negative Look behind Assertion

Blob | Pattern Match return
:------:|--------------
Avi Mehenwal | :x:
Shubhranshu Mehenwal | :ballot_box_with_check:

Now lets reverse the situation, we want all *Mehenwal* which are **not** preceded by *Avi*.
We want *Mehenwal* from *Shubhranshu Mehenwal*

```py
(?<!Avi) Mehenwal
```

## :rose: Grep

> Global Regular Expression

egrep - Extended regular expressions
:   include all of the basic **meta-characters**
    along with additional meta-characters to express more complex matches.

## :rosette: Resources

* https://www.regular-expressions.info/refrepeat.html
* [Test and explain your RE](https://regex101.com/)
* [One Liner Programs](https://en.wikipedia.org/wiki/One-liner_program)
* [how-to-replace-perl-one-liner-regex-with-python-one-liner](https://stackoverflow.com/questions/58608239/how-to-replace-perl-one-liner-regex-with-python-one-liner)
* [Python one Liners](https://wiki.python.org/moin/Powerful%20Python%20One-Liners)
* [grep - global regex](https://en.wikipedia.org/wiki/Grep)
* [extended grep](https://www.digitalocean.com/community/tutorials/using-grep-regular-expressions-to-search-for-text-patterns-in-linux)

*[RE]: Regular Expressions | regex

<Footer />
