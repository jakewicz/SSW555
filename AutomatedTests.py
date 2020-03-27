# This is our test file
import unittest
from Sprint02 import *
from Sprint01 import *
from Sprint03 import *

#format sample
    #def test_US##(self):
        #for indi in (families or individuals):
            #self.assertEquals(call your function, the return when it passes, indi)
#example output:
    #======================================================================
    #FAIL: test_US15_test (__main__.Sprint02Test)
    #----------------------------------------------------------------------
    #Traceback (most recent call last):
    #File "c:/Users/gmigg/Documents/SSW555/SSW555/AllTests.py", line 8, in test_US15_test
        #self.assertEquals(US15_child_max(indi, families), None, indi)
    #AssertionError: 'ERROR: too many kids' != None : @F15@

#IF YOU DONT GET THAT, IT DOESNT WORK

class Test(unittest.TestCase):
    def test_US15(self):
        for indi in families:
            self.assertEqual(US15_child_max(indi, families), None, indi)
    def test_US14(self):
        for indi in families:
            self.assertEqual(US14_quintuplets(indi, families), None, indi)
    def test_US34(self):
        for indi in individuals:
            self.assertEqual(US34_age_difference(indi, individuals), None, indi)
    def test_US21(self):
        for indi in families:
            self.assertEqual(US21_correct_gender(indi, families, individuals), None, indi)

if __name__ == '__main__':
    #this calls the automatic tests
    unittest.main()