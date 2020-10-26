answer = 5

attempts = 0

entry = ""

''' a loop that repeats while the users guess is not the same as the answer '''

while answer != entry :

    entry = int(input("Enter a number between 1 and 5 "))
    
    ''' Each time through the loop 1 is added to the number of attempts '''
    
    attempts = attempts + 1
    
''' After the loop it will say how many attempts it took '''

print("Well done you correctly guessed the number it took you " + str(attempts) + " attempts") '''
