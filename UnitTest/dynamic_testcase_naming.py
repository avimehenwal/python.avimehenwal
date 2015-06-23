"""
http://www.voidspace.org.uk/python/articles/introduction-to-unittest.shtml
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


