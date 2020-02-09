#Jacob Senkewicz
#Project 02 SSW 555

data = open("proj02test.ged")
#print(data.read())   #used as a test to see if the file is read properly
goodTags0 = ["INDI", "FAM", "HEAD", "TRLR", "NOTE"]
goodTags1 = ["NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "MARR", "HUSB", "WIFE", "CHIL", "DIV"]
goodTags2 = ["DATE"]
myOutput = []

for line in data:
    line = line.strip()
    myOutput.append("-->" + line)
    parse = line.split(' ')
    level = parse[0]
    #int(level) #
    tag = parse[1]

    try:
        tag2 = parse[2]
    except:
        continue

    arg1 = line.replace(level,'',1)
    arg2 = arg1.replace(tag,'',1)
    arg2 = arg2.strip() #need this otherwise there is a large gap
    arg3 = arg2.replace(tag2,'',1) #using replace function a a way of 'subtracting' linesn only need to do it once

    if tag in goodTags0 and int(level) == 0:
        valid = "Y" + "|"
    elif tag in goodTags1 and int(level) == 1:
        valid = "Y" + "|"
    elif tag in goodTags2 and int(level) == 2:
        valid = "Y" + "|"
    elif tag2 in goodTags0 and int(level) == 0:
        valid = "Y" + "|"
    else:
        valid = "N" + "|"

    if tag2 == "INDI" or tag2 == "FAM":
        myOutput.append("<--" + level + "|" + tag2 + "|" + valid + tag + arg3)
    elif tag2:
        myOutput.append("<--" + level + "|" + tag + "|" + valid + tag2 + arg3)
    else:
        myOutput.append("<--" + level + "|" + tag + "|" + arg2)

#print(myOutput)
for line in myOutput:
    print(line)
    #print("<--" + level + tag + valid + arguments)
