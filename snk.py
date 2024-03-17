import random

class SnakesAndLadders:

#define the game board
board = 100

#define the position of the snakes and ladders on the board

snakes_ladders = {}
#define the positions of the players and the current player
players = [1, 1]
current_player = 0

#define a function to roll the dice and move the player
def roll_dice():
    return random.randint(1, 6)
def move_player(player, roll):
    new_position = player + roll
    if new_position > 100:
        return player
    if new_position in snakes_ladders:
        return snakes_ladders[new_position]
    return new_position

#define a function to check if a player has won the game

def check_win(player):
    return player == 100

#define the game loop
while True:

    #Get the roll for the current player and move the player
    input(f"player{current_player +1}, press Enter to roll the dice")
    roll = roll_dice()
    print(f"player {current_player +1} rolled {roll}")
    players[current_player] = move_player(players[current_player], roll)
print(f"player{current_player +1} moved to position {players[current_player]}")

#check if the player has won the game
if check_win(players[current_player]):
    print(f"player{current_player +1} has won the game!")
    
    
    

