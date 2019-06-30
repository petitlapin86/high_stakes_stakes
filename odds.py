import numpy

class Odds:  #this class shuffles the horse list to create random odds
    @staticmethod
    def print_odds_info():

        horse_odds =  {'1':'Seattle Slew',  #this is my use of a dictionary
               '2':'Zenyata',
               '3':'Black Caviar',
               '4':'Sea Biscuit',
               '5':'Man o War',
               '6':'Secretariat',
               '7':'Phar Lap'}

        print("\33[30m\n Here are the horses sorted by current odds to win: ")
        print('\33[30m''_'*35)  #dividing line
        horses_list = list(horse_odds.items())  #turn dict into list
        numpy.random.shuffle(horses_list) #shuffle list   #YAY THIS WORKS!
        horses_dict = dict(horses_list)  #turning into shuffled dictionary  #WONDER IF I NEED TO CHANGE BACK TO DICT AT ALL?

        print()  #default new line
        print("Saddle".center(10), end='')  # header
        print("Horse".ljust(10), end='\n')

        for saddle, horse in horses_dict.items():  #iterate through dict
            print(saddle.center(10), end='')  #print each item in dict
            print(horse.ljust(10), end='\n')  #new line after each horse

        print("_"*35)  #dividing line

#Odds.print_odds_info()  #for test purposes
