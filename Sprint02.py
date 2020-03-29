from UsefulFunctions import *
from Parser import *

#US15
#author GM
#no more than 15 siblings
def US15_child_max(indi, families):
    if 'CHIL' in families[indi].keys():
        if len(families[indi]['CHIL']) >15:
            return("ERROR: too many kids")

#US14
#author GM
#no more than 5 kids born at once
def US14_quintuplets(indi, families, individuals):
    if 'CHIL' in families[indi].keys():
        if len(families[indi]['CHIL']) >5:
            #family has more than 5 kids
            for child in families[indi]['CHIL']:
                counter=1
                date= individuals[child]['BIRT']
                for child2 in families[indi]['CHIL']:
                    if(individuals[child2]['BIRT']==date):
                        counter +=1
                if (counter >6):
                    return ("ERROR: more than 5 kids born at once")

#US29
#author JC
#list the deceased
def US29_the_deceased(individuals):
    print("US 29: List of the deceased:")
    for indi in individuals:
        if(individuals[indi]['ALIVE'] == 'False'):
            print(individuals[indi]['NAME'])
