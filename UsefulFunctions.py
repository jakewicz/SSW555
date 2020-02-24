from datetime import date, datetime

#returns true if dead
def dead(indi, individuals): 
    if('DEAT' in individuals[indi].keys()):
        return True
    else:
        return False

#age they died at
def died_at(indi, individuals):
    if('DEAT' in individuals[indi].keys()):
        death = datetime.strptime(individuals[indi]['DEAT'], '%d %b %Y')
        individuals[indi]['DEAT'] = datetime.strptime(individuals[indi]['DEAT'], '%d %b %Y')
        birth = datetime.strptime(individuals[indi]['BIRT'], '%d %b %Y')
        individuals[indi]['BIRT'] = datetime.strptime(individuals[indi]['BIRT'], '%d %b %Y')
        death_age = int((death-birth).days/365)
    return(death_age)

#finds age and adds to individual dict
def find_age(individuals): 
    today = datetime.now()
    for indi in individuals:
        if('BIRT' in individuals[indi].keys()):
            #finding age if still alive
            if(dead(indi, individuals) == False):
                birth =  datetime.strptime(individuals[indi]['BIRT'], '%d %b %Y')
                individuals[indi]['BIRT'] = datetime.strptime(individuals[indi]['BIRT'], '%d %b %Y')
                individuals[indi]['AGE'] = int((today - birth).days/365)
            else:
                age = died_at(indi, individuals)
                individuals[indi]['AGE'] = age
                #checking if birthdaqy is after death
                if(age < 0):
                    print("ERROR: invalid death date")
                else:
                    individuals[indi]['AGE']= age
    return individuals

#calculates marriage and divorce ages and adds to individuals dictionary
def div_marr_ages(families, individuals):
    for indi in families:
        marriage =  datetime.strptime(families[indi]['MARR'], '%d %b %Y')
        if ('DIV' in individuals[families[indi]['HUSB']].keys() or 'DIV' in individuals[families[indi]['WIFE']].keys()):
            divorced = datetime.strptime(families[indi]['DIV'], '%d %b %Y')
            individuals[families[indi]['HUSB']]['DIV_AGE'] = int((divorced-individuals[families[indi]['HUSB']]['BIRT']).days/365)
            individuals[families[indi]['WIFE']]['DIV_AGE'] = int((divorced-individuals[families[indi]['WIFE']]['BIRT']).days/365)

        individuals[families[indi]['HUSB']]['MARR_AGE'] = int((marriage-individuals[families[indi]['HUSB']]['BIRT']).days/365)
        individuals[families[indi]['WIFE']]['MARR_AGE'] = int((marriage-individuals[families[indi]['WIFE']]['BIRT']).days/365)
    return(individuals)

#keeping track of ages in dictionaries
def age_bank(families, individuals):
    individuals = find_age(individuals)
    individuals = div_marr_ages(families, individuals)
    return individuals