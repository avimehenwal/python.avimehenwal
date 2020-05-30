import unittest

"""
The __new__ method in the metaclass gets called when the class itself is defined, not when the first instance is created. I would imagine this method of dynamically creating test methods is more compatible with the introspection used by unittest to determine how many tests are in a class (i.e. it may compile the list of tests before it ever creates an instance of that class).


import unittest

class CustomTest(unittest.TestCase):
    def __init__(self, name, a, b):
        super().__init__()
        self.name = name
        self.a = a
        self.b = b

    def runTest(self):
        print("test", name)
        self.assertEqual(a, b)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(CustomTest("Foo", 1337, 1337))
    suite.addTest(CustomTest("Bar", 0xDEAD, 0xC0DE))
    unittest.TextTestRunner().run(suite)




class TestPreReqs(unittest.TestCase):
    ...

def create_test (pair):
    def do_test_expected(self):
        self.assertEqual(under_test(pair[0]), pair[1])
    return do_test_expected

for k, pair in enumerate ([(23, 55), (4, 32)]):
    test_method = create_test (pair)
    test_method.__name__ = 'test_expected_%d' % k
    setattr (TestPreReqs, test_method.__name__, test_method)
"""


l = [["foo", "a", "a",], ["bar", "a", "b"], ["lee", "b", "b"]]

class TestSequenceMeta(type):
    def __new__(mcs, name, bases, dict):

        def gen_test(a, b):
            def test(self):
                self.assertEqual(a, b)
            return test

        for tname, a, b in l:
            test_name = "test_%s" % tname
            dict[test_name] = gen_test(a,b)
        return type.__new__(mcs, name, bases, dict)

class TestSequence(unittest.TestCase):
    __metaclass__ = TestSequenceMeta

if __name__ == '__main__':
    unittest.main(verbosity=2)
