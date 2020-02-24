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

def div_age():
    pass
#kc sprint 1 birth before marrage | birth before death

def check_birth_before_marr(key, individuals):
    if(individuals[key]['MARR_AGE'] < 0):
        individuals[key]['MARR_AGE'] = "INVALID"
        return("ERROR: Invalid Marrage date, married before birth")
    else:
        return("Marrage date valid")

def store_ages(families, individuals):
    individuals = calc_ages(individuals)
    individuals = marr_and_div_ages(families, individuals)
    return individuals

def less_than_one_fifty(key, individuals):
    # Ticket US07 - Death should be less than 150 years after 
    # birth for dead individuals, and current date should be less 
    # than 150 years after birth for all living individuals
    if(death_age(key, individuals) >= 150):
        return "Death Age Invalid"
    if(get_age(key, individuals) >= 150):
        return "Current Age Invalid"
    
def marrige_after_fourteen(key,families, individuals):
    # Ticket US10 - Marriage should be at least 14 years after birth 
    # of both spouses (parents must be at least 14 years old)
    if(individuals[families[key]['HUSB']]['MARR_AGE'] <= 14) or (individuals[families[key]['WIFE']]['MARR_AGE'] <= 14):
        return "Marrige under the age of 14 is invalid"


def mar_b4_death(key, individuals):
    if(individuals[key]['MARR_AGE'] > individuals[key]['AGE']):
        return False
    else:
        return True


def div_b4_death(key, individuals):
    if(individuals[key]['DIV_AGE'] > individuals[key]['AGE']):
        return False
    else:
        return True