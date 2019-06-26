"""horse race cli game in python

REQUIREMENTS:
at the minimum at least of of each of the following:
[ ]container type (list, tuple, set or dictionary)
[X]iteration type (for, while)
[X]condiditional (if)
[ ]try blocks
[ ]user-defined functions
[X]input and or output file (submit input data)
[ ]user-defined class. the class must be imported by your main program and have the following required structures.
[ ]- at least 1 private and 2 public self attributes
[ ]at least 1 private and 1 public method that takes arguments, return values and are used by your program
[ ]an init() method that takes at least one argument
[ ]a repr() method

[ ]provide unit tests that prove your class methods work as expected. the tests should evaluate results using
the assert statements.

if you desire to include a module that is not part of the standard python build you must first
get permission from the facilitator.

when submitting your project the instructions for installing the module must be included
in the instructions for running the code
"""

from horses import Horses  #import horses.py
from odds import Odds  #import odds.py
#spec out ideas for project

#INTRO
#-----------------------------------------------------------
#tell user the name of race and horses running
print("Welcome to High Stakes Stakes!")
print(f"The the Horses in todays race are: ")
Horses.print_horse_info()  #call Horses class from horses.py

#ODDS
#-----------------------------------------------------------
#offer more information on horse odds y/n
answer = input("Would you like to see horse current odds to win? y/n: ".lower())
if answer == 'y' or 'yes':
    print(f'{Odds.print_odds_info()}')  # if yes display horse odds from odds.py
elif answer == 'n' or 'no':   #FOR SOME REASON ONLY IF BLOCK IS WORKING HERE
    print('Risky!, okay lets bet.')
else:
    print("please enter y or n.")

#BETTING
#--------------------------------------------------------------
print("In Horse Races there are three major types of bets: \n Win (1st), Exacta (1st and 2nd) and Trifecta (1st, 2nd and 3rd)")
type_of_bet = input("Enter 1, 2 or 3 for the type of bet you'd like to make: ")  # ask user which type of bet they would like to make (1, 1,2 or 1,2,3)

horses_to_win = input("Now enter the saddle number for the horse or horses you'd like to bet on: ")  # ask user which horses they want to bet on

amount = input("Lastly enter a numberical amount of dollars you'd like to place on this bet: ")
# bet placing - ask user how much they would like to bet
print(f"To confirm you would like to make a {type_of_bet} bet, on horse(s) {horses_to_win}, with ${amount}")#confirm total bet (type_of_bet, horses_to_win, bet_amount)

#if yes, run program
#display race results
#display wallet with winnings or losings calculated

#ALGORITHMS
#--------------------------------------------------------------
# program that calculates wallet with winnings or losings and creates new total
# program that randomly selects winners of horses for three different types of bets
# program that compares winners wirh users bet horses_to_win
