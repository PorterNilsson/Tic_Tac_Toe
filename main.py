from tic_tac_toe_game import TicTacToeGame
from random_player import RandomPlayer

player_1 = RandomPlayer()
player_2 = RandomPlayer()

games_to_play = 10_000_000

x_wins = 0
o_wins = 0
draws = 0
errors = 0
for _ in range(games_to_play):
    game = TicTacToeGame(False, player_1, player_2)
    
    result = game.play_game()

    if result == "X":
        x_wins += 1
    elif result == "O":
        o_wins += 1
    elif result == "Draw":
        draws += 1

print(f'{x_wins = } ({x_wins / games_to_play:.2%})')
print(f'{o_wins = } ({o_wins / games_to_play:.2%})')
print(f'{draws = } ({draws / games_to_play:.2%})')

if x_wins + o_wins + draws != games_to_play:
    raise Exception("INVALID GAMESTATE WAS REACHED")