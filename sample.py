'''Please find my comments and suggestions below...

1) To solve the formatting method we follow 2 approaches:
    1. The first one uses string function ljust to left justified text to a give width provided as an input parameter (check  also rjust if needed)
        The "end" parameter of print is also important to not have a return in the middle of 2 columns.
    2. The 2nd solution uses the % modulo operator. Its general form is
    %[flags][width][.precision]type
        The minus before width makes the string left justified.
    3. Of course, it is possible that there exists many other approaches to do this.

2) To solve the problem about the index print on column 1, you will have to change your dictionary to something like this:
    students = {1: {'112121': 'John'},
                      2: {'2343': 'Frank'}}

    Then, "print(students[1]['112121'])" will output "John"

This should help you to make progress on your problem.
In case doubts still, you can join a dropin session or resubmit showing your work.

Thanks for visiting Smarthinking.'''


students = {
 '112121': 'John',
 '5456': 'Gregory',
 '342432': 'Emily',
 '2343': 'Frank'}

# first method
# header
print("StudentID".ljust(20), end='')
print("StudentName".ljust(20), end='\n')

for sid, name in students.items():
 print(sid.ljust(20), end='')
 print(name.ljust(20), end='\n')

print("****************************************")
# another alternative
# header
print("StudentID".ljust(20), end='')
print("StudentName".ljust(20), end='\n')

for sid, name in students.items():
 print("%-20s"% (sid), end='')
 print("%-20s"% (name), end='\n')

 
  #below is attempt to print 3 items from key value pair instead of 2

  #horses_3 = {
  #            1: {'Seattle Slew': '2/7'},
  #            2: {'Zenyata': '6/7'},
  #            3: {'Black Caviar': '3/7'},
  #            4: {'Sea Biscuit': '4/7'},
  #            5: {'Man o War': '1/7'},
  #            6: {'Secretariat': '7/7'},
  #            7: {'Phar Lap': '5/7'}
  #            }

  #print("Saddle".ljust(20), end='')
  #print("Horses".ljust(20), end='')
  #print("Odds".ljust(20), end='\n')

  #for saddle in range(1):
  #    for horse, odd in horses_3.items():
  #        print(horse)
  #        print(odd)
