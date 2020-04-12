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