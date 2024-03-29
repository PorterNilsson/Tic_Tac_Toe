class Board:
	
	def __init__(self):
		self.board_state = [[None, None, None] for _ in range(3)]
		self.row_letters = ["A", "B", "C"]
		self.result = None

		self.valid_moves = [
		"A1", "A2", "A3",
		"B1", "B2", "B3",
		"C1", "C2", "C3"
		]
	
	def __str__(self):
		return_string = "  1|2|3\n"
		
		index = 0
		for row in self.board_state:
			return_string += self.row_letters[index]
			index += 1
			return_string += "|"
			
			for cell in row:
				
				if cell != None:
					return_string += cell
				else:
					return_string += " "
				
				return_string += "|"
					
			return_string += "\n"
		
		return return_string
				
	def make_move(self, move, player) -> bool:

		# print(move)
		# print(int(move[1]) - 1)

		if move in self.valid_moves:

			# print(self.board_state)
			# print(self.row_letters.index(move[0]))
			# print(self.board_state[self.row_letters.index(move[0])])

			# print("IN VALID MOVES")

			row = self.board_state[self.row_letters.index(move[0])]
			cell = row[int(move[1]) - 1]

			if cell == None:

				row[int(move[1]) - 1] = player

				return True
			else:
				return False


		else:
			return False
		
	def game_over(self) -> bool:

		# 3 horizontal
		for row in self.board_state:

			# print(row)
			# print("TEST")

			if all(element == row[0] for element in row) and row[0] != None:
				self.result = row[0]
				return True

		# 3 vertical
		for i in range(len(self.board_state[0])):
			if self.board_state[0][i] == self.board_state[1][i] == self.board_state[2][i] and self.board_state[0][i] != None:
				self.result = self.board_state[0][i]
				return True

		# 2 diagonal
		if self.board_state[0][0] == self.board_state[1][1] == self.board_state[2][2] and self.board_state[0][0] != None:
			self.result = self.board_state[0][0]
			return True
		if self.board_state[0][2] == self.board_state[1][1] == self.board_state[2][0] and self.board_state[0][2] != None:
			self.result = self.board_state[0][2]
			return True
		
		#Draw
		draw = True
		for row in self.board_state:
			for cell in row:
				if cell == None:
					draw = False
		if draw:
			self.result = "Draw"
		return draw