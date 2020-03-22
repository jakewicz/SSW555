# This is our test file
from Sprint02 import *

def test_child_max(indi, families):
    if(child_max(indi, families) == "ERROR: too many kids"):
        return ("ERROR:", indi, ": too many kids")
    #else: return("child max test passed")

def test_quintuplets(indi, families):
    if(quintuplets(indi, families) == "ERROR: more than 5 kids born at once"):
        return ("ERROR:", indi, ": more than 5 kids born at once")
    #else: return("quintuplets test passed")

def test_the_deceased(individuals):
    result = the_deceased(individuals)
    if ("ERROR" in result):
        return result
    else:
        return "The deceased: " + str(result)

for indi in families:
    print(test_child_max(indi, families))
    print(test_quintuplets(indi, families))
print(test_the_deceased(individuals))