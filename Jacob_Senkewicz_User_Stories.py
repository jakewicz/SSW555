#Sprint 02
#_____________________________________________US16____________________________________________________________________________
#US 16
#Author JS
#Prints all male last names
def US16_get_last_names(individuals):
    names = []
    for indi in individuals:
        if individuals[indi]['SEX'] == "M":
            line = individuals[indi]["NAME"]
            line = line.strip()
            parse = line.split(' ')
            firstName = parse[0]
            lastName = parse[1]
            lastName = lastName.replace("/", "", 2)
            names.append(lastName)
    print(names)
    return names
#____________________________________________US30______________________________________________________________________________
def US30_list_living_married(individuals):
    for indi in individuals:
        if individuals[indi]['FAMS'] != 'N/A' and individuals[indi]['DEAT'] == 'N/A':
            print(individuals[indi]['NAME'])

            
 #_____________________________________________________________________________________________________________________________
#Sprint 03
def US17_dont_marry_children(indi, individuals, families):
    if individuals[indi]['FAMS'] == 'N/A':
        return False
    if len(individuals[indi]['FAMS']) < 2:
        return False
    for fam in individuals[indi]['FAMS']:
        if fam not in families.keys():
            continue
        if families[fam]['CHIL'] == 'N/A':
            continue
        for child in families[fam]['CHIL']:
            if individuals[child]['FAMS'] == 'N/A':
                continue
            for child_fam in individuals[child]['FAMS']:
                if child_fam in individuals[indi]['FAMS']:
                    return True
    return False

#_________________________________________________________________________________________________________________________________
def US18_siblings_should_not_marry(indi, individuals, families):
    if individuals[indi]['FAMS'] == 'N/A':
        return False
    for indi in individuals:
        if individuals[indi]['FAMC'] not in families.keys():
            return False
        for child in families[individuals[indi]['FAMC']]['CHIL']:
            if child == indi:
                continue
            if individuals[child]['FAMS'] != 'N/A':
                for fam in individuals[child]['FAMS']:
                    if fam in individuals[indi]['FAMS']:
                        return True
    return False
