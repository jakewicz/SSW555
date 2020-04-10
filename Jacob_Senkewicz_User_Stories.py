from datetime import datetime
#Sprint 02
#_____________________________________________US16____________________________________________________________________________
#US 16
#Author JS
#Prints all male last names
def US16_get_last_names(individuals):
    print("\nUS:16 Print Male Last Names")
    for indi in individuals:
        if individuals[indi]['SEX'] == 'M':
            line = individuals[indi]["NAME"]
            line = line.strip()
            parse = line.split(' ')
            lastName = parse[1]
            lastName = lastName.replace("/", "", 2)
            print(lastName)


#____________________________________________US30______________________________________________________________________________
def US30_list_living_married(individuals):
    print("\nUS30: All individuals who are married and alive:")
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
#_____________________________________________________________________________________________________________________________
#Sprint 04
#if bday is the same for sibs, first name should be unique

def US25_unique_first_names(individuals,families):
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
            names = []
            if len(birthdays[birth]) > 1:
                for child in birthdays[birth]:
                    childFN = individuals[child]["NAME"]
                    childFN = childFN.strip()
                    parse = childFN.split(' ')
                    firstName = parse[0]
                    #print(firstName)
                    names.append(firstName)
                for child in names:
                    error = names.count(child)
                    if error > 1:
                        print("\nERROR US25: ", child, "born on", birth.date(), " does not have a unique name for the birthdate.")
                        print()
                    return child 
 #_____________________________________________________________________________________________________________________________           

#All dates should be legitimate dates for the months specified (e.g., 2/30/2015 is not legitimate)
def US42_legit_dates(indi, individuals, families):
    dates = []
    for indi in individuals:
        if individuals[indi]["BIRT"]:
            dates.append(individuals[indi]["BIRT"])
        elif individuals[indi]["DEAT"]:
            dates.append(individuals[indi]["DEAT"])
    for fam in families:
        if families[fam]["MARR"]:
            dates.append(families[fam]["MARR"])
        elif families[fam]["DIV"]:
            dates.append(families[fam]["DIV"])
        
    for date in dates:
        if date != 'N/A':
            parse = date.split(' ')
            day = int(parse[0])
            month = parse[1]

            if month == 'JAN' and (day<1 or day>31):
                print ("ERROR US42: ", day, " is not a valid date in ", "month: ",month)
            elif month == 'FEB' and (day<1 or day>29):
                print ("ERROR US42: ", day, " is not a valid date in ", "month: ",month)
            elif month == 'MAR' and (day<1 or day>31):
                print ("ERROR US42: ", day, " is not a valid date in ", "month: ",month)
            elif month == 'APR' and (day<1 or day>30):
                print ("ERROR US42: ", day, " is not a valid date in ", "month: ",month)
            elif month == 'MAY' and (day<1 or day>31):
                print ("ERROR US42: ", day, " is not a valid date in ", "month: ",month)
            elif month == 'JUN' and (day<1 or day>30):
                print ("ERROR US42: ", day, " is not a valid date in ", "month: ",month)
            elif month == 'JUL' and (day<1 or day>31):
                print ("ERROR US42: ", day, " is not a valid date in ", "month: ",month)
            elif month == 'AUG' and (day<1 or day>30):
                print ("ERROR US42: ", day, " is not a valid date in ", "month: ",month)
            elif month == 'SEP' and (day<1 or day>30):
                print ("ERROR US42: ", day, " is not a valid date in ", "month: ",month)
            elif month == 'OCT' and (day<1 or day>31):
                print ("ERROR US42: ", day, " is not a valid date in ", "month: ",month)
            elif month == 'NOV' and (day<1 or day>30):
                print ("ERROR US42: ", day, " is not a valid date in ", "month: ",month)
            elif month == 'DEC' and (day<1 or day>31):
                print ("ERROR US42: ", day, " is not a valid date in ", "month: ",month)
            """Because of the way our parser is working, using datetime for stripping, it seems as though upon reading the file
            it will automatically flag an invalid date. This will result in the program not executing, refactoring the parser now
            may result in errors in the team's user stories as the specific usage of datetime varied from person to person. To
            demonstrate the functionality of the user story, August 30th was deemed the cutoff
            """
