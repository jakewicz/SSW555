# This is our test file
from Sprint02 import *
from Sprint01 import *
from Sprint03 import *
from Dan_Bianchini_User_Stories import *

#sprint 1 tests
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

#start sprint 2 tests
def US15_test_child_max(indi, families):
    if (US15_child_max(indi, families) == "ERROR: too many kids"):
        print( "ERROR: US15", indi, ": family has over 15 children")

def US14_test_quin(indi, families):
    if (US14_quintuplets(indi, families) == "ERROR: more than 5 kids born at once"):
        print( "ERROR: US14", indi, ": family has more than 5 children born at the same time")

#US27: Age is tested in our dictionary and is printed with every individual

def US08_test_born_before_marr(indi, individuals, families):
    US08_born_before_parents_married(indi, individuals, families)

def US12_test_parents_too_old(indi, individuals, families):
    US12_parents_too_old(indi, individuals, families)

#tests for sprint 3
def US21_test_gender(indi, families, individuals):
    if (US21_correct_gender(indi, families, individuals) == 'ERROR: US21 wrong gender for role'):
        print( "ERROR: US21", indi, ": husband or wife is the wrong gender for that role")

def US34_test_age_diff(indi, individuals):
    if (US34_age_difference(indi, individuals) == 'ERROR: US34 large age difference in married couple'):
        print( "ERROR: US34", indi, ": age difference too big, one partner was twice the age of the other when married")

def US31_test(individuals):
    US31_list_living_single(individuals)

def US32_test(individuals, families):
    US32_list_multiple_births(individuals, families)

def US33_test(indi, individuals, families):
    US33_the_orphans(indi, individuals, families)

def US22_test(indi, individuals):
    US22_Unique_IDs(indi, individuals)

for indi in individuals:
    US01_test_check_current_date(indi, individuals)
    US02_test_marriage_after_birth(indi, individuals)
    US03_test_birth_before_death(indi, individuals)
    US04_test_married_before_div(indi, individuals)
    US05_test_married_before_death(indi, individuals)
    US06_test_divorce_before_death(indi, individuals)
    US07_test_check150(indi, individuals)
    US10_test_young_marriage(indi, individuals)
    US34_test_age_diff(indi, individuals)
    US08_test_born_before_marr(indi, individuals, families)
    US12_test_parents_too_old(indi, individuals, families)
for indi in families:
    US14_test_quin(indi, families)
    US15_test_child_max(indi, families)
    US21_test_gender(indi, families, individuals)
US29_the_deceased(individuals)
US31_list_living_single(individuals)
US32_list_multiple_births(individuals, families)
US33_the_orphans(indi, individuals, families)
