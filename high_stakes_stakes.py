"""
horse race cli game in python
Created June 2019 Author Paige Jones
"""

from horses import Horses  #import horses.py
from odds import Odds  #import odds.py
from wallet import Wallet  #import wallet.py
from race import Race  #import race.py

#INTRO
#-----------------------------------------------------------
#tell user the name of race and horses running
print('\33[30m''_'*35)  #dividing line
print("\33[30m \n Welcome to High Stakes Stakes!")
print("\33[30m The Horses in todays race are: ")
Horses.print_horse_info()  #call Horses class from horses.py

#ODDS
#-----------------------------------------------------------
#offer more information on horse odds y/n
while True:
    answer = input(" Would you like to see horse current odds to win? y/n: ").lower()
    if answer == 'y' or answer =='yes':
        Odds.print_odds_info()  # if yes display horse odds from odds.py
        break
    elif answer == 'n' or answer =='no':   #FOR SOME REASON ONLY IF BLOCK IS WORKING HERE
        print(' Risky!, okay lets bet. \n')
        break
    else:  #FOR SOME REASON ONLY IF BLOCK IS WORKING HERE
        print(" Please enter y or n.")

#BETTING
#--------------------------------------------------------------
user_wallet = Wallet(100)  #define default wallet amount
print(user_wallet)

print("\33[30m In Horse Races there are three major types of bets: \n \033[94m Win (1st)\n  Exacta (1st and 2nd)\n  Trifecta (1st, 2nd and 3rd) \n")
response = 'y'
while response == 'y' or response =='yes':
    type_of_bet = int(input("\33[30m Enter 1, 2 or 3 for the type of bet you'd like to make: ")) # ask user which type of bet they would like to make (1, 1,2 or 1,2,3)
    correctBet = False
    horses_to_win = []
    while not correctBet:
        horses_to_win = input(" Now enter the saddle number for the horse or horses you'd like to bet on : ").split(",")
        # ask user which horses they want to bet

        if(len(horses_to_win)==type_of_bet):
            correctBet = True

    amount = int(input(" Lastly enter a numerical amount of dollars you'd like to place on this bet: "))  # bet placing - ask user how much they would like to bet

#print#confirm total bet (type_of_bet, horses_to_win, bet_amount)

    go_on = True
    while True:
        confirm_response = input(f" To confirm you would like to make a {type_of_bet} bet, on horse(s) {horses_to_win}, with ${amount}. Y/N :").lower()  #confirm total bet (type_of_bet, horses_to_win, bet_amount)
        if confirm_response == 'y' or confirm_response == 'yes':
            break
        elif confirm_response == 'n' or confirm_response == 'no':
            go_on = False
            break
        else:
            print("please enter y or n.")

    if go_on:  #if yes, run program
        win = Race.horse_race(horses_to_win)
        if win:
            user_wallet.win(amount)
        else:
            user_wallet.lose(amount)

    print(user_wallet)  #display wallet with winnings or losings calculated

    if(user_wallet.get_wallet() <= 0):
        print("No more bets can be placed")
        break
    else:
        while True:
            response = input(" Would you like to place another bet? y/n: ").lower()
            if response == 'y' or response == 'yes' or response =='n' or response=='no':
                break
            else:
                print("please enter y or n.")
