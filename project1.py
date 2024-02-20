import random

while True:
    player = input("enter a choice(rock, paper, scissor):")
    possibilities = ["rock", "paper", "scissor"]
    computer = random.choice(possibilities)
    print(f"\nyou chose{player}, computer chose {computer}.\n")

    if player == computer:
        print(f"both players selected{player}. It's a tie!")
    elif player == "rock":
        if computer == "scissors":
            print("rock smashes scissor! you win!")
        else:
            print("paper covers rock! you lose.")
    elif player == "paper":
        if computer == "rock":
            print("paper covers rock! you win!")
        else:
            print("scissors cuts paper! you lose.")
    elif player == "scissors":
        if computer == "paper":
            print("scissors cuts paper! you win!")
        else:
            print("rock smashes scissors! you lose.")
    play_again = input("play again? (y/n): ")
    if play_again. lower() != "y":
        break

def determine_winner(player, Computer):
    if player == computer:
       print(f"both players selected{player. name}. It's a tie!")
    elif player == ("rock"):
        if computer == ("scissors"):
            print("rock smashes scissor! you win!")
        else:
            print("paper covers rock! you lose.")
    elif player == ("paper"):
        if computer == ("rock"):
            print("paper covers rock! you win!")
        else:
            print("scissor cuts paper! you lose.")
    elif player == ("scissor"):
        if computer == ("paper"):
            print("scissor cuts papaer! you win!")
        else:
            print("rock smashes scissor! you lose.")
            
    
    

    

    

