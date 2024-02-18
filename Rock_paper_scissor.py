# rock, paper, scissors Game
from random import randint

# moves for the player
moves = ("rock", "paper", "scissor")

while True:
    computer = moves[randint(0,2)]
    player = input("rock, paper or scissor? (or end the game) ").lower()
    if player =="end the game":
        print("the game has ended")
        break 
    elif player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("you lose!", computer, "beats", player)
        else:
            print("you win!", player, "beats", computer)
    elif player =="paper":
        if computer == "scissor":
            print("you lose!", computer, "beats", player)
        else:
            print("you win!", player, "beats", computer)
    elif player =="scissor":
        if computer == "rock":
            print("you lose!", computer, "beats", player)
        else:
            print("you win!", player, "beats", computer)
    else:
        print("check your spelling...")

