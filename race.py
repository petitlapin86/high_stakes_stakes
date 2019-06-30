import random
import numpy

#Race Class shuffles the horse list to create random winners & calculates wins/losses
class Race:
    def horse_race(horses_to_win):  #take users input as argument

        horses =  {'1':'Seattle Slew',  #dictionary of horses
                   '2':'Zenyata',
                   '3':'Black Caviar',
                   '4':'Sea Biscuit',
                   '5':'Man o War',
                   '6':'Secretariat',
                   '7':'Phar Lap'}
        print("\n \033[94m AND THE HORSES ARE OFF! \n")  #simple horse unicode to represent the race
        print(u"  \U0001F40E \U0001F40E \U0001F40E \U0001F40E \U0001F40E \U0001F40E \U0001F40E")
        print("\n \33[30m Here are the race results: ")
        print('\33[30m''_'*35)  #dividing line
        horses_list = list(horses.keys())  #turn dict into list
        numpy.random.shuffle(horses_list) #shuffle list to create random winners

        print()  #default new line
        print("Saddle".center(10), end='')  # header
        print("Horse".ljust(10), end='\n')
        print("_"*35)  #dividing line

        num_of_horses = len(horses_to_win)  #compare length of lists

        for saddle in horses_list[0:num_of_horses]:  #iterate through dict
            print(saddle.center(10), end='')  #print each item in dict
            print(horses[saddle].ljust(10), end='\n')  #new line after each horse
            print("_"*35)  #dividing line

        has_won = True  #this block of codes checks if users horses match winning horses
        for i in range(num_of_horses):
            if horses_to_win[i] != horses_list[i]:
                has_won = False
                break

        if has_won:  #let user know if they win or lose
                print("\n CONGRATULATIONS!, YOU WON!")
        else:
                print("\n Sorry, you LOST this race, better luck next time!")

        return has_won

#Race.horse_race(['7', '2'])  #for test purposes
