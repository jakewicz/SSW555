# This is our test file
from Sprint01 import *


def test_marriage_after_birth(indi, individuals):
    if(marriage_after_birth(indi, individuals) == "ERROR: married before born"):
        print("ERROR: US02", indi, ": married before born")
    #if (marriage_after_birth(indi, individuals) == "Marriage date valid" or marriage_after_birth(indi, individuals) == "no marriage date"):
        #return("marriage is after birth test passed")

def test_birth_before_death(indi, individuals):
    #if(birth_before_death(indi, individuals) =="valid"):
        #return("birth is before death test passed")
    if(birth_before_death(indi, individuals)== "Error: death date cannot be before birth date"):
        print("ERROR: US03", indi,  ": death date cannot be before birth date")

def test_check150(indi, individual):
    if (check150(indi, individual) == "Error: Too Old"):
        print("ERROR: US07", indi, ": Individual is over 150 years old ")
    #if (check150(indi, individual) == "valid"):
        #return ("under 150 test passed")

def test_divorce_before_death(indi, individuals):
    if(divorce_before_death(indi, individuals) == "Error: cannot get divorced after death"):
        print("ERROR: US06", indi, ": cannot get divorced after death")
    #if(divorce_before_death(indi, individuals)=="valid"):
        #return("divorce before death-test passed")

def test_young_marriage(indi, individuals):
    if (young_marriage(indi, individuals) == "Error: Too young to get married, must be at least 14 years old"):
        print("ERROR: US10", indi, ": Too young to get married, must be at least 14 years old")
    #else:
        #return "young marriage test passed"

def test_check_current_date(indi, individuals):
    if (check_current_date(indi, individuals) == "Error: date is after the current date"):
        print("ERROR: US01", indi, ": date is after the current date")

def test_married_before_death(indi, individuals):
    if (married_before_death(indi, individuals) == "Error: cannot get married after death"):
        print("ERROR: US05", indi, ": cannot get married after death")
    #if (married_before_death(indi, individuals) =="valid"):
        #return "marriage before death test passed"

def test_married_before_div(indi, individuals):
    if (married_before_div(indi, individuals) == "Error: marriage date after divorce date"):
        print( "ERROR: US04", indi, ": marriage date after divorce date")
    #if (married_before_div(indi, individuals) =="valid"):
        #return "marriage before divorce test passed"

for indi in individuals:

    test_marriage_after_birth(indi, individuals)
    test_birth_before_death(indi, individuals)
    test_check150(indi, individuals)
    test_divorce_before_death(indi, individuals)
    test_young_marriage(indi, individuals)
    test_check_current_date(indi, individuals)
    test_married_before_death(indi, individuals)
    test_married_before_div(indi, individuals)
