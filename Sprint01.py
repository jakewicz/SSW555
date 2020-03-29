from UsefulFunctions import *

#author JC
#checks to see if person is less than 150 years old
def US07_check150(indi, individuals):
    if individuals[indi]['DEAT'] is int:
        if(died_at(indi, individuals) >= 150):
            return "Error: Too Old"
    if(individuals[indi]['AGE'] >= 150):
        return "Error: Too Old"

#author JC
#checks if death date is after divorce date
def US06_divorce_before_death(indi, individuals):
    if individuals[indi]['DIV_AGE'] != 'N/A':
        if(individuals[indi]['DIV_AGE'] > individuals[indi]['AGE']):
            return "Error: cannot get divorced after death"
        else:
            return "valid"

#checks if indi got marriede befgore age of 14
def US10_young_marriage(indi, individuals):
    if individuals[indi]['MARR_AGE'] != 'N/A' and individuals[indi]['MARR_AGE'] != 'INVALID':
        if(individuals[indi]['MARR_AGE'] <= 14):
            return "Error: Too young to get married, must be at least 14 years old"

#checks if all dates are before current date
def US01_check_current_date(indi, individuals):
    if 'BIRT' in individuals[indi].keys() and individuals[indi]['BIRT'] != 'N/A':
        if (datetime.strptime(individuals[indi]['BIRT'], '%d %b %Y') > datetime.now()):
            return "Error: date is after the current date"
    if 'DEAT' in individuals[indi].keys() and individuals[indi]['DEAT'] != 'N/A':
        if (datetime.strptime(individuals[indi]['DEAT'], '%d %b %Y') > datetime.now()):
            return "Error: date is after the current date"
    if 'MARR' in individuals[indi].keys() and individuals[indi]['MARR'] != 'N/A':
        if (datetime.strptime(individuals[indi]['MARR'], '%d %b %Y') > datetime.now()):
            return "Error: date is after the current date"
    if 'DIV' in individuals[indi].keys() and individuals[indi]['DIV '] != 'N/A':
        if (datetime.strptime(individuals[indi]['DIV'], '%d %b %Y') > datetime.now()):
            return "Error: date is after the current date"
            
#author GM
#checks if marriage date is before death date
def US05_married_before_death(indi, individuals):
    if individuals[indi]['MARR_AGE'] != 'N/A' and individuals[indi]['MARR_AGE'] != 'INVALID':
        if(individuals[indi]['MARR_AGE'] > individuals[indi]['AGE']):
            return "Error: cannot get married after death"
        else:
            return "valid"

#author GM
#checks if marriage date is before divorce date
def US04_married_before_div(indi, individuals):
    if individuals[indi]['MARR_AGE'] != 'N/A' and individuals[indi]['MARR_AGE'] != 'INVALID':
        if individuals[indi]['DIV_AGE'] != 'N/A' and individuals[indi]['DIV_AGE'] != 'INVALID':
            if(individuals[indi]['DIV_AGE'] > individuals[indi]['MARR_AGE']):
                return "valid"
            else:
                return "Error: marriage date after divorce date"
