#Sprint 02
#_____________________________________________US16____________________________________________________________________________
#US 16
#Author JS
#Prints all male last names
def US16_get_last_names(indi,individuals):
    names = []
    if individuals[indi]['SEX'] == "M":
        line = individuals["NAME"]
        line = line.strip()
        parse = line.split(' ')
        firstName = parse[0]
        lastName = parse[1]
        lastName = lastName.replace("/", "", 2)
        names.append(lastName)
        print(lastName)
    return names
#____________________________________________US18______________________________________________________________________________
def US18_siblings_should_not_marry(individuals, families):
    for indi in individuals:
        if individuals[indi]['FAMC'] != 'N/A':
            if individuals[indi]['SPOUSE'] != 'N/A':
                family_code = individuals[indi]['FAMC']
                spouse = individuals[indi]['SPOUSE']
                spouse_family_code = individuals[spouse]['FAMC']
                if spouse_family_code == family_code:
                    print("ERROR US 18: You cannot marry your siblings.")
#_____________________________________________________________________________________________________________________________
