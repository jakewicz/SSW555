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
#____________________________________________US30______________________________________________________________________________
def US30_list_living_married(individuals):
    for indi in individuals:
        if individuals[indi]['FAMS'] != 'N/A' and individuals[indi]['DEAT'] == 'N/A':
            print(individuals[indi]['NAME'])

            
 #_____________________________________________________________________________________________________________________________
#Sprint 03
def US17_dont_marry_children(families):
    marryChild = []
    for fam in families:
        if "CHIL" in families[fam]:
            for child in families[fam]["CHIL"]:
                if child == families[fam]["HUSB"]:
                    print (families[fam]["HUSB"])    
                    marryChild.append("ERROR US17: You cannot marry your children!")
                elif child == families[fam]["WIFE"]:
                    print ("ERROR US17: You cannot marry your children!")
                    marryChild.append(families[fam]["WIFE"])
                else:
                    continue
    return marryChild
#_________________________________________________________________________________________________________________________________
def US18_siblings_should_not_marry(individuals,families):
    for fam in families:
        dad = families[fam]['HUSB']
        mom = families[fam]["WIFE"]
        dad_fam = individuals[dad]['FAMC']
        mom_fam = individuals[mom]['FAMC']
        if mom_fam == dad_fam:
            print("ERROR US18: You cannot marry your siblings, that is incest.")
    return dad
