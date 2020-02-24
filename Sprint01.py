from UsefulFunctions import *
from Parser import *

#author DB
#checking if person was born before married
def marriage_after_birth(indi, individuals):
    if(individuals[indi]['MARR_AGE'] < 0):
        individuals[indi]['MARR_AGE'] = "INVALID"
        return("ERROR: married before born")
    else:
        return("Marriage date valid")

#author DB
#birth before death
def birth_before_death(indi, individuals):
    if(individuals[indi]['AGE'] >= 0):
        return "valid"
    else:
        return "Error: death date cannot be before birth date"

#author JC
#checks to see if person is less than 150 years old
def check150(indi, individuals):
    if(died_at(indi, individuals) >= 150):
        return "Error: Too Old"
    if(individuals[indi]['AGE'] >= 150):
        return "valid"

#author JC
#checks if death date is after divorce date
def divorce_before_death(indi, individuals):
    if(individuals[indi]['DIV_AGE'] > individuals[indi]['AGE']):
        return "Error: cannot get divorced after death"
    else:
        return "valid"

#author JS
#checks if indi got marriede befgore age of 14
def young_marriage(indi, individuals):
    if(individuals[indi]['MARR_AGE'] <= 14):
        return "Error: Too young to get married, must be at least 14 years old"

#author GM
#checks if marriage date is befgore death date
def married_before_death(indi, individuals):
    if(individuals[indi]['MARR_AGE'] > individuals[indi]['AGE']):
        return "Error: cannot get married after death"
    else:
        return "valid"

#author GM
#checks if marriage date is befgore divorce date
def married_before_div(indi, individuals):
    if(individuals[indi]['DIV_AGE'] > individuals[indi]['MARR_AGE']):
        return "valid"
    else:
        return "Error: marriage date after divorce date"

#We Need these two lines to read in file and add to ages
#Adds to age dictionary
individuals, families =read_file('./test.ged')
individuals = UsefulFunctions.age_bank(families, individuals)