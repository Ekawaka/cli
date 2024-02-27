from random import choice
#selecting the hangman words
hangman=["JOVIAL","SMART","JUICY","HANDSOME","BRIGHT"]
# selecting the word randomly
word=choice(hangman)
# printing character of randomly selected word as dashes
print(word)
print("_"*len(word))
# counting the no of characters in word
times=len(word)
# counting the no of wrong characters guesses
failed=0
letters_guessed=[]
# creating a loop equavalent to length of the word selected
while times>0:
    guess=input("Guess the Character of the word: ").upper()
    if (guess in word and guess not in letters_guessed):
        print (guess,end=" ")
        letters_guessed.append(guess) # Creating a list of characters chosen
        times=times-1                   # decreasing the remaining chance choose a character
    elif (guess in word and guess in letters_guessed):
          print ("Letter already selected,select another letter")
    else:
        guess not in word
        print("_", end=" ")
        letters_guessed.append(guess)
        times=times-1     # decreasing the remaining chance choose a character
        failed=failed+1   # increasing count of failed attempts
        if failed==6:     # Exit loop if the number of failed attempts are matched 6
            break
if failed==0:
    print(f"letters guessed: {letters_guessed}")
    print(f"Word is {word},YOU WORN")
else:
    print(f"letters guessed: {letters_guessed}")
    print(f"Word is {word},YOU LOSE")