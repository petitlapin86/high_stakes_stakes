class Color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

name = "paige"

print(Color.PURPLE + 'Hello World !')
print('\033[94m second version !')
print('\033[1m third version !')
print(f"my name is{name}"(Color.BOLD))
