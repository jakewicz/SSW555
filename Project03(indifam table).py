#gianna jason dan jake
#project 3 portion that parses lines and prints out each indi and family

import pprint

def strip(ged_line):
    return ged_line.strip('\n').split(" ")


def check(line):
    tags_0 = ["INDI",  "FAM",  "HEAD", "TRLR", "NOTE"]
    tags_1 = ["NAME", "SEX", "BIRT", "DEAT", "FAMC",
                "FAMS", "MARR", "HUSB", "WIFE", "CHIL", "DIV"]
    tags_2 = ["DATE"]

    level = line.pop(0)
    tag = line.pop(0)
    args = " ".join(line)
    status = False

    if (tag == "INDI" or tag == "FAM"):
        status = False

    if ((args in tags_0) or (args in tags_1) or (args in tags_2)):
        tag, args = args, tag
    if ((level == "0") and (tag in tags_0)):
        status = True
    elif ((level == "1") and (tag in tags_1)):
        status = True
    elif ((level == "2") and (tag in tags_2)):
        status = True
    return(status, tag, args)


def read_file(path):
    ged = open(path)
    ged_lines = ged.readlines()
    person_date_tags = ["BIRT", "DEAT"]
    fam_date_tags = ["MARR","DIV"]
    fam_flag=False
    date_type=''
    individuals={}
    ind_id = ""
    families={}
    for ged_line in ged_lines:
        status, tag, args = check(strip(ged_line))
        if(status == True):
            if(tag == "INDI"):
                ind_id = args
                individuals[ind_id] = {}
                individuals[ind_id]["ID"] = args
                fam_flag = False

            if(tag == "NAME" or tag == "SEX"):
                individuals[ind_id][tag] = args

            if(tag in person_date_tags):
                date_type = tag
            if(tag == "DATE"):
                if(fam_flag == False):
                    individuals[ind_id][date_type] = args
                else:
                    families[ind_id][date_type] = args

            if(tag == "FAM"):
                ind_id = args
                fam_flag = True
                families[ind_id] = {}
                families[ind_id]["ID"] = args

            if(tag in fam_date_tags):
                date_type = tag
            if(tag == "HUSB" or tag == "WIFE"):
                families[ind_id][tag]=args
            if(tag == "CHIL"):
                if( tag not in families[ind_id].keys() ):
                    families[ind_id][tag] = [args]
                else:
                    families[ind_id][tag].append(args)
    
    ged.close
    return(individuals, families)

pp = pprint.PrettyPrinter()
individuals, families =read_file('./project01.ged')
pp.pprint(individuals)
print(individuals.get("@I8@"))
pp.pprint(families)
