
import timeit

PYTEST = """
from logilab.common.testlib import TestCase

class TestFramework(TestCase):
    %s
"""

UNITTEST = """
from unittest import TestCase, main

class TestFramework(TestCase):
    %s
main()
"""

NTESTS = 400

TEST = """
    def test_assert_true%i(self):
        self.assert_(True)
"""


class Evaluator(object):

    def __init__(self, fname, body, cmd):
        self.fname = fname
        self._body = body
        self._cmd = cmd
        self.time = None

    def generate(self):
        fid = open(self.fname, "w")
        tests = [TEST % idx for idx in range(NTESTS)]
        fid.write(self._body % "".join(tests))
        fid.close()

    def build_cmd(self):
        return "%s %s" % (self._cmd, self.fname)
    
    def run(self):
        run_cmd = self.build_cmd()
        print "Evaluating '%s'" % run_cmd
        timer_cmd = 'os.system("%s &> /dev/null")' % run_cmd
        timer = timeit.Timer(timer_cmd, "import os")
        self.time = timer.timeit(5)
        

if __name__ == "__main__":
    pytest = Evaluator("test_pytest.py", PYTEST, "pytest")
    unittest = Evaluator("test_unittest.py", UNITTEST, "python")
    for evl in [pytest, unittest]:
        evl.generate()
        evl.run()
    resume = [
         "From the 'timeit' evaluation of %i tests, " \
         "pytest seems to be %.2f times slower than unittest." % \
         (NTESTS, pytest.time / unittest.time),
         "",
         "For evaluating by yourself, you may try:",
         "",
         "   time %s" % pytest.build_cmd(),
         "   time %s" % unittest.build_cmd(),
         "",
         "For cleaning:",
         "",
         "   rm %(pytest)s %(pytest)sc %(unittest)s" % \
         {"pytest" : pytest.fname, "unittest" : unittest.fname},
         "",
         ]
    print "\n".join(resume)
    
