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
        death = datetime.strptime(individuals[indi]['DEAT'], '%d %b %Y')
        birth = datetime.strptime(individuals[indi]['BIRT'], '%d %b %Y')
        death_age = int((death-(birth)).days/365)
        return(int(death_age))

#finds age and adds to individual dict
def find_age(individuals): 
    today = datetime.now()
    for indi in individuals:
        if('BIRT' in individuals[indi].keys()):
            #finding age if still alive
            if(dead(indi, individuals) == False):
                birth =  datetime.strptime(individuals[indi]['BIRT'], '%d %b %Y') 
                #individuals[indi]['BIRT'] = datetime.strptime(individuals[indi]['BIRT'], '%d %b %Y')#not working
                individuals[indi]['AGE'] = int((today - birth).days/365)
            else:
                age = died_at(indi, individuals)
                individuals[indi]['AGE'] = age
    return individuals

#calculates marriage and divorce ages and adds to individuals dictionary
def div_marr_ages(families, individuals):
    for indi in families:
        marriage =  datetime.strptime(families[indi]['MARR'], '%d %b %Y')
        if ('DIV' in families[indi].keys()):
            divorced = datetime.strptime(families[indi]['DIV'], '%d %b %Y')
            individuals[families[indi]['HUSB']]['DIV_AGE'] = int((divorced-datetime.strptime(individuals[families[indi]['HUSB']]['BIRT'], '%d %b %Y')).days/365)
            individuals[families[indi]['WIFE']]['DIV_AGE'] = int((divorced-datetime.strptime(individuals[families[indi]['WIFE']]['BIRT'], '%d %b %Y')).days/365)

        individuals[families[indi]['HUSB']]['MARR_AGE'] = int((marriage-datetime.strptime(individuals[families[indi]['HUSB']]['BIRT'], '%d %b %Y')).days/365)
        individuals[families[indi]['WIFE']]['MARR_AGE'] = int((marriage-datetime.strptime(individuals[families[indi]['WIFE']]['BIRT'], '%d %b %Y')).days/365)
        
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
        if 'FAMC' not in individuals[indi].keys():
            individuals[indi]['FAMC'] = "N/A"
        if 'FAMS' not in individuals[indi].keys():
            individuals[indi]['FAMS'] = "N/A"
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