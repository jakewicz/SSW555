# This is our test file
from Sprint02 import *

def US15_test_child_max(indi, families):
    if(US15_child_max(indi, families) == "ERROR: too many kids"):
        print("ERROR: US15", indi, ": too many kids")

def US14_test_quintuplets(indi, families):
    if(US14_quintuplets(indi, families) == "ERROR: more than 5 kids born at once"):
        print("ERROR: US14", indi, ": more than 5 kids born at once")

def US29_test_the_deceased(individuals):
    result = US29_the_deceased(individuals)
    if ("ERROR: US29" in result):
        return result
    else:
        return "The deceased: " + str(result)

for indi in families:
    US14_test_quintuplets(indi, families)
    US15_test_child_max(indi, families)
print(US29_test_the_deceased(individuals))