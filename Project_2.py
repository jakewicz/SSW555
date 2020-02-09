def remove(ged_line):
    take = ged_line.strip('\n') 
    return take.split(" ")

def validate(remove):
    check = {
    "x": ["INDI",  "FAM",  "HEAD", "TRLR", "NOTE"],
    "y": ["NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "MARR", "HUSB", "WIFE", "CHIL", "DIV"],
    "z": ["DATE"] }

    level = remove.pop(0)
    tag = remove.pop(0)
    args = " ".join(remove)

    if (args in check["x"] or args in check["y"] or args in check["z"]):
        temp = tag
        tag = args
        args = temp

    if (level == "0"):
        if tag in check["x"]:
            valid = "Y"
        else:
            valid = "N"
    elif (level == "1"):
        if tag in check["y"]:
            valid = "Y"
        else: 
            valid = "N"
    elif (level == "2"):
        if tag in check["z"]:
            valid = "Y" 
        else:
            valid = "N"
    else: 
        valid = "N"

    return "<-- " + level + "|" + tag + "|" + valid + "|" + args 
            
if __name__ == "__main__":
    file = open('./My-Family-26-Jan-2020-658.ged')
    
    ged = file.readlines()

    for ged_line in ged:
        print ("--> " + ged_line)
        print(validate(remove(ged_line)))
        print ("-------------------")

    file.close