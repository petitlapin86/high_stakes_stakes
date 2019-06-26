
'''
REQUIREMENTS:
: )at the minimum at least of of each of the following:
[X]container type (list, tuple, set or dictionary)
[X]iteration type (for, while)
[X]condiditional (if)
[ ]try blocks
[X]user-defined functions
[X]input and or output file (submit input data)
[ ]user-defined class. the class must be imported by your main program and have the following required structures.
[ ]- at least 1 private and 2 public self attributes
[ ]at least 1 private and 1 public method that takes arguments, return values and are used by your program
[ ]an init() method that takes at least one argument
[ ]a repr() method
'''

#wallet
class Wallet:
    def __init__(self,wallet):  #this might be a good place to fill this requirement?yes
            self.__wallet = wallet

    def get_wallet(self):
        self.__wallet = wallet

    def set_wallet(self,wallet):
        self.__wallet = wallet
    #wallet = 100  #display wallet (start with $100)
    def win(self, amount):
        self.__wallet += amount

    def lose(self, amount):
        self.__wallet -= amount
    #To do : raise exception when wallet value is less than equal to 0

    def __check_money_in_wallet(self):
        try:
            #what do i do in here?
            if self.__wallet <= 0:
                raise ValueError('Wallet value is less than or equal to zero')
        except ValueError as e:
            print("You are out of money. ")#+repr(e) , include this if you want to print line 31

    def __repr__():
        #you can create your custom string
        wallet_string = "This is your wallet"
        return wallet_string
