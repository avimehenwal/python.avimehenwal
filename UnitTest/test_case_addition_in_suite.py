import unittest

"""
Tests are added to TestClass dynamically in its __dict__ and dir(TestClass)

(Pdb) pprint(dict(TestClass.__dict__))
{'__doc__': None,
 '__module__': '__main__',
 'test_one': <function test at 0x10b2d8c08>,
 'test_thr': <function test at 0x10b2d8cf8>,
 'test_two': <function test at 0x10b2d8c80>}
(Pdb)
"""

class TestClass(unittest.TestCase): pass

def gen_test(data):
    def test(self):
        print self, data
    return test
    
suite1 = unittest.TestSuite()
suite2 = unittest.TestSuite()

setattr(TestClass, 'test_one', gen_test('one'))
setattr(TestClass, 'test_two', gen_test('two'))
setattr(TestClass, 'test_thr', gen_test('thr'))

suite2.addTest(TestClass('test_one'))
suite1.addTest(TestClass('test_two'))

suite = unittest.TestSuite([suite1, suite2])

unittest.TextTestRunner(verbosity=2).run(suite)
#unittest.main(verbosity=2)
