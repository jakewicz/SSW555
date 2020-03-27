from datetime import date, datetime

#returns true if dead
def dead(indi, individuals): 
    if('DEAT' in individuals[indi].keys()):
        return True
    else:
        return False

#age they died at
def died_at(indi, individuals):
    if individuals[indi]['DEAT'] != 'N/A':
        death = individuals[indi]['DEAT']
        birth = individuals[indi]['BIRT']
        death_age = (death - birth).days/365
        return(death_age)

#finds age and adds to individual dict
def find_age(individuals): 
    today = datetime.now()
    for indi in individuals:
        if('BIRT' in individuals[indi].keys()):
            #finding age if still alive
            if(dead(indi, individuals) == False):
                birth = individuals[indi]['BIRT']
                individuals[indi]['AGE'] = (today - birth).days/365
            else:
                individuals[indi]['AGE'] = died_at(indi, individuals)             
    return individuals

#calculates marriage and divorce ages and adds to individuals dictionary
#also adds "N/A" for values if not applicable
def div_marr_ages(families, individuals):
    for indi in families:
        marriage =  families[indi]['MARR']
        if ('DIV' in families[indi].keys()):
            divorced = families[indi]['DIV']
            individuals[families[indi]['HUSB']]['DIV_AGE'] = (divorced - individuals[families[indi]['HUSB']]['BIRT']).days/365
            individuals[families[indi]['WIFE']]['DIV_AGE'] = (divorced - individuals[families[indi]['WIFE']]['BIRT']).days/365

        individuals[families[indi]['HUSB']]['MARR_AGE'] = (marriage - individuals[families[indi]['HUSB']]['BIRT']).days/365
        individuals[families[indi]['WIFE']]['MARR_AGE'] = (marriage - individuals[families[indi]['WIFE']]['BIRT']).days/365
        
        if 'DIV' not in families[indi].keys():
            families[indi]['DIV'] = "N/A"
        if 'CHIL' in families[indi].keys():
            individuals[families[indi]['HUSB']]['CHILD'] = families[indi]['CHIL']
            individuals[families[indi]['WIFE']]['CHILD'] = families[indi]['CHIL'] 
        if 'CHIL' not in families[indi].keys():
            families[indi]['CHIL'] = "N/A"
            individuals[families[indi]['HUSB']]['CHILD'] = "N/A"
            individuals[families[indi]['WIFE']]['CHILD'] = "N/A"
        if 'WIFE' in families[indi].keys():
            individuals[families[indi]['WIFE']]['SPOUSE'] = families[indi]['HUSB']
            families[indi]['Wife Name'] = individuals[families[indi]['WIFE']]['NAME']
        if 'HUSB' in families[indi].keys():
            individuals[families[indi]['HUSB']]['SPOUSE'] = families[indi]['WIFE']
            families[indi]['Husband Name'] = individuals[families[indi]['HUSB']]['NAME']
        
    for indi in individuals:    
        if 'MARR_AGE' not in individuals[indi].keys():
            individuals[indi]['MARR_AGE'] = "N/A"
        if 'DIV_AGE' not in individuals[indi].keys():
            individuals[indi]['DIV_AGE'] = "N/A"
        if 'DEAT' not in individuals[indi].keys():
            individuals[indi]['DEAT'] = "N/A"
            individuals[indi]['ALIVE'] = "True"
        else: individuals[indi]['ALIVE'] = "False"
        if 'CHILD' not in individuals[indi].keys():
            individuals[indi]['CHILD'] = "N/A"
        if 'SPOUSE' not in individuals[indi].keys():
            individuals[indi]['SPOUSE'] = "N/A"
    return(individuals)

#keeping track of ages in dictionaries
def age_bank(families, individuals):
    individuals = find_age(individuals)
    individuals = div_marr_ages(families, individuals)
    return individuals

def handle_date(raw_date):
    month = 0
    months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
    info = raw_date.split(" ")
    for x in range(12):
        if (info[1] == months[x]):
            month = x + 1
    if (month == 0):
        print("ERROR: invalid month ", info[1])
        return
    return datetime(int(info[2]), month, int(info[0]))