from UsefulFunctions import *
import Parser
from datetime import timedelta, datetime

#US38
#author GM
#list upcoming birthdays in next 30 days
def US38_upcoming_bdays(individuals):
    print('\nUS38: Upcoming birthdays, HAPPY BIRTHDAY to: ')
    group = []
    for indi in individuals:
        today = datetime.now()
        birth =  datetime.strptime(individuals[indi]['BIRT'], '%d %b %Y')
        thirty = datetime.today() - timedelta(days=30)
        if today.month == birth.month and today.day >= birth.day:
            print(indi, individuals[indi]['NAME'], "'s birthday is on", datetime.strftime(birth, '%d %b'))
            group.append(indi)
        if birth.month == thirty.month and birth.day >= thirty.day:
            print(indi, individuals[indi]['NAME'], "'s birthday is on", datetime.strftime(birth, '%d %b'))
            group.append(indi)
    return group

#US39
#author GM
#list upcoming anniversaries in next 30 days
def US39_upcoming_anniversary(families, individuals):
    group = []
    print('\nUS39: Upcoming anniversaries, HAPPY ANNIVERSARY to: ')
    for indi in families:
        today = datetime.now()
        anni =  datetime.strptime(families[indi]['MARR'], '%d %b %Y')
        thirty = datetime.today() - timedelta(days=30)
        if today.month == anni.month and today.day >= anni.day:
            print(indi, individuals[families[indi]["HUSB"]]['NAME'],"and",individuals[families[indi]["WIFE"]]['NAME'], "got married on", datetime.strftime(anni, '%d %b %Y'))
            group.append(indi)
        if anni.month == thirty.month and anni.day >= thirty.day:
            print(indi, individuals[families[indi]["HUSB"]]['NAME'],"and",individuals[families[indi]["WIFE"]]['NAME'], "got married on", datetime.strftime(anni, '%d %b %Y'))
            group.append(indi)
    return group

#US 37
#author JC
#List recent survivors
def US37_recent_survivors(individuals):
    survivors_spouse = {}
    survivors_children = {}
    today = datetime.now()
    print('')
    print('US37: list of recent survivors: ')
    for indi in individuals:
         if individuals[indi]['DEAT'] != 'N/A':
            diff = int((today - datetime.strptime(individuals[indi]['DEAT'], '%d %b %Y')).days)
            if diff <= 30:
                print('')
                print("The following are recent survivors of " + individuals[indi]['NAME'])
                if individuals[indi]['SPOUSE'] != 'N/A':
                    survivors_spouse = individuals[indi]['SPOUSE']
                    survivors_spouse = individuals[survivors_spouse]['NAME']
                    print(survivors_spouse + ' their spouse')
    for indi in individuals:
         if individuals[indi]['DEAT'] != 'N/A':
            diff = int((today - datetime.strptime(individuals[indi]['DEAT'], '%d %b %Y')).days)
            if diff <= 30:
                if individuals[indi]['CHILD'] != 'N/A':
                    children = individuals[indi]['CHILD']
                    survivors_children = children
    for children in survivors_children:
        survivors_children = individuals[children]['NAME']
        print(survivors_children + ' their child')
    return survivors_children

#US 33
#author JC
#List orphans
def US33_list_orphans(families, individuals):
    orphans = {}
    mom = {}
    dad = {}
    child = {}
    print('')
    print('US33: list of all the orphans: ')
    for indi in families:
        if families[indi]['CHIL'] != 'N/A':
            child = families[indi]['CHIL']
            dad = families[indi]['HUSB']
            mom = families[indi]['WIFE']
            if individuals[mom]['DEAT'] != 'N/A':
                if individuals[dad]['DEAT'] != 'N/A':
                        orphans = child
    for child in orphans:
        orphans = individuals[child]['NAME']
        print(orphans)