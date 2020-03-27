from UsefulFunctions import *
from Parser import *

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