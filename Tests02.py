# This is our test file
from Sprint02 import *
import unittest

def test_child_max(indi, families):
    if(child_max(indi, families) == "ERROR: married before born"):
        return ("ERROR: too many kids")
    else: return("child max test passed")

def test_quintuplets(indi, families):
    if(quintuplets(indi, families) == "ERROR: married before born"):
        return ("ERROR: more than 5 kids born at once")
    else: return("quintuplets test passed")

for indi in families:
    print(indi)
    print(test_child_max(indi, families))
    print(test_quintuplets(indi, families))


class Test_Parser(unittest.TestCase):

    def test_dont_marry_children(self): #US 17
        self.assertEqual(dont_marry_children(families.values()), [])
    def test_get_last_names(self): #US 16
        self.assertEqual(get_last_names(individuals.values()), ["Chlus", "Chlus", "Fisher", "Fisher", "Chlus", "Chlus", "Najjar", "Najjar", "Najjar", "Najjar","Cambalik", "Cambalik", "Cambalik"])

unittest.main()
