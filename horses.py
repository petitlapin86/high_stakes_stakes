class Horses:
#HORSES TABLE
################################################################
    @staticmethod
    def print_horse_info():
        print('_'*25)  #dividing line

        horses =  {'1':'Seattle Slew',  #this is my use of a dictionary
               '2':'Zenyata',
               '3':'Black Caviar',
               '4':'Sea Biscuit',
               '5':'Man o War',
               '6':'Secretariat',
               '7':'Phar Lap'}

        print()  #default new line
        print("Saddle".center(10), end='')  # header
        print("Horse".ljust(10), end='\n')

        for saddle, horse in horses.items():  #iterate through dict
            print(saddle.center(10), end='')  #print each item in dict
            print(horse.ljust(10), end='\n')

        print("_"*25)  #dividing line
##################################################################

#HORSES MORE INFO
        while True:  #ask for a new saddle number infinitly
            saddle_number = int(input("Enter a horses saddle number for more information: "))
            print("When ready to go back to game type 0")

            if saddle_number > 7:  #tell user id number limitations
                print("Enter a saddle number between 0 and 7")

            elif saddle_number == 1:
                print("1st horse info goes here ")
            elif saddle_number == 2:
                print("2nd horse info goes here ")
            elif saddle_number == 3:
                print("3rd horse info goes here ")
            elif saddle_number == 4:
                print("4th horse info goes here ")
            elif saddle_number == 5:
                print("5th horse info goes here ")
            elif saddle_number == 6:
                print("6th horse info goes here ")
            elif saddle_number == 7:
                print("last horse here")
            elif saddle_number == 0:
                print("Goodbye")  #HERE I NEED TO ACTUALLY SEND BACK TO MAIN MENU : )
                break
#Horses.print_horse_info()
