import unittest

"""
unittest.TestCase -> return the test case name

SELF=test_case_1 (__main__.SomeTestClassName)
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
"""

class SomeTestClassName(unittest.TestCase):

    def test_case_1(self):
        print('SELF={}'.format(self))
        import pdb; pdb.set_trace()

    def test_case_2(self):
        pass


if __name__ == '__main__':
    unittest.main()
