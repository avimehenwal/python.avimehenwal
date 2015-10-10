#!/usr/env python

__author__ = "avimehenwal"
__date__   = "Thu Oct  8 14:35:44 IST 2015"

"""
Python3 RegEx
"""

import re


"""
search - find something anywhere in the string, and return it.
match  - find something from the beginning of the string, and return it.
metacharacters, qualifiers, Backslash plague

Non-Capturing Groups
>>> re.search("([abc])+", "adbc").groups()
('a',)
>>> re.search("(?:[abc])+", "adbc").groups()
()

Python Named Groups
>>> re.search("(?P<word>\\b\\w+\\b)", "avi yu").group("word")
'avi'

Greedy And Non-Greedy Pattern matching
>>> re.search(r".+", string)
<_sre.SRE_Match object; span=(0, 32), match='English "HEllo" , Spanish "Hola"'>
>>> re.search(r".+?", string)
<_sre.SRE_Match object; span=(0, 1), match='E'>
>>> 
"""

string = "This is a ((test)) of the ((emergency station))."
split = re.split(r"(\(\([^)]+\)\))", string)
print(split)

line = 'asdf fjdk; afed, fjek,asdf,      foo'
print(re.split(r'[;,\s]\s*', line))
print(re.split(r'(;|,|\s)\s*', line))

# Findall non-overlapping occourence of a pattern
pattern = re.compile(r'a*')
pattern.findall("hello world")

# Backreference with substitution \g<number>
text = "imagine a new *world*, a magic *world*"
pattern = re.compile(r'\*(.*?)\*')
print(pattern.sub(r"<b>\g<1>5<\\b>", text))
