"""
http://www.voidspace.org.uk/python/articles/introduction-to-unittest.shtml

DDT Style testing with unittest

test_bar_(a,b) (__main__.TestSequense) ... FAIL
test_foo_(a,a) (__main__.TestSequense) ... ok
test_lee_(b,b) (__main__.TestSequense) ... ok

======================================================================
FAIL: test_bar_(a,b) (__main__.TestSequense)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "dynamic_testcase_naming.py", line 14, in test
    self.assertEqual(a,b)
AssertionError: 'a' != 'b'
- a
+ b


----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=1)
"""

import unittest

l = [["foo", "a", "a",], ["bar", "a", "b"], ["lee", "b", "b"]]

class TestSequense(unittest.TestCase):
    pass

def test_generator(a, b):
    def test(self):
        self.assertEqual(a,b)
    return test

if __name__ == '__main__':
    for t in l:
        test_name = 'test_{0}_({1},{2})'.format(t[0], t[1], t[2])
        test = test_generator(t[1], t[2])
        setattr(TestSequense, test_name, test)
    unittest.main(verbosity=3)
