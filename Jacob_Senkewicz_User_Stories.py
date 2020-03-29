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
#_____________________________________________US17___________________________________________________________________________
#US 17
#author JS
#Alerts when an individual marries child
def US17_dont_marry_children(families):
    fam = families[indi]
    marryChild = []
    for fam in families:
        if "CHIL" in families[fam].keys():
            for child in families[fam]["CHIL"]:
                if child == families[fam]["HUSB"]:
                    print ("ERROR US17: You cannot marry your children!")    
                    marryChild.append("ERROR US17: You cannot marry your children!")
                if child == families[fam]["WIFE"]:
                    print ("ERROR US17: You cannot marry your children!")
                    marryChild.append("ERROR US17: You cannot marry your children!")
                else:
                    continue
    return marryChild
#_____________________________________________________________________________________________________________________________
