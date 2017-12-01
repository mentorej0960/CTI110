# Generate a random number ranging from 1 through 100 
# November 12, 2017
# CTI-110 M6HW2 - Random Number Guessing Game
# Jermine Mentore
#Resubmitting assignment.


import random

def generateRandomNumber():
    randomNumber = random.randint(1, 100)
    return randomNumber

def askUserForNumber():
    userNumber = int( input( "Guess the number: "))
    return userNumber
def checkUserNumber( userNumber, randomNumber ):
    if userNumber > randomNumber:
        return "Too high"
    elif userNumber < randomNumber:
        return "Too low"
    else:
        return "Congratulations!"

def main():
    userCongratulated = False

    while userCongratulated==False:
        userNumberOfGuesses = 0
        randomNumber = generateRandomNumber()
        userNumber = askUserForNumber()
        userNumberOfGuesses += 1
        message = checkUserNumber( userNumber, randomNumber )

        while message != "Congratulations!":
            print( message )
            userNumber = askUserForNumber()
            message = checkUserNumber( userNumber, randomNumber )
            userNumberOfGuesses = userNumberOfGuesses + 1

        print( message, "It took you", userNumberOfGuesses,\
               "attempts to guess correctly\n" )
        userCongratulated = True

main()

        
        
    
