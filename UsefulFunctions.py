from datetime import timedelta, datetime

def calc_ages(individuals):
    today = datetime.now()
    for key in individuals:
        if('BIRT' in individuals[key].keys()):
            if(is_dead(key, individuals) == False):
                bday = datetime.strptime(individuals[key]['BIRT'], '%d %b %Y')
                individuals[key]['BIRT'] = datetime.strptime(individuals[key]['BIRT'], '%d %b %Y')
                individuals[key]['AGE'] = int((today - bday).days/365.2425)
            else:
                #if dead age is their last living age individuals[key]['AGE']
                age = death_age(key, individuals)
                individuals[key]['AGE'] = age
                if(age < 0): #death before birth
                    print("ERROR: Invalid death date, death before birth")
                else:
                    individuals[key]['AGE']= age
    return individuals

def is_dead(key, individuals): #by person
    if('DEAT' in individuals[key].keys()):
        return True
    else:
        return False

def get_age(key, individuals): #by person
    #not totally needed but it could make life easy maybe.  can also just do a ditct call
    return (individuals[key]['AGE'])


def death_age(key, individuals): #by person
    if('DEAT' in individuals[key].keys()):
        # print(individuals[key]['DEAT'])
        # print(key, type(individuals[key]['DEAT']), individuals[key]['DEAT'])
        if(type(individuals[key]['DEAT']) == str):
            dday = datetime.strptime(individuals[key]['DEAT'], '%d %b %Y')
            individuals[key]['DEAT'] = datetime.strptime(individuals[key]['DEAT'], '%d %b %Y')
            bday = datetime.strptime(individuals[key]['BIRT'], '%d %b %Y')
            individuals[key]['BIRT'] = datetime.strptime(individuals[key]['BIRT'], '%d %b %Y')
            d_age = int((dday-bday).days/365.2425)
        else:
            d_age = int(
                (individuals[key]['DEAT'] - individuals[key]['BIRT']).days/365.2425)
        return(d_age)
        

def marr_and_div_ages(families, individuals): #runs on whole dictionary
    for key in families: 
        marr_date = datetime.strptime(families[key]['MARR'], '%d %b %Y')   
        div_date = datetime.strptime(families[key]['DIV'], '%d %b %Y')
        #print(marr_date)

        individuals[families[key]['HUSB']]['MARR_AGE'] = int((marr_date-individuals[families[key]['HUSB']]['BIRT']).days/365.2425)
        individuals[families[key]['HUSB']]['DIV_AGE'] = int((div_date-individuals[families[key]['HUSB']]['BIRT']).days/365.2425)
        individuals[families[key]['WIFE']]['MARR_AGE'] = int((marr_date-individuals[families[key]['WIFE']]['BIRT']).days/365.2425)
        individuals[families[key]['WIFE']]['DIV_AGE'] = int((div_date-individuals[families[key]['WIFE']]['BIRT']).days/365.2425)
    return(individuals)