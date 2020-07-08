#!/usr/bin/env python

"""
FileName   hidden_features.py
Author     avimehenwal
Created    Sun Mar 27 09:52:24 IST 2016

some cool and interesting stuff with python


try:
    # try to do something
except:
    # handle errors
else:
    # only executed if no errors occurred
finally:
    # always executed
"""


# For ... Else loop
# region snippet
def for_else(n):
    """else in for loop is always executed"""
    for i in n:
        print('Loop', i)
    else:
        print('Else ', n)
# endregion snippet


if __name__ == '__main__':
    for_else('avi')
    for_else([])
    for_else([1, 3, 4])

# END
