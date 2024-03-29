from board import Board
import random

class RandomPlayer:

    def __init__(self):
        self.symbol = None
    
    def move(self, board: Board):

        return random.choice(board.valid_moves)

    def set_symbol(self, symbol):
        self.symbol = symbol