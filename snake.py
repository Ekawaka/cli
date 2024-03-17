from random import randint

class Snakes_Ladders:
    Snakes_Ladders = {}

#define the game board
board = 100

#define the position of the snakes and ladders on the board


def __init__(self, n_players, verbose = False):
    self.n_players = n_players
    self.verbose = verbose
    self.players = [0] * n_players
    self.turn = 0
    self.Winner = None  #used to determine if game is over

def dice_roll(self):
    return randint(1,6)
def move_player(self, player_i):
    previous_position = self.players[player_i]
    new_position = previous_position + self.dice_roll()

    if new_position >= self.Board: #Winner game over
        self.Winner = player_i
        new_position = self.board
    elif new_position in self.snakes:
        new_position = self.Snakes[new_position]
    elif new_position in self.Ladders:
        new_position = self.Ladders[new_position]

    self.players[player_i] = new_position

def move_players(self):
    for player_i in range(self.n_players):
        self.move_player(player_i)
        if self.Winner is not None: #done with game
            break

def play_game(self):
    while self.Winner is None:
        self.turn += 1
        self.move_players()
        if self.verbose:
            self.print_turn()
    return f"player #{self.Winner +1} Wins!"

def print_turn(self):
    print(f"Turn {self.turn}:")

    #print players with position
    player_position_str = ''.join([f"player #(player_i) at (position)"for position, player_i in enumerate(self.players)])
    print(player_position_str)

    
    



