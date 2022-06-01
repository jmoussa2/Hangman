
#The secret word the player is trying to guess
secrectWord = "rhythm"
lettersGuessed = ""

#The number of turns before the player loses
failureCount = 6

#loop until the player has made too many failed attempts
#will 'break' loop if they succeed instead
while failureCount > 0:

    #get the guessed letter from the player
    guess = input("Enter a letter: ")

    if guess in secrectWord:
        #Player guessed a correct letter
        print(f"Correct! There is one or more {guess} in the secret word.")
    else:
        failureCount -= 1
        print(f"Incorrect. There are no {guess} in the secrect word. {failureCount} turn(s) left.")

    #Maintain a list of all letters guessed
    lettersGuessed = lettersGuessed + guess
    wrongLetterCount = 0

    for letter in secrectWord:
        if letter in lettersGuessed:
            print(f"{letter}",end="")
        else:
            print("_", end="")
            wrongLetterCount += 1
    print("")

    #If there were no wrong letters, then the player won!
    if wrongLetterCount == 0:
        print(f"CONGRATS! The secrect word was: {secrectWord}. You won!")
        break

else:
    print("Sorry, you didn't win. Try again?")
