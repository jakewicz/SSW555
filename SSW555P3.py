#Jacob Senkewicz
#Project 02 SSW 555

from prettytable import PrettyTable

indTable = PrettyTable()
indTable.field_names = ["Unique Identifier", "Name"]
famTable = PrettyTable()
famTable.field_names = ["Unique Identifier", "Name"]
data = open("proj02test.ged")
#print(data.read())   #used as a test to see if the file is read properly

goodTags0 = ["INDI"]
goodTags1 = ["NAME"]
goodTags2 = ["FAM"]
goodTags3 = ["HUSB", "WIFE"]
individual = {
    "id":{},
    "name":{}
    }
family = {
    "id": {},
    "name": {}
}

for line in data:
    line = line.strip()
    parse = line.split(' ')
    level = parse[0]
    uuid = parse[1]
    try:
        tag2 = parse[2]
    except:
        continue

    #indTable.add_row([level, tag])
    #famTable.add_row([level, tag])

    arg1 = line.replace(level,'',1)
    arg2 = arg1.replace(uuid,'',1)
    name = arg2.strip() #need this otherwise there is a large gap
    arg3 = name.replace(tag2,'',1)

    if tag2 in str(goodTags0) and int(level) == 0:
        individual.update({"id":uuid})
    if uuid in str(goodTags1) and int(level) == 1:
        individual.update({"name": name})

    if tag2 in str(goodTags2) and int(level) ==0:
        family.update({"id":uuid})
    if uuid in str(goodTags3) and int(level) == 1:
        family.update({"name": name})



print("INDIVIDUALS")
print("_______________")
for id, name in individual.items():
    print ('{} | {}'.format(id, name))

print("")
print("FAMILY")
print("_______________")
for id, name in family.items():
    print('{} | {}'.format(id, name))





    #indTable.add_row()
    #print(individual["id"])
    #print(individual["name"])
#for line in family:
#    famTable.add_row([line])
#indTable.sortby = "Unique Identifier"
#famTable.sortby = "Unique Identifier"
#print(famTable)
#print(indTable)
