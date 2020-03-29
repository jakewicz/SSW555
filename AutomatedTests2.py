import unittest
from Sprint01 import *
from Sprint02 import *
from Sprint03 import *
from Dan_Bianchini_User_Stories import *
from Jacob_Senkewicz_User_Stories import *

class Test(unittest.TestCase):
    def test_US02(self):
        individuals = {'@I1@': {'MARR_AGE': -20}}
        self.assertTrue(US02_born_after_married('@I1@', individuals))

    def test_US03():
        individuals = {'@I1@': {'BIRT': '1 JAN 2000', 'DEAT': '1 JAN 1990'}}
        self.assertTrue(US03_death_before_birth('@I1@', individuals))

    def test_US08():
        individuals = {'@I1@': {'BIRT': '1 JAN 2000', 'FAMC': '@F1@'}}
        families = {'@F1@': {'MARR': '1 JAN 2001'}}
        self.assertTrue(US08_born_before_parents_married('@I1@', individuals, families))

    def test_US12():
        individuals = {'@I1@': {'BIRT': '1 JAN 2000', 'FAMC': '@F1@'}, '@I2@': {'BIRT': '1 JAN 1900'}, '@I3@': {'BIRT': '1 JAN 1970'}}
        families = {'@F1@': {'HUSB': '@I2@', 'WIFE': '@I3@'}}
        self.assertTrue(US12_parents_too_old('@I1@', individuals, families))

    def test_US31():
        print("If ONLY 'one' and 'three' print below this, US31 works:")
        individuals = {'@I1@': {'FAMS': 'N/A', 'AGE': 31, 'NAME': 'one'}, '@I2@': {'FAMS': '@F1@', 'AGE': 31, 'NAME': 'two'}, '@I3@': {'FAMS': 'N/A', 'AGE': 31, 'NAME': 'three'}, '@I3@': {'FAMS': 'N/A', 'AGE': 20, 'NAME': 'four'}}
        self.assertEqual(US31_list_living_single(individuals), None)

    def test_US32():


    def test_US09():


    def test_US23():
