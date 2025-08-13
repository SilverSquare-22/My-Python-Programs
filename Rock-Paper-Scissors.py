import random
cl = ('Rock', 'Paper', 'Scissors')
print ('This is a Rock-Paper-Scissors simulation wherein you will play against the computer. Refer below the codes to input your choice:\n1. Rock\t2. Paper\t3.Scissors\n\nEnter your choice [1, 2 or 3]: ', end = '')
while True:
    try:
        ut = int (input ())
        while ut not in (1, 2, 3):
            ut = int (input ('\nInvalid entry! Enter a valid code [1, 2 or 3]: '))
        r = random.randrange (3)
        print ('------------------------------\nYou chose:', cl [ut - 1], "\nComputer's choice:", cl [r])
        ct = r + 1
        if ut == ct:
            print ("\nIt's a tie!")
        elif ut == 1:
            if ct == 2:
                print ('\nComputer wins!')
            else:
                print ('\nYou win!')
        elif ut == 2:
            if ct == 1:
                print ('\nYou win!')
            else:
                print ('\nComputer wins!')
        elif ut == 3:
            if ct == 1:
                print ('\nComputer wins!')
            else:
                print ('\nYou win!')
        break
    except ValueError:
        print ('\nInvalid entry! Enter a valid code [1, 2 or 3]: ', end = '')
