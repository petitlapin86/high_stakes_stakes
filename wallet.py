
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

    def __repr__(self):
        #you can create your custom string
        wallet_string = "Your current wallet amount is %d"%self.__wallet
        return wallet_string

#test code
my_wallet = Wallet(100)
#print(my_wallet)
#my_wallet.win(50)
#print(my_wallet)
#my_wallet.lose(100)
#print(my_wallet)
