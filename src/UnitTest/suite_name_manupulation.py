import unittest
import HTMLTestRunner

"""
Change test suite name dynamically
"""

class AviClass(unittest.TestCase): pass

def gen_test(data):
    def test(self):
        print self, data
    return test
    
suite = unittest.TestSuite()

setattr(AviClass, 'test_one', gen_test('one'))
setattr(AviClass, 'test_two', gen_test('two'))
setattr(AviClass, 'test_thr', gen_test('thr'))

suite.addTest(AviClass('test_one'))
suite.addTest(AviClass('test_two'))

AviClass.__name__ = 'CHANGED'

#unittest.TextTestRunner(verbosity=2).run(suite)
with open('report.html', 'w') as outfile:
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=outfile,
        title='[QA]Reflektion UAT Report',
        description='powered by xcheck framework (pronounced as cross-check)'
    )
    runner.run(suite)
