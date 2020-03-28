from UsefulFunctions import *
from Parser import *
from collections import defaultdict

#US 34
#author GM
#list large age differences (older spouse is twice the age of younger)
def US34_age_difference(indi, individuals):
    if individuals[indi]['SPOUSE'] != 'N/A':
        if individuals[indi]['MARR_AGE'] != 'INVALID' and individuals[individuals[indi]['SPOUSE']]['MARR_AGE'] != 'INVALID':
            age1 = individuals[indi]['MARR_AGE']
            age2 = individuals[individuals[indi]['SPOUSE']]['MARR_AGE']
            if age1 >= age1*2:
                return('ERROR: US34 large age difference in married couple')
            elif age2 >= age1*2:
                return('ERROR: US34 large age difference in married couple')

#US 21
#author GM
#correct gender for role
def US21_correct_gender(indi, families, individuals):
    if 'WIFE' in families[indi].keys():
        if individuals[families[indi]['WIFE']]['SEX'] != 'F':
            return('ERROR: US21 wrong gender for role')
    if 'HUSB' in families[indi].keys():
        if individuals[families[indi]['HUSB']]['SEX'] != 'M':
            return('ERROR: US21 wrong gender for role')

#US 33
#author JC
#List Orphans
def US33_the_orphans(indi, families, individuals):
    if 20 == "WIFE":
        print("hello")

#US 22
#author JC
#Unique IDS
def US22_Unique_IDs(indi, individuals):
    holder = defaultdict(int)
    for indi in individuals:
        print(individuals[indi]['ID'])
        holder[individuals[indi]['ID']] += 1 
    for val in holder:
        if holder[val] > 1:
            return ("Error: US22 Not all individuals have a unique ID" + val)