import random
import numpy

    ####################################################################################
class Race:  #this class shuffles the horse list to create random winners
    def horse_race(horses_to_win):  #take users input as argument

        horses =  {'1':'Seattle Slew',  #this is my use of a dictionary
                   '2':'Zenyata',
                   '3':'Black Caviar',
                   '4':'Sea Biscuit',
                   '5':'Man o War',
                   '6':'Secretariat',
                   '7':'Phar Lap'}

        print("\33[30m Here are the race results: ")
        print('\33[30m''_'*35)  #dividing line
        horses_list = list(horses.keys())  #turn dict into list
        numpy.random.shuffle(horses_list) #shuffle list

        print()  #default new line
        print("Saddle".center(10), end='')  # header
        print("Horse".ljust(10), end='\n')

        for saddle in horses_list:  #iterate through dict
            print(saddle.center(10), end='')  #print each item in dict
            print(horses[saddle].ljust(10), end='\n')  #new line after each horse

            print("_"*35)  #dividing line

        hasWon = True
        for i in range(len(horses_to_win)):
            print(horses_list[i])
            print(horses_to_win[i])
            if horses_to_win[i] != horses_list[i]:
                hasWon = False
                print(hasWon)
                break

        if hasWon:
                print("CONGRATULATIONS!, YOU WON!")
        else:
                print("Better luck next time")

        return hasWon

#Race.horse_race(['7', '2'])  #for test purposes
