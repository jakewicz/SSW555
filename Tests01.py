# This is our test file

from Sprint01 import *


def test_marriage_after_birth(indi, individuals):
    if(marriage_after_birth(indi, individuals) == "ERROR: married before born" or marriage_after_birth(indi, individuals) == "Marriage date valid"):
        return("marriage is after birth test passed")

def test_birth_before_death(individuals):
    for indi in individuals:
        if('BIRT' in individuals[indi].keys()):
            if('DEAT' in individuals[indi].keys()):
                if('AGE' in individuals[indi].keys()):
                    if(individuals[indi]['AGE'] < 0):
                        yield(indi+"ERROR: birth before death")
                    else:
                        yield(indi+"PASS Birth Before Death")

def test_check150(indi, Individual):
    if (check150(indi, Individual) == "Error: Too Old") or (check150(indi, Individual) == "valid"):
        return "Individual is under 150 years old - Test passed"

def test_divorce_before_death(indi, individuals):
    if(divorce_before_death(indi, individuals) == "Error: cannot get divorced after death" or divorce_before_death(indi, individuals)=="valid"):
        return("divorce before death-test passed")

def test_young_marriage(indi, individuals):
    if (young_marriage(indi, individuals) == "Error: Too young to get married, must be at least 14 years old"):
        return "marrige after the age of 14 test passed"

def test_check_current_date(indi, individuals):
    if (check_current_date(indi, individuals) == "Error: date is after the current date"):
        return "check current date test passed"

def test_married_before_death(indi, individuals):
    if (married_before_death(indi, individuals) == "Error: cannot get married after death" or married_before_death(indi, individuals) =="valid"):
        return "marriage before death test passed"

def test_married_before_div(indi, individuals):
    if (married_before_div(indi, individuals) == "Error: marriage date after divorce date" or married_before_div(indi, individuals) =="valid"):
        return "marriage before divorce test passed"



