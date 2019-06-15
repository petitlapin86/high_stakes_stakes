horses =  {'Seattle Slew': '2/7',
          'Zenyata': '6/7',
          'Black Caviar': '3/7',
          'Sea Biscuit': '4/7',
          'Man o War': '1/7',
          'Secretariat': '7/7',
          'Phar Lap': '5/7'}

print(format("Saddle", "10s"),format("Horses", "10s"), format("Odds", "10s")) #format strings specified width
for horse, odds in horses.items():
    print('{}''{}'.format(horse, odds))



horses_2 =  {'Seattle Slew': '2/7',
          'Zenyata': '6/7',
          'Black Caviar': '3/7',
          'Sea Biscuit': '4/7',
          'Man o War': '1/7',
          'Secretariat': '7/7',
          'Phar Lap': '5/7'}

horses_3 = {
            1: {'Seattle Slew': '2/7'},
            2: {'Zenyata': '6/7'},
            3: {'Black Caviar': '3/7'},
            4: {'Sea Biscuit': '4/7'},
            5: {'Man o War': '1/7'},
            6: {'Secretariat': '7/7'},
            7: {'Phar Lap': '5/7'}
            }

# first method
# header
print("Horses".ljust(20), end='')
print("Odds".ljust(20), end='\n')

for horse, odd in horses_2.items():
 print(horse.ljust(20), end='')
 print(odd.ljust(20), end='\n')
