import unittest
import Parser
from Sprint01 import *
from Sprint02 import *
from Sprint03 import *
from Sprint04 import *
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
		print("\nIf ONLY the word 'yes' prints below with no 'no's, US31 works:")
		individuals = {
			'@I1@': {'FAMS': 'N/A', 'AGE': 31, 'NAME': 'yes'},
			'@I2@': {'FAMS': ['@F1@'], 'AGE': 31, 'NAME': 'no'},
			'@I3@': {'FAMS': 'N/A', 'AGE': 31, 'NAME': 'yes'},
			'@I4@': {'FAMS': 'N/A', 'AGE': 20, 'NAME': 'no'}
		}
		self.assertEqual(US31_list_living_single(individuals), None)

	def test_US32(self):
		print("\nIf ONLY the word 'yes' prints below with no 'no's, US32 works:")
		individuals = {
			'@I1@': {'NAME': 'yes', 'BIRT': '1 JAN 2000'},
			'@I2@': {'NAME': 'yes', 'BIRT': '1 JAN 2000'},
			'@I3@': {'NAME': 'yes', 'BIRT': '1 JAN 2000'},
			'@I4@': {'NAME': 'no', 'BIRT': '1 MAR 2000'}
		}
		families = {'@F1@': {'CHIL': ['@I1@', '@I2@', '@I3@', '@I4@']}}
		self.assertEqual(US32_list_multiple_births(individuals, families), None)

	def test_US35(self): 
		print("\nIf ONLY the word 'yes' prints below with no 'no's, US35 works:")
		individuals = {
			'@I1@': {'NAME': 'yes', 'BIRT': '20 MAR 2020'},
			'@I2@': {'NAME': 'yes', 'BIRT': '21 MAR 2020'},
			'@I3@': {'NAME': 'no', 'BIRT': '1 JAN 2000'},
			'@I4@': {'NAME': 'no', 'BIRT': '1 MAR 2000'}
		}
		self.assertEqual(US35_recent_births(individuals), None)

	def test_US36(self):
		print("\nIf ONLY the word 'yes' prints below with no 'no's, US36 works:")
		individuals = {
			'@I1@': {'NAME': 'yes', 'DEAT': '20 MAR 2020'},
			'@I2@': {'NAME': 'yes', 'DEAT': '21 MAR 2020'},
			'@I3@': {'NAME': 'no', 'DEAT': '1 JAN 2000'},
			'@I4@': {'NAME': 'no', 'DEAT': '1 MAR 2000'}
		}
		self.assertEqual(US36_recent_deaths(individuals), None)			
		
	def test_US16(self):
		individuals = {
			'@I2@': {'SEX': 'M', 'NAME': 'Frank /Sagat/'},
			'@I3@': {'SEX': 'M', 'NAME': 'Mike /Tyson/'},
			'@I4@': {'SEX': 'F', 'NAME': 'Olivia /Tyson/'}}
		self.assertFalse(US16_get_last_names(individuals))
	
	def test_US17(self):
		individuals = {
			'@I1@': {'FAMS': ['@F1@', '@F2@']},
			'@I2@': {'FAMS': ['@F2@']}
		}
		families = {'@F1@': {'CHIL': ['@I2@']}}
		self.assertTrue(US17_dont_marry_children('@I1@', individuals, families))
	
	def test_US18(self):
		individuals = {
			'@I1@': {'FAMC':'@F1@', 'FAMS': ['@F2@']},
			'@I2@': {'FAMC':'@F1@', 'FAMS': ['@F2@']}
		}
		families = {'@F1@': {'CHIL': ['@I1@', '@I2@']}}
		self.assertTrue(US18_siblings_should_not_marry('@I1@', individuals, families))
	
	def test_US30(self):
		print("\nIf ONLY the word 'yes' prints below with no 'no's, US30 works:")
		individuals = {
			'@I1@': {'FAMS': 'N/A', 'DEAT': 'N/A', 'NAME': 'no'},
			'@I2@': {'FAMS': ['@F1@'], 'DEAT': 'N/A', 'NAME': 'yes'},
			'@I3@': {'FAMS': ['@F2@'], 'DEAT': '1 JAN 2020', 'NAME': 'no'}
		}
		self.assertEqual(US30_list_living_married(individuals), None)

	def test_US01(self):
		individuals= {'@I1@': {'BIRT' :'13 FEB 2022'}}
		self.assertTrue(US01_check_current_date('@I1@', individuals))
	def test_US10(self):
		individuals = {'@I1@':{'MARR_AGE': 12}}
		self.assertTrue(US10_young_marriage('@I1@', individuals))

#Gianna automated tests for all 3 sprints
	def test_US04(self):
		individuals = {'@I1@': {'MARR_AGE': 25, 'DIV_AGE': 35}}
		self.assertEqual(US04_married_before_div('@I1@', individuals), "valid")
	def test_US05(self):
		individuals = {'@I1@': {'MARR_AGE': 25, 'AGE': 35}}
		self.assertEqual(US05_married_before_death('@I1@', individuals), "valid")
	def test_US14(self):
		individuals = {
			'@I1@': {'NAME': 'quin1', 'BIRT': '1 MAR 2000'},
			'@I2@': {'NAME': 'quin2', 'BIRT': '1 MAR 2000'},
			'@I3@': {'NAME': 'quin3', 'BIRT': '1 MAR 2000'},
			'@I4@': {'NAME': 'quin4', 'BIRT': '1 MAR 2000'},
			'@I5@': {'NAME': 'quin5', 'BIRT': '1 MAR 2000'},
			'@I6@': {'NAME': 'quin6', 'BIRT': '1 MAR 2000'}
		}
		families = {'@F1@': {'CHIL': ['@I1@', '@I2@', '@I3@', '@I4@', '@I5@', '@I6@']}}
		self.assertEqual(US14_quintuplets('@F1@', families, individuals), "ERROR: more than 5 kids born at once")
	def test_US15(self):
		families = {'@F1@': {'CHIL': ['@I1@', '@I2@', '@I3@', '@I4@', '@I5@', '@I6@','@I7@', '@I8@', '@I9@', '@I10@', '@I11@', '@I12@'
					'@I13@', '@I14@', '@I15@', '@I16@', '@I17@']}}
		self.assertEqual(US15_child_max('@F1@', families), "ERROR: too many kids")
	def test_US21(self):
		individuals = {'@I1@': {'NAME': 'Gianna', 'SEX': 'F'}}
		families = {'@F1@': {'HUSB': '@I1@'}}
		self.assertEqual(US21_correct_gender('@F1@', families, individuals), 'ERROR: US21 wrong gender for role')
	def test_US34(self):
		individuals = {
			'@I1@': {'NAME': 'young', 'SPOUSE': '@I2@', 'MARR_AGE': 22},
			'@I2@': {'NAME': 'old', 'SPOUSE': '@I1@', 'MARR_AGE': 45}}
		self.assertEqual(US34_age_difference('@I1@', individuals), 'ERROR: US34 large age difference in married couple')
	def test_US38(self):
		individuals = {
			'@I1@': {'NAME': 'birthday', 'BIRT': '30 MAR 2000'},
			'@I2@': {'NAME': 'bday', 'BIRT': '10 APR 2000'},
			'@I3@': {'NAME': 'not soon', 'BIRT': '10 SEP 2012'},
		}
		self.assertEqual(US38_upcoming_bdays(individuals), ['@I1@', '@I2@'])
	def test_US39(self):
		individuals = {
			'@I1@': {'NAME': 'wife'},
			'@I2@': {'NAME': 'husband'},
		}
		families = {
			'@F1@': {'HUSB': '@I2@', 'WIFE': '@I1@', 'MARR': '8 APR 2007'},
			'@F2@': {'HUSB': '@I2@', 'WIFE': '@I1@', 'MARR': '8 OCT 2007'}
		}
		self.assertEqual(US39_upcoming_anniversary(families, individuals), ['@F1@'])

		
	# Dan sprint 4
	def test_US09(self):
		individuals ={
			'@I1@': {'BIRT': '1 JAN 2000', 'FAMC': '@F1@'},
			'@I2@': {'DEAT': '1 JAN 1990'},
			'@I3@': {'DEAT': 'N/A'}
		}
		families = {'@F1@': {'HUSB': '@I2@', 'WIFE': '@I3@'}}
		self.assertTrue(US09_born_after_parents_death('@I1@', individuals, families))

	def test_US23(self):
		print("\nUS23: Should ONLY print @I1@, @I2@, and @I3@:")
		individuals = {
			'@I1@': {'NAME': 'yes', 'BIRT': '1 JAN 2000'},
			'@I2@': {'NAME': 'yes', 'BIRT': '1 JAN 2000'},
			'@I3@': {'NAME': 'yes', 'BIRT': '1 JAN 2000'},
			'@I4@': {'NAME': 'no', 'BIRT': '1 MAR 2000'}
		}
		self.assertEqual(US23_unique_name_and_birthday(individuals), None)

	def test_US25(self):
		individuals = {
			'@I1@': {'NAME': 'Jake', 'BIRT': '8 FEB 1999'},
			'@I2@': {'NAME': 'Jake','BIRT': '8 FEB 1999'}
		}
		families = {
			'@F1@': {'CHIL': ['@I1@', '@I2@']}
		}
		self.assertTrue(US25_unique_first_names(individuals,families))

	def test_US42(self):
		individuals = {
			'@I1@': {'NAME': 'Jake', 'BIRT': '30 FEB 1999'}
		}	
		families = {
			'@F1@': {'MARR': '40 APR 1970'}

		}
		self.assertFalse(US42_legit_dates('@I1@', individuals, families))

	def test_US37(self):
		individuals = {
			'@I1@' : {'NAME': 'dead', 'BIRT': '13 FEB 1980', 'DEAT': '11 APR 2020', 'SPOUSE': '@I2@', 'CHILD': '@I3@'},
			'@I2@' : {'NAME': 'wife', 'BIRT': '15 FEB 1981', 'DEAT': 'N/A'},
			'@I3@' : {'NAME': 'child', 'BIRT': '15 FEB 2008', 'DEAT': 'N/A'}
		}
		self.assertEqual(US37_recent_survivors(individuals), ['@I3@'])

	def test_US33(self):
		print("\nIf ONLY the word 'yes' prints below with no 'no's, US33 works:")
		individuals = {
			'@I1@' : {'NAME': 'no', 'BIRT': '13 FEB 1980', 'DEAT': '11 APR 2009', 'SPOUSE': '@I2@', 'CHILD': '@I3@'},
			'@I2@' : {'NAME': 'no', 'BIRT': '15 FEB 1981', 'DEAT': '11 APR 2009', 'SPOUSE': '@I1@', 'CHILD': '@I3@'},
			'@I3@' : {'NAME': 'yes', 'BIRT': '15 FEB 2008', 'DEAT': 'N/A'}
		}
		families = {
			'@F1@': {'HUSB': '@I1@', 'WIFE': '@I2@', 'CHIL': ['@I3@']}
		}
		self.assertEqual(US33_list_orphans(families, individuals), None)

# needs to be at the end, don't touch this
if __name__ == '__main__':
	unittest.main()

