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
"""

string = "This is a ((test)) of the ((emergency station))."
split = re.split(r"(\(\([^)]+\)\))", string)
print(split)

line = 'asdf fjdk; afed, fjek,asdf,      foo'
print(re.split(r'[;,\s]\s*', line))
print(re.split(r'(;|,|\s)\s*', line))
