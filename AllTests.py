# This is our test file
from Sprint02 import *
from Sprint01 import *
from Sprint03 import *
from Sprint04 import *
from Dan_Bianchini_User_Stories import *
from Jacob_Senkewicz_User_Stories import *
import Parser

individuals, families = Parser.read_file("./test.ged")

#sprint 1 tests
def US02_test_born_after_married(indi, individuals):
    if US02_born_after_married(indi, individuals):
        print("ERROR US02: ", individuals[indi]['NAME'], " married before born")

def US03_test_death_before_birth(indi, individuals):
    if US03_death_before_birth(indi, individuals):
        print("ERROR US03: ", individuals[indi]['NAME'],  " death date cannot be before birth date")

def US07_test_check150(indi, individual):
    if (US07_check150(indi, individual) == "Error: Too Old"):
        print("ERROR: US07", individuals[indi]['NAME'], ": Individual is over 150 years old ")

def US06_test_divorce_before_death(indi, individuals):
    if(US06_divorce_before_death(indi, individuals) == "Error: cannot get divorced after death"):
        print("ERROR: US06", individuals[indi]['NAME'], ": cannot get divorced after death")

def US10_test_young_marriage(indi, individuals):
    if (US10_young_marriage(indi, individuals) == "Error: Too young to get married, must be at least 14 years old"):
        print("ERROR: US10", individuals[indi]['NAME'], ": Too young to get married, must be at least 14 years old")

def US01_test_check_current_date(indi, individuals):
    if (US01_check_current_date(indi, individuals) == "Error: date is after the current date"):
        print("ERROR: US01", individuals[indi]['NAME'], ": date is after the current date")

def US05_test_married_before_death(indi, individuals):
    if (US05_married_before_death(indi, individuals) == "Error: cannot get married after death"):
        print("ERROR: US05", individuals[indi]['NAME'], ": cannot get married after death")

def US04_test_married_before_div(indi, individuals):
    if (US04_married_before_div(indi, individuals) == "Error: marriage date after divorce date"):
        print( "ERROR: US04", individuals[indi]['NAME'], ": marriage date after divorce date")

#start sprint 2 tests
def US15_test_child_max(indi, families):
    if (US15_child_max(indi, families) == "ERROR: too many kids"):
        print( "ERROR: US15", indi, ": family has over 15 children")

def US14_test_quin(indi, families, individuals):
    if (US14_quintuplets(indi, families, individuals) == "ERROR: more than 5 kids born at once"):
        print( "ERROR: US14", indi, ": family has more than 5 children born at the same time")

#US27: Age is tested in our dictionary and is printed with every individual

def US08_test_born_before_marr(indi, individuals, families):
    if US08_born_before_parents_married(indi, individuals, families):
        print("ANOMALY US08: ", individuals[indi]['NAME'], " born before parents were married")

def US12_test_parents_too_old(indi, individuals, families):
    if US12_parents_too_old(indi, individuals, families):
        print("ERROR US12: ", individuals[indi]['NAME'], " parent(s) too old")
        
def US16_test_get_last_names(individuals):
    US16_get_last_names(individuals)
        
def US30_test_list_living_married(individuals):
    US30_list_living_married(individuals)

#tests for sprint 3
def US21_test_gender(indi, families, individuals):
    if (US21_correct_gender(indi, families, individuals) == 'ERROR: US21 wrong gender for role'):
        print( "ERROR: US21 in familiy with ID ", indi, ": husband or wife is the wrong gender for that role")

def US34_test_age_diff(indi, individuals):
    if (US34_age_difference(indi, individuals) == 'ERROR: US34 large age difference in married couple'):
        print( "ERROR: US34", individuals[indi]['NAME'], ": age difference too big, one partner was twice the age of the other when married")

def US31_test_list_living_single(individuals):
    US31_list_living_single(individuals)

def US32_test_list_multiple_births(individuals, families):
    US32_list_multiple_births(individuals, families)

def US35_test_recent_births(individuals):
    US35_recent_births(individuals)

def US36_test_recent_deaths(individuals):
    US36_recent_deaths(individuals)    

def US17_test_dont_marry_children(indi, individuals, families):
    if US17_dont_marry_children(indi, individuals, families):
        print("Error US17: ", individuals[indi]['NAME'], " is married to his/her child")

def US18_test_siblings_should_not_marry(indi, individuals, families):
    if US18_siblings_should_not_marry(indi, individuals,families):
        print("ERROR US18: ", individuals[indi]['NAME'], " is married to his/her sibling")


# tests for sprint 4

def US09_test_born_after_parents_death(indi, individuals, families):
    if US09_born_after_parents_death(indi, individuals, families):
        print("ERROR US09: ", individuals[indi]['NAME'], " born after one or more parents died")

def US23_test_unique_name_and_birthday(individuals):
    US23_unique_name_and_birthday(individuals)

def US25_test_unique_first_names(individuals,families):
    US25_unique_first_names(individuals,families)

def US42_test_legit_dates(indi,individuals,families):
    US42_legit_dates(indi,individuals,families)

def US38_test_upcoming_bdays(individuals):
    US38_upcoming_bdays(individuals)

def US39_test_upcoming_anniversary(families, individuals):
    US39_upcoming_anniversary(families, individuals)

def US33_test_list_orphans(families, individuals):
    US33_list_orphans(families, individuals)

def US37_test_recent_survivors(individuals):
    US37_recent_survivors(individuals)

#print out individual and family tables
Parser.print_tables(individuals, families)

# call all test functions properly
for indi in individuals:
    US01_test_check_current_date(indi, individuals)
    US02_test_born_after_married(indi, individuals)
    US03_test_death_before_birth(indi, individuals)
    US04_test_married_before_div(indi, individuals)
    US05_test_married_before_death(indi, individuals)
    US06_test_divorce_before_death(indi, individuals)
    US07_test_check150(indi, individuals)
    US10_test_young_marriage(indi, individuals)
    US34_test_age_diff(indi, individuals)
    US08_test_born_before_marr(indi, individuals, families)
    US12_test_parents_too_old(indi, individuals, families)
    US09_test_born_after_parents_death(indi, individuals, families)
    US17_test_dont_marry_children(indi, individuals, families)
    US18_test_siblings_should_not_marry(indi, individuals, families)

for indi in families:
    US14_test_quin(indi, families, individuals)
    US15_test_child_max(indi, families)
    US21_test_gender(indi, families, individuals)

US29_the_deceased(individuals)
US31_test_list_living_single(individuals)
US32_test_list_multiple_births(individuals, families)
US23_test_unique_name_and_birthday(individuals)
US30_test_list_living_married(individuals)
US35_test_recent_births(individuals)
US36_test_recent_deaths(individuals)
US16_test_get_last_names(individuals)
US25_test_unique_first_names(individuals,families)
US42_test_legit_dates(indi,individuals,families)
US38_test_upcoming_bdays(individuals)
US39_test_upcoming_anniversary(families, individuals)
US33_test_list_orphans(families, individuals)
US37_test_recent_survivors(individuals)