import numpy

class Odds:
    def print_odds_info():
        horse_odds =  {'1':'Seattle Slew',  #this is my use of a dictionary
               '2':'Zenyata',
               '3':'Black Caviar',
               '4':'Sea Biscuit',
               '5':'Man o War',
               '6':'Secretariat',
               '7':'Phar Lap'}

        print("Here are the current horse odds to win: ")
        horses_list = list(horse_odds.items())  #turn dict into list
        print("_" * 50)
        numpy.random.shuffle(horses_list) #shuffle list   #YAY THIS WORKS!
        print(horses_list)

        print("_" * 50)
        horses_dict = dict(horses_list)  #getting shuffled dictionary  #WONDER IF I NEED TO CHANGE BACK TO DICT AT ALL?
        print(horses_dict)


#Odds.print_odds_info()
