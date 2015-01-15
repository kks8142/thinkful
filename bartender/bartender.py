#!/usr/bin/python -tt

import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

def get_profile():
    preferences={}
    for type,question in questions.iteritems():
        print question
        usr_input = raw_input("Enter y or yes\n").lower()
        if (usr_input == ('y' or 'yes')):
            preferences[type] = usr_input
    return preferences
    
    
def dump_preferences(preferences):
    have_prefs=0
    print "\n"
    print "Here is what you like :" 
    for i in preferences:
       if preferences[i]==('y' or 'yes'):
           have_prefs += 1
           print "{}++++{}".format(i, preferences[i])
    if not have_prefs:
       print "you have no preferences\n"
       
    return have_prefs
           

def make_my_drink(preferences):
    my_drink = []
    for type, liked in preferences.iteritems():
        if liked:
           #print "{}... {}".format(type, liked) 
           my_drink.append(random.choice(ingredients[type]))
    
    return my_drink


def print_reciepe(my_drink):
     print "\n"
     print "your drink is coming up."
     print "Here is the reciepe."
     for an_ingredient in my_drink:
         print "A {}".format(an_ingredient)

def main():
   while True:
     usr_pref = get_profile()
     have_prefs = dump_preferences(usr_pref)
     if have_prefs:
        my_drink = make_my_drink(usr_pref)
        print_reciepe(my_drink)
        print "\nDo you like to enjoy one more drink"
        usr_input = raw_input("Enter y or yes\n").lower()
        if (usr_input != ('y' or 'yes')):
           print "\nAdios..\n"
           break
     else:
        print "\ndon't be boring person..lets try again\n"
	

if __name__=='__main__':main()