import random
import time
import math
import os
import sys
import pickle

cwd =  os.path.dirname(os.path.realpath('__file__'))

def init():
        if os.path.isdir('saves'):
            print("savedir exists!")
        else:
            print("savedir did not exist, creating now...")
            os.mkdir('saves')
            print("dir created!")

def main():
    while True:
        mainchoice=input('''
        Welcome to RuneExplorer! Choose an option!
        1)Continue
        2)New Game
        3)Exit 
        :- ''')
    
        if mainchoice == '1':
            svname = ("Please choose a save! :- ")
            load(svname)

        elif mainchoice == '2':
            print("Starting a new game! :- ")
            svname = input("Please enter a name for the save! :- ")
            svcr(svname)
        elif mainchoice == '3':
            print("Sorry to see you go!")
            sys.exit()
        else:
            print("Invalid Choice, Please enter 1, 2 or 3 :- ")

def load(name):
    if os.path.isfile(name):
        lname = os.path.join(cwd, f'saves/%s' %name +'.dat')
        save = open(lname, 'rb+')
        print("load success!")
        return(save)
    else:
        print("Oof, that save does not exist!")
        while True:
            choose = input('''
Choose an option:- 
1) Load some other save
2) Make a new save with this name
3) Return to main menu
''')
            if choose == '1':
                svname = input("Enter load's name (Hopefully will exist):- ")
                load(svname)
            elif choose == '2':
                svcr(name)
            elif choose == '3':
                main()
        else:
            print("Invalid choice! Please choose 1, 2 or 3")
    

def svcr(name):
    name = os.path.join(cwd, f'saves/%s' %name +'.dat')
    if os.path.isfile(name):
        choose = input("Oh! seems like that save already exists! Want to use it instead?? y/n")
        if choose.lower() == 'y':
            save = open(name, 'rb+')
            return(save)
        if choose.lower() == 'n':
            while True:
                choose = input('''
Choose an option:- 
1) Make a save with different name
2) Delete the existing save and make a new one
3) These choices are difficult! Just take me back to main menu!!
:- ''')
                if choose.lower() == '1':
                    svname = input("Enter save's name (different hopefully!):- ")
                    svcr(svname)
                elif choose.lower() == '2':
                    os.remove(name)
                    save = open(name, 'wb+')
                    return(save)
                elif choose.lower() == '3':
                    main()
                else:
                    print("Invalid choice! Enter 1, 2 or 3")
    else:
        print("creating save...")
        save = open(name, 'wb+')
        return (save)
init()
main()
        


        