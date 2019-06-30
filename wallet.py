
#Wallet Class keeps provides money to bet with and tracks winnings/losses
class Wallet:
    def __init__(self,wallet):  #__init__ method with private __wallet
            self.__wallet = wallet

    def __check_money_in_wallet(self):
        try:
            if self.__wallet <= 0:  #If user runs out of money raise an error
                raise ValueError('Wallet value is less than or equal to zero')
        except ValueError as e:
            print("You are out of money. ")

    def get_wallet(self):
        return self.__wallet

    def set_wallet(self,wallet):
        self.__wallet = wallet

    def win(self, amount):
        self.__wallet += amount

    def lose(self, amount):
        self.__wallet -= amount
        self.__check_money_in_wallet()  #check amount in wallet

    def __repr__(self):
        wallet_string = " Your current wallet amount is: \033[94m %d \n"%self.__wallet  #display wallet amount
        return wallet_string

#test code
my_wallet = Wallet(100)  #wallet = 100  #display wallet (start with $100)
#print(my_wallet)
#my_wallet.win(50)
#print(my_wallet)
#my_wallet.lose(100)
#print(my_wallet)
