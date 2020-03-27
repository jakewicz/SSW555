# ========================== SPRINT 1 ============================

# US 02
# author DB
# returns true if individual was born after they were married
def US02_born_after_married(indi, individuals):
    if individuals[indi]['MARR_AGE'] != 'N/A':
        if individuals[indi]['MARR_AGE'] < 0:
            individuals[indi]['MARR_AGE'] = "INVALID"
            print("ERROR US02: ", individuals[indi]['NAME'], " born after being married")
            return True
    return False

# US 03
# author DB
# returns true if individual died before they were born
def US03_death_before_birth(indi, individuals):
    if individuals[indi]['DEAT'] == 'N/A':
        return False
    diff = int((individuals[indi]['DEAT'] - individuals[indi]['BIRT']).days / 365)
    if diff < 0:
        print("ERROR US03: ", individuals[indi]['NAME'], " died before birth")
        return True
    return False

# ========================== SPRINT 2 ============================

# US 08
# author DB
# returns true if individual was born before his/her parents were married
def US08_born_before_parents_married(indi, individuals, families):
    birth = individuals[indi]['BIRT']
    if individuals[indi]['FAMC'] == 'N/A':
        return False
    if individuals[indi]['FAMC'] not in families.keys():
        return False
    marriage = families[individuals[indi]['FAMC']]['MARR']
    if birth < marriage:
        print("ERROR US08: ", individuals[indi]['NAME'], " born before parents married")
        return True
    return False

# US 12
# author DB
# returns true if parents are too old (80 years older for father, 60 years for mother)
def US12_parents_too_old(indi, individuals, families):
    birth = individuals[indi]['BIRT']
    if individuals[indi]['FAMC'] == 'N/A':
        return False
    if individuals[indi]['FAMC'] not in families.keys():
        return False
    father_birth = individuals[families[individuals[indi]['FAMC']]['HUSB']]['BIRT']
    mother_birth = individuals[families[individuals[indi]['FAMC']]['WIFE']]['BIRT']
    father_diff = int((father_birth - birth).days / 365)
    mother_diff = int((mother_birth - birth).days / 365)
    if father_diff >= 80:
        print("ERROR US12: father of ", individuals[indi]['NAME'], " is 80 years or more older than ", individuals[indi]['NAME'])
        return True
    if mother_diff >= 60:
        print("ERROR US12: mother of ", individuals[indi]['NAME'], " is 60 years or more older than ", individuals[indi]['NAME'])
        return True
    return False

# ========================== SPRINT 3 ============================

# US 31
# author DB
# lists living individuals over 30 who have never married
def US31_list_living_single(individuals):
    print("US 31: List of every individual over 30 who has never married:")
    for indi in individuals:
        if individuals[indi]['FAMS'] == 'N/A' and individuals[indi]['AGE'] > 30:
            print(individuals[indi]['NAME'])

# US 32
# author DB
# interpretation A: list all sets of tuplets (twins, triplets, etc.)
def US32_list_multiple_births(individuals, families):
    print("US 32: list multiple births:")
    for fam in families:
        birthdays = {}
        if families[fam]['CHIL'] == 'N/A':
            continue
        if len(families[fam]['CHIL']) > 1:
            for child in families[fam]['CHIL']:
                if child in birthdays.values():
                    continue
                birth = individuals[child]['BIRT']
                done_flag = False
                for bday in birthdays.keys():
                    diff = (bday - birth).days
                    if diff >= -1 and diff < 1:
                        birthdays[bday].append(child)
                        done_flag = True
                        break
                if done_flag:
                    continue
                birthdays[birth] = [child]
                
        for birth in birthdays:
            if len(birthdays[birth]) > 1:
                for child in birthdays[birth]:
                    print(individuals[child]['NAME'], " (", individuals[child]['BIRT'], end ="), ")
                print()
