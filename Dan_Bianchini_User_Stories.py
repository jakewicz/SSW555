from datetime import datetime
# ========================== SPRINT 1 ============================

# US 02
# author DB
# returns true if individual was born after they were married
def US02_born_after_married(indi, individuals):
    if individuals[indi]['MARR_AGE'] != 'N/A':
        if individuals[indi]['MARR_AGE'] < 0:
            return True
    return False

# US 03
# author DB
# returns true if individual died before they were born
def US03_death_before_birth(indi, individuals):
    if individuals[indi]['DEAT'] == 'N/A':
        return False
    death = datetime.strptime(individuals[indi]['DEAT'], '%d %b %Y')
    birth = datetime.strptime(individuals[indi]['BIRT'], '%d %b %Y')
    diff = int((death - birth).days / 365)
    if diff < 0:
        return True
    return False

# ========================== SPRINT 2 ============================

# US 08
# author DB
# returns true if individual was born before his/her parents were married
def US08_born_before_parents_married(indi, individuals, families):
    birth = datetime.strptime(individuals[indi]['BIRT'], '%d %b %Y')
    if individuals[indi]['FAMC'] not in families.keys():
        return False
    marriage = datetime.strptime(families[individuals[indi]['FAMC']]['MARR'], '%d %b %Y')
    if birth < marriage:
        return True
    return False

# US 12
# author DB
# returns true if parents are too old (80 years older for father, 60 years for mother)
def US12_parents_too_old(indi, individuals, families):
    birth = datetime.strptime(individuals[indi]['BIRT'], '%d %b %Y')
    if individuals[indi]['FAMC'] not in families.keys():
        return False
    father_birth = datetime.strptime(individuals[families[individuals[indi]['FAMC']]['HUSB']]['BIRT'], '%d %b %Y')
    mother_birth = datetime.strptime(individuals[families[individuals[indi]['FAMC']]['WIFE']]['BIRT'], '%d %b %Y')
    father_diff = int((birth-father_birth).days / 365)
    mother_diff = int((birth-mother_birth).days / 365)
    if father_diff >= 80:
        return True
    if mother_diff >= 60:
        return True
    return False

# ========================== SPRINT 3 ============================

# US 31
# author DB
# lists living individuals over 30 who have never married
def US31_list_living_single(individuals):
    print("\nUS 31: List of every individual over 30 who has never married:")
    for indi in individuals:
        if individuals[indi]['FAMS'] == 'N/A' and individuals[indi]['AGE'] > 30:
            print(individuals[indi]['NAME'])

# US 32
# author DB
# interpretation A: list all sets of tuplets (twins, triplets, etc.)
def US32_list_multiple_births(individuals, families):
    print("\nUS 32: list multiple births:")
    for fam in families:
        birthdays = {}
        if families[fam]['CHIL'] == 'N/A':
            continue
        if len(families[fam]['CHIL']) > 1:
            for child in families[fam]['CHIL']:
                if child in birthdays.values():
                    continue
                birth = datetime.strptime(individuals[child]['BIRT'], '%d %b %Y')
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
                print(birth.date(), end =":   ")
                for child in birthdays[birth]:
                    print(individuals[child]['NAME'], end =", ")
                print()

# ========================== SPRINT 4 ============================

# US 09
# author DB
# returns true if individual was born after the death of his/her parents
def US09_born_after_parents_death(indi, individuals, families):
    birth = datetime.strptime(individuals[indi]['BIRT'], '%d %b %Y')
    if individuals[indi]['FAMC'] not in families.keys():
        return False
    father_id = families[individuals[indi]['FAMC']]['HUSB']
    mother_id = families[individuals[indi]['FAMC']]['WIFE']
    if individuals[father_id]['DEAT'] != "N/A":
        father_death = datetime.strptime(individuals[father_id]['DEAT'], '%d %b %Y')
        if father_death < birth:
            return True
    if individuals[mother_id]['DEAT'] != "N/A":
        mother_death = datetime.strptime(individuals[mother_id]['DEAT'], '%d %b %Y')
        if mother_death < birth:
            return True
    return False

# US 23
# author DB
# lists individual IDs that have the same name and birthday
def US23_unique_name_and_birthday(individuals):
    data = {}
    for indi in individuals.keys():
        info = (individuals[indi]['NAME'], individuals[indi]['BIRT'])
        if info not in data.keys():
            data[info] = [indi]
        else:
            data[info].append(indi)
    for x in data.keys():
        if len(data[x]) < 2:
            continue
        print("\nERROR US23: multiple individuals with name ", x[0], " and birthday ", x[1], ", IDs:")
        for indi in data[x]:
            print(indi)