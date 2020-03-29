import unittest
import Parser
from Sprint01 import *
from Sprint02 import *
from Sprint03 import *
from Dan_Bianchini_User_Stories import *
from Jacob_Senkewicz_User_Stories import *

individuals_ged, families_ged = Parser.read_file("./test.ged")

class Test(unittest.TestCase):
	def test_US02(self):
		individuals = {'@I1@': {'MARR_AGE': -20}}
		self.assertTrue(US02_born_after_married('@I1@', individuals))

	def test_US03(self):
		individuals = {'@I1@': {'BIRT': '1 JAN 2000', 'DEAT': '1 JAN 1990'}}
		self.assertTrue(US03_death_before_birth('@I1@', individuals))

	def test_US08(self):
		individuals = {'@I1@': {'BIRT': '1 JAN 2000', 'FAMC': '@F1@'}}
		families = {'@F1@': {'MARR': '1 JAN 2001'}}
		self.assertTrue(US08_born_before_parents_married('@I1@', individuals, families))

	def test_US12(self):
		individuals = {
			'@I1@': {'BIRT': '1 JAN 2000', 'FAMC': '@F1@'},
			'@I2@': {'BIRT': '1 JAN 1900'},
			'@I3@': {'BIRT': '1 JAN 1970'}
		}
		families = {'@F1@': {'HUSB': '@I2@', 'WIFE': '@I3@'}}
		self.assertTrue(US12_parents_too_old('@I1@', individuals, families))

	def test_US31(self):
		print("If ONLY the word 'yes' prints below with no 'no's, US31 works:")
		individuals = {
			'@I1@': {'FAMS': 'N/A', 'AGE': 31, 'NAME': 'yes'},
			'@I2@': {'FAMS': '@F1@', 'AGE': 31, 'NAME': 'no'},
			'@I3@': {'FAMS': 'N/A', 'AGE': 31, 'NAME': 'yes'},
			'@I4@': {'FAMS': 'N/A', 'AGE': 20, 'NAME': 'no'}
		}
		self.assertEqual(US31_list_living_single(individuals), None)

	def test_US32(self):
		print("If ONLY the word 'yes' prints below with no 'no's, US32 works:")
		individuals = {
			'@I1@': {'NAME': 'yes', 'BIRT': '1 JAN 2000'},
			'@I2@': {'NAME': 'yes', 'BIRT': '1 JAN 2000'},
			'@I3@': {'NAME': 'yes', 'BIRT': '1 JAN 2000'},
			'@I4@': {'NAME': 'no', 'BIRT': '1 MAR 2000'}
		}
		families = {'@F1@': {'CHIL': ['@I1@', '@I2@', '@I3@', '@I4@']}}
		self.assertEqual(US32_list_multiple_births(individuals, families), None)
	    
	def test_US01(self):
        	individuals = {'@I1@':{'BIRT:13 Feb 2022'}}
        	self.assertTrue(US01_check_current_date('@I1@', individuals))
		
   	def test_US10(self):
        	individuals = {'@I1@':{'MARR_AGE': 12}}
        	self.assertTrue(US10_young_marriage('@I1@', individuals))
		
    	def test_US16(self):
        	individuals = {'@I1@':{'SEX': 'F'}}
        	self.AssertTrue(US16_get_last_names('@I1@',individuals))
		
    	def test_US17(self):
        	individuals = {
            	'@I1@': {'FAMS':'@F2@'},
            	'@I2@': {'FAMS':'@F2@'}
        	}
        	families = {'@F1@': {'HUSB': '@I1@', 'WIFE': '@I3@', 'CHIL': '@I3@'}}
        	self.assertTrue(US17_dont_marry_children('@I1@', individuals, families))
		
    	def test_US18(self):
        	individuals = {
            	'@I1@': {'FAMC':'@F1@'},
            	'@I2@': {'FAMC':'@F1@'}
        	}
        	families = {'@F1@': {'HUSB': '@I1@', 'WIFE': '@I2@'}}
        	self.assertTrue(US18_siblings_should_not_marry('@I1@', individuals, families))
		
    	def test_US30(self):
        	individuals = {
            	'@I1@': {'FAMS':'N/A', 'DEAT':'5 OCT 2016'},
            	'@I2@': {'FAMS':'N/A', 'DEAT': 'N/A'},
            	'@I3@': {'FAMS': '@I4@', 'DEAT': 'N/A'}
        	}
        	self.assertTrue(US30_list_living_married(individuals))


# needs to be at the end, don't touch this
if __name__ == '__main__':
	unittest.main()
