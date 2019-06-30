class Horses:
#HORSES TABLE
################################################################
    @staticmethod
    def print_horse_info():
        print('\33[30m''_'*35)  #dividing line

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
        print("_"*35)  #dividing line
        for saddle, horse in horses.items():  #iterate through dict
            print(saddle.center(10), end='')  #print each item in dict
            print(horse.ljust(10), end='\n')

        print("_"*35)  #dividing line
##################################################################

#HORSES MORE INFO
        while True:  #ask for a new saddle number infinitly
            saddle_number = int(input("\33[30m Enter a horses saddle number for more information: "))
            print("\33[30m When ready to go back to game type 0 \n")

            if saddle_number > 7:  #tell user id number limitations
                print("\33[30m Enter a saddle number between 1 and 7")

            elif saddle_number == 1:
                print("\033[36m Back in the 70’s, Slew was remembered as a thouroughbred horse born for victory and boy oh boy did he manage to live up to his oath by birth by eventually. Growing up till the age of 28 which is shocking for the amount of years a horse can actually live and also remarkable as well. He has grown older than some humans have had the chance to, sadly passing away yet still his name remains as a legend in the horse racing business and is recognized globally. He has influenced the training and breeding of other horses and has served a great inspiration to horse trainers also by the legacy of his greatness left behind. Seattle Slew can definitely be considered as one of the best race horses to have ever kicked the grounds of the race tracks.\n")
            elif saddle_number == 2:
                print("\033[96m Female horses that exhibit the same amount of strength and determination as a stallion is somewhat of a remarkable thing and must be given the utmost of respect. Zenyatta has been dubbed as “The Queen of Race horses”. This automatically speaks enough about her reputation thus far and as far as ranked best race horses are concerned, she most certainly has the spirit of some famous human “godmother” we know, who do you picture that comes to mind? Zenyatta has also been the 2010 Race horse of the year due to carrying most of the weight during any other male or female horse of that year’s major races. In her majesty’s rest of retirement, she now enjoys motherhood with foals to her name.\n")
            elif saddle_number == 3:
                print("\033[94m Here we speak of Royalty Horses which represents one of the best in its field. Australian Royalty Horse Black Caviar is worth $210 000! In the case of Black Caviar, Royalty commands respect. Royalty Caviar as one of the best Race horsees of all time, most certainly earned that respect by winning 25 Races of her 25 Races in the midst of her Horse career before retiring In 2013.\n")
            elif saddle_number == 4:
                print("\033[92m The story of SeaBiscuit is more inspirational and doesn’t necessarily center around the number of wins it had, winning isn’t always as honorable as the integrity shown by someone or something and SeaBee has really been an exceptional example of utter dedication and perseverance. In his time, falling and getting back up then giving his competitors a duel finish and a run for their lungs at the last minute. Just like Race Horse Ruffian, SeaBiscuit also has a movie made in its honor. The determination of this specific horse has imprinted on an entire Nation of it’s era.\n")
            elif saddle_number == 5:
                print("\033[34m Man o' War was an American Thoroughbred who is widely considered one of the greatest racehorses of all time. Several sports publications including The Blood-Horse, Sports Illustrated, ESPN, and the Associated Press voted Man o' War as the outstanding horse of the 20th century.\n")
            elif saddle_number == 6:
                print("\033[35m Secretariat who can be considered as a God of War or an Spartan warrior. As the name sounds more Ancient Roman than anything else. But then again if horse names made them famous, horse racing businesses wouldn’t exist. In terms of the amount of money Secretariat has generated by his wins which spanned over a very short 16 month career altogether by emerging victoriously first 16 times, coming out second 3 times and third, only ONCE! Which all in all generated a winning total of $1,316,808 to be an exact figure. Which simply means to say that although horse racing is a billion dollar industry and has subsequently made people millionaires too. \n")
            elif saddle_number == 7:
                print("\033[95m Foaled in New Zealand,[3] he was trained and raced in Australia by Harry Telford.[4] Phar Lap dominated Australian racing during a distinguished career, winning a Melbourne Cup, two Cox Plates, an AJC Derby, and 19 other weight for age races.[5][6] He then won the Agua Caliente Handicap in Tijuana, Mexico \n")
            elif saddle_number == 0:
                print("Alright - Lets move on to who is likely to win!")
                break   #Send back to main menu

#Horses.print_horse_info()  Just for testing purposes
