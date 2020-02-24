#Sprint 1


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