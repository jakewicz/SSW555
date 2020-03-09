from UsefulFunctions import *
from Parser import *

#US15
#author GM
#no more than 15 siblings
def child_max(indi, families):
    for fam in families:
        if 'CHIL' in families[fam].keys():
            if len(families[fam]['CHIL']) >15:
                return("ERROR: too many kids")

#US14
#author GM
#no more than 5 kids born at once
def quintuplets(indi, families):
    for fam in families:
        if 'CHIL' in families[fam].keys():
            if len(families[fam]['CHIL']) >1:
                #family has more than 5 kids
                for child in families[fam]['CHIL']:
                    counter=1
                    date= individuals[child]['BIRT']
                    for child2 in families[fam]['CHIL']:
                        if(individuals[child2]['BIRT']==date):
                            counter +=1
                    if (counter >5):
                        return ("ERROR: more than 5 kids born at once")
    return ("families valid")

#US28
#author JC
#list the deceased
def the_deceased(individuals):
    dead = {}
    for indi in individuals:
        if('DEAT' in individuals[indi].keys()):
            dead[individuals[indi]['ID']] = individuals[indi]['NAME']
        else:
            continue
    return dead

#We Need these two lines to read in file and add to ages
#Adds to age dictionary
individuals, families =read_file('./test.ged')
individuals = UsefulFunctions.age_bank(families, individuals)