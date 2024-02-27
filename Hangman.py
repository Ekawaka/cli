import random

print("welcome to hangman")
print(".......................................")

wordDictionary = ["berries", "water", "rosemary", "glucose", "orange", "white"]

# chose a random word

randonWord = random.choice(wordDictionary)

for x in "randomWord":
    print("_", end="")

def print_hangman(wrong):
    if (wrong == 0):
        print("\n+---+")
        print("    |")
        print("    |")
        print("    |")
        print("   ===")
    elif(wrong == 1):
        print("\n+---+")
        print("o    |")
        print("    |")
        print("    |")
        print("   ===")
    elif(wrong == 2):
        print("\n+---+")
        print("o   |")
        print("|   |")
        print("    |")
        print("   ===")
    elif(wrong == 3):
        print("\n+---+")
        print(" o  |")
        print("/|  |")
        print("    |")
        print("   ===")
    elif(wrong == 4):
        print("\n+---+")
        print(" o  |")
        print("/|\ |")
        print("    |")
        print("   ===")
    elif(wrong == 5):
        print("\n+---+")
        print(" o  |")
        print("/|\ |")
        print("/   |")
        print("   ===")
    elif(wrong == 6):
         print("\n+---+")
         print(" o  |")
         print("/|\ |")
         print("/ \ |")
         print("   ===")

def printWord(guessedLetters):
    counter=0
    rightLetters=0
    for char in "randomWord":
        if(char in guessedLetters):
            print(randonWord[counter], end="")
            rightletters+=1
        else:
            print(" ", end=" ")
        counter+=1
        return rightLetters

def printLines():
    print("\r")
    for char in "randomWord":
        print("\u203E",end=" ")

    # create loops for the game
        
lenght_of_word_to_guess = len("randomWord")
amount_of_time_wrong = 0
current_guess_index = 0
current_letters_guessed = []
current_letters_right = 0

while("amount_of_times_wrong" != 6 and current_letters_right != "length_of_word_to_guess"):
    print("\nLetter guessed so far: ")
    for letter in current_letters_guessed:
        "Print"(letter, end=" ")
    # To prompt user to input
    letterguessed = input("\nGuess a letter: ")
    # user is right
    if("randomWord"[current_guess_index] == letterguessed):
        print_hangman("amount_of_times_wrong")
        # print word
        current_guess_index+=1
        current_letters_guessed.append(letterguessed)
        current_letters_right = printWord(current_letters_guessed)
        printLines()
    # use was wrong
    else:
        amount_of_time_wrong+=1
        current_letters_guessed.append(letterguessed)
        # print word
        print_hangman(amount_of_time_wrong)
        current_letters_right = printWord(current_letters_guessed)
        printLines()

print("Game is over! Thank you":) 






