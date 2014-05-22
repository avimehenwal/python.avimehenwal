################################################
# UNIT-TEST
################################################

"""
Unit tests for DictDiffer
-------------------------
"""

__author__ = 'AviMehenwal'

try:
    import DictDiffer
except:
    print "Cant import DictDiffer"
    
import unittest     


class TestDictDiffer(unittest.TestCase):
    """ Unittest cases for DictDiffer """

    def __init__(self, testName, data):
        super(TestDictDiffer, self).__init__(testName)
            # calling the super class init varies for different python versions.
        self.data = data


    def setUp(self):
        """ Initializing sample current and previous dictionaries with class instance """

        try:   
            self.d = DictDiffer.DictDiffer(self.data['current'], self.data['previous'])
        except :
            print 'cannot instantiate DictDiffer.DictDiffer'


    def test_no_parameters(self):
        """ no parameters: DictDiffer throws a Traceback """
        
        try:
            e = DictDiffer.DictDiffer()
            print e
        except:
            print 'exception'
            self.assertRaises('TypeError')


    def test_valid_parameters_string_dict(self):
        """ valid str dictionaries: instance of class is created """
        
        self.assertIsInstance(self.d, DictDiffer.DictDiffer)
        

    def test_is_dict_changed(self):
        """ changed() returns the key whose value has been changed """

        print "test_is_dict_changed", self.d.changed()
        self.assertEquals(self.d.changed(), self.data['changed'])


    def test_is_dict_removed(self):
        """ removed() returns the key which has been removed from current """
        
        print "test_is_dict_removed", self.d.removed()
        self.assertEquals(self.d.removed(), self.data['removed'])


    def test_is_dict_added(self):
        """ added() returns the keys which are newely added in current """

        print "test_is_dict_added", self.d.added()
        self.assertEquals(self.d.added(), self.data['added'])


    def test_is_dict_unChanged(self):
        """ unchanged() returns unchanged keys from the dictionaries """

        print "test_is_dict_unChanged", self.d.unchanged()
        self.assertEquals(self.d.unchanged(), self.data['unchanged'])


    def test_is_dict_match(self):
        """ match() returns boolean value to check if dicts match or not """

        print "test_is_dict_match", self.d.ismatch()
        print self.data['ismatch']
##        self.assertNotEqual(self.current, self.previous)
        self.assertEqual(self.d.ismatch(), self.data['ismatch'])


    def test_is_dict_diff(self):
        """ diff() returns the differences from the 2 dicts """

        print "test_is_dict_diff", self.d.diff()
        self.assertEqual(self.d.diff(), self.data['diff'])




if __name__ == '__main__':

    
    dataSet = [ # Random Data sample
        
                {   "current"   :   {'a':'a', 'b':'b', 'd':'z'},
                    "previous"  :   {'b':'b', 'c':'c', 'd':'d'},
                    "added"     :   set(['a']),
                    "removed"   :   set(['c']),
                    "changed"   :   set(['d']),
                    "unchanged" :   set(['b']),
                    "diff"      :   set(['a', 'c']),
                    "ismatch"   :   False,
                },

                # One empty one non-empty dictionary
                
                {   "current"   :   {},
                    "previous"  :   {'b':'b', 'c':'c', 'd':'d'},
                    "added"     :   set([]),
                    "removed"   :   set(['c', 'b', 'd']),
                    "changed"   :   set([]),
                    "unchanged" :   set([]),
                    "diff"      :   set(['c', 'b', 'd']),
                    "ismatch"   :   False,
                },

                # Both Empty dictionaries

                {   "current"   :   {},
                    "previous"  :   {},
                    "added"     :   set([]),
                    "removed"   :   set([]),
                    "changed"   :   set([]),
                    "unchanged" :   set([]),
                    "diff"      :   set([]),
                    "ismatch"   :   True,
                },

                # Equal Text Dictionaries

                {   "current"   :   {'first':'avi', 'last':'mehenwal', 'age':25, 'p':1},
                    "previous"  :   {'first':'avi', 'last':'mehenwal', 'age':25, 'p':1},
                    "added"     :   set([]),
                    "removed"   :   set([]),
                    "changed"   :   set([]),
                    "unchanged" :   set(['p', 'age', 'last', 'first']),
                    "diff"      :   set([]),
                    "ismatch"   :   True,
                },

                # And so on ...
                
               ]

    count = 0
    for data in dataSet:

        count+=1
        print "="*50
        print "RUNNING TESTS ON DATA SET NO : [%s] "%(count)
        print "="*50
        
        suite = unittest.TestSuite()
        suite.addTest(TestDictDiffer('test_no_parameters', data))
        suite.addTest(TestDictDiffer('test_valid_parameters_string_dict', data))
        suite.addTest(TestDictDiffer('test_is_dict_changed', data))
        suite.addTest(TestDictDiffer('test_is_dict_removed', data))
        suite.addTest(TestDictDiffer('test_is_dict_added', data))
        suite.addTest(TestDictDiffer('test_is_dict_unChanged', data))
        suite.addTest(TestDictDiffer('test_is_dict_match', data))
        suite.addTest(TestDictDiffer('test_is_dict_diff',data))
        unittest.TextTestRunner(verbosity=1).run(suite)

# END
