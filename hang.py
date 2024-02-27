from random import choice
#selecting the hangman words
hangman=["JOVIAL","SMART","JUICY","HANDSOME"]
# selecting the word randomly
word=choice(hangman)
# printing character of randomly selected word as dashes
print(word)
print("_"*len(word))
# counting the no of characters in word
times=len(word)
# counting the no of wrong characters guesses
failed=0
# creating a loop equavalent to length of the word selected
while times>0:
    times=times-1
    guess=input("Guess the Character of the word: ").upper()
    if guess in word:
        print (guess,end=" ")
    else:
         print("_", end=" ")
         failed=failed+1   # count the number of failed attempt
         if failed==6:     # Exit loop if the number of failed attempts are 6
            break
if failed==0:
    print(f"Word is {word},YOU WORN")
else:
    print(f"Word is {word},YOU LOSE")












