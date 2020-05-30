import unittest
import HTMLTestRunner

class TestSuiteOne(unittest.TestCase):
    def test_1(self):
        print "<a href='#'>hello from passing test</a>"
        self.assertTrue(True)

    def test_2(self):
        msg = '<strong>YES!</strong> <h2>It failed</h2>'
        print msg
        raise Exception
        #try:
        #    self.assertTrue(False, msg)
        #except AssertionError:
        #    print msg
        #raise AssertionError(msg)

    def test_3(self):
        self.assertTrue(False)

class TestSuiteTwo(unittest.TestCase):
    def test_1(self):
        self.assertTrue(True)
    def test_2(self):
        self.assertTrue(True)
    def test_3(self):
        self.assertTrue(True)
        
class TestSuiteThree(unittest.TestCase):
    def test_1(self):
        self.assertTrue(False)
    def test_2(self):
        self.assertTrue(False)
    def test_3(self):
        self.assertTrue(False)

if __name__ == '__main__':
    #suite = unittest.TestSuite()
    #suite.addTest(SampleTestCases('test_1'))
    #suite.addTest(SampleTestCases('test_2'))
    #print suite
    #unittest.TextTestRunner(verbosity=2).run(suite)

    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestSuiteOne)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestSuiteTwo)
    suite3 = unittest.TestLoader().loadTestsFromTestCase(TestSuiteThree)

    suite = unittest.TestSuite([suite1, suite2, suite3])
    #import pdb; pdb.set_trace()
    #unittest.TextTestRunner(verbosity=2).run(suite)

    with open('result_file.html', 'w') as outfile:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='[QA]Reflektion UAT Report',
            description='Code Freeze test results'
        )
        runner.run(suite)
