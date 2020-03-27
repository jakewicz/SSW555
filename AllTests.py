# This is our test file
import unittest
from Sprint02 import *
from Sprint01 import *

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

class Sprint02Test(unittest.TestCase):
    def test_US15(self):
        for indi in families:
            self.assertEqual(US15_child_max(indi, families), None, indi)
    def test_US14(self):
        for indi in families:
            self.assertEqual(US14_quintuplets(indi, families), None, indi)


#DO NOT EDIT AFTER THIS POINT
if __name__ == '__main__':
    #sprint 1 tests, old format
    def US02_test_marriage_after_birth(indi, individuals):
        if(US02_marriage_after_birth(indi, individuals) == "ERROR: married before born"):
            print("ERROR: US02", indi, ": married before born")

    def US03_test_birth_before_death(indi, individuals):
        if(US03_birth_before_death(indi, individuals)== "Error: death date cannot be before birth date"):
            print("ERROR: US03", indi,  ": death date cannot be before birth date")

    def US07_test_check150(indi, individual):
        if (US07_check150(indi, individual) == "Error: Too Old"):
            print("ERROR: US07", indi, ": Individual is over 150 years old ")

    def US06_test_divorce_before_death(indi, individuals):
        if(US06_divorce_before_death(indi, individuals) == "Error: cannot get divorced after death"):
            print("ERROR: US06", indi, ": cannot get divorced after death")

    def US10_test_young_marriage(indi, individuals):
        if (US10_young_marriage(indi, individuals) == "Error: Too young to get married, must be at least 14 years old"):
            print("ERROR: US10", indi, ": Too young to get married, must be at least 14 years old")

    def US01_test_check_current_date(indi, individuals):
        if (US01_check_current_date(indi, individuals) == "Error: date is after the current date"):
            print("ERROR: US01", indi, ": date is after the current date")

    def US05_test_married_before_death(indi, individuals):
        if (US05_married_before_death(indi, individuals) == "Error: cannot get married after death"):
            print("ERROR: US05", indi, ": cannot get married after death")

    def US04_test_married_before_div(indi, individuals):
        if (US04_married_before_div(indi, individuals) == "Error: marriage date after divorce date"):
            print( "ERROR: US04", indi, ": marriage date after divorce date")

    for indi in individuals:
        US01_test_check_current_date(indi, individuals)
        US02_test_marriage_after_birth(indi, individuals)
        US03_test_birth_before_death(indi, individuals)
        US04_test_married_before_div(indi, individuals)
        US05_test_married_before_death(indi, individuals)
        US06_test_divorce_before_death(indi, individuals)
        US07_test_check150(indi, individuals)
        US10_test_young_marriage(indi, individuals)

    #this calls the automatic tests
    unittest.main()