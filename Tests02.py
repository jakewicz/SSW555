# This is our test file
from Sprint02 import *

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

