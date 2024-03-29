from board import Board
from typing import Optional
from random_player import RandomPlayer

class TicTacToeGame:
	
	def __init__(self, output=True, player_x: Optional[RandomPlayer] = None, player_o: Optional[RandomPlayer] = None):
		self.board = Board()
		self.player_turn = "X"

		self.output = output

		self.player_x = player_x
		self.player_x.set_symbol("X")
		self.player_o = player_o
		self.player_o.set_symbol("O")

		
	def play_game(self) -> str:

		while not self.board.game_over():

			current_turn = self.player_turn

			if current_turn == "X":
				if self.output:
					print("X's turn!")
				self.player_turn = "O"
			else:
				if self.output:
					print("O's turn!")
				self.player_turn = "X"
		
			if self.output:
				print()
				print(self.board)
			
			move = None
			valid_move = False
			while not valid_move:

				if current_turn == "X" and self.player_x != None:
					move = self.player_x.move(self.board)
				elif current_turn == "O" and self.player_o != None:
					move = self.player_o.move(self.board)
				else:
					move = input("Type move! (A1, C2, etc)")

				valid_move = self.board.make_move(move, current_turn)

				if self.output:
					if not valid_move:
						print("INVALID MOVE")

			self.board.valid_moves.remove(move)
		
		if self.output:
			print()
			print(self.board)
			if self.board.result != "Draw":
				print(self.board.result + " Wins!")
			else:
				print(self.board.result + "!")
			
		return self.board.result