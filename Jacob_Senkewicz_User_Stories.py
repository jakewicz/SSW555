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
def US30_list_living_married(individuals):
    for indi in individuals:
        if individuals[indi]['FAMS'] != 'N/A' and individuals[indi]['DEAT'] == 'N/A':
            print(individuals[indi]['NAME'])
#_____________________________________________________________________________________________________________________________
