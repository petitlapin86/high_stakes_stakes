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
        horses_list = list(horses.items())  #turn dict into list
        numpy.random.shuffle(horses_list) #shuffle list   #YAY THIS WORKS!
        winners_dict = dict(horses_list)  #turning into shuffled dictionary  #WONDER IF I NEED TO CHANGE BACK TO DICT AT ALL?

        print()  #default new line
        print("Saddle".center(10), end='')  # header
        print("Horse".ljust(10), end='\n')

        for saddle, horse in winners_dict.items():  #iterate through dict
            print(saddle.center(10), end='')  #print each item in dict
            print(horse.ljust(10), end='\n')  #new line after each horse

            print("_"*35)  #dividing line

        if winners_dict == horses_to_win:
                print(" CONGRATULATIONS!, YOU WON!")
        else:
                print("better luck next time")

Race.horse_race(2)  #for test purposes
