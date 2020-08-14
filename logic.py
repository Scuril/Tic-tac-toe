class Game:
	__grid_size = 3
	__inrow_size = 3

	def __init__(self):
		self.__move_i = 0
		self.have_draw = lambda: self.__move_i == 9

		self.__winner = '-'
		self.current_symbol = 'X'
		self.game_stats = []

		for i in range(self.__grid_size):
			temp = []
			for j in range(self.__grid_size):
				temp.append(" ")

			self.game_stats.append(temp)

	def paint_symbol(self, symbol):
		if symbol == 'X':
			return f"\033[1;31;40m{symbol}\033[1;37;40m"
		elif symbol == 'O':
			return f"\033[1;34;40m{symbol}\033[1;37;40m"

		return symbol

	def put(self, position):
		column = int(position[0]) - 1
		row = ord(position[1].lower()) - 97 # convert char to it's index in alphabet

		if (column >= self.__grid_size or row >= self.__grid_size or 
			column < 0 or row < 0):
			return False
		if self.game_stats[column][row] != " ":
			return False

		self.game_stats[column][row] = self.current_symbol
		self.current_symbol = self.__change_symbol(self.current_symbol)
		self.__move_i += 1
		return True
		

	def have_winner(self):
		if self.is_winner('X'):
			self.__winner = 'X'
			return True
		elif self.is_winner('O'):
			self.__winner = 'O'
			return True

		return False

	def is_winner(self, symbol):

		only_zero_symbol = []

		for i in range(self.__grid_size):
			for j in range(self.__grid_size):
				if self.game_stats[i][j] == symbol and (i == 0 or j == 0):
					only_zero_symbol.append((i, j))

		result = []

		for symbol_pos in only_zero_symbol:
			if symbol_pos[0] - self.__inrow_size >= 0: # north
				result.append(self.__find_round_symbol(symbol, symbol_pos, "n", 1))

			if symbol_pos[0] - self.__inrow_size >= 0 and symbol_pos[1] + self.__inrow_size <= self.__grid_size: # north-east
				result.append(self.__find_round_symbol(symbol, symbol_pos, "ne", 1))

			if symbol_pos[1] + self.__inrow_size <= self.__grid_size: # east
				result.append(self.__find_round_symbol(symbol, symbol_pos, "e", 1))

			if symbol_pos[0] + self.__inrow_size <= self.__grid_size and symbol_pos[1] + self.__inrow_size <= self.__grid_size: # south-east
				result.append(self.__find_round_symbol(symbol, symbol_pos, "se", 1))

			if symbol_pos[0] + self.__inrow_size <= self.__grid_size: # south
				result.append(self.__find_round_symbol(symbol, symbol_pos, "s", 1))

			if symbol_pos[0] + self.__inrow_size <= self.__grid_size and symbol_pos[1] - self.__inrow_size >= 0: # south-west
				result.append(self.__find_round_symbol(symbol, symbol_pos, "sw", 1))

			if symbol_pos[1] - self.__inrow_size >= 0: # west
				result.append(self.__find_round_symbol(symbol, symbol_pos, "w", 1))

			if symbol_pos[0] - self.__inrow_size >= 0 and symbol_pos[1] - self.__inrow_size >= 0: # north-west
				result.append(self.__find_round_symbol(symbol, symbol_pos, "nw", 1))
			

		return any(result)

	def get_winner(self):
		if self.__winner == '-':
			raise Exception("Have not winner yet")

		return self.__winner

	def print_grid(self):
		print("\033[1;37;40m", end = '')
		frow = " "
		for i in range(self.__grid_size):
			frow += f" {i+1}"

		print(frow)

		for i in range(self.__grid_size):
			row = chr(i + 97).upper()
			for j in range(self.__grid_size):
				row += f" {self.paint_symbol(self.game_stats[j][i])}"

			print(row)

	def __change_symbol(self, symbol):
		if symbol == 'X':
			return 'O'
		else:
			return 'X'

	def __find_round_symbol(self, symbol, pos, direction, depth):
		if depth == self.__inrow_size:
			return True

		if direction == "n": # north
			npos = (pos[0]-1, pos[1])
			if self.game_stats[npos[0]][npos[1]] == symbol:
				return self.__find_round_symbol(symbol, npos, "n", depth+1)
			else:
				return False
		elif direction == "ne": # north-east
			npos = (pos[0]-1, pos[1]+1)
			if self.game_stats[npos[0]][npos[1]] == symbol:
				return self.__find_round_symbol(symbol, npos, "ne", depth+1)
			else:
				return False
		elif direction == "e": # east
			npos = (pos[0], pos[1]+1)
			if self.game_stats[npos[0]][npos[1]] == symbol:
				return self.__find_round_symbol(symbol, npos, "e", depth+1)
			else:
				return False
		elif direction == "se": # south-east
			npos = (pos[0]+1, pos[1]+1)
			if self.game_stats[npos[0]][npos[1]] == symbol:
				return self.__find_round_symbol(symbol, npos, "se", depth+1)
			else:
				return False
		elif direction == "s": # south
			npos = (pos[0]+1, pos[1])
			if self.game_stats[npos[0]][npos[1]] == symbol:
				return self.__find_round_symbol(symbol, npos, "s", depth+1)
			else:
				return False
		elif direction == "sw": # south-west
			npos = (pos[0]+1, pos[1]-1)
			if self.game_stats[npos[0]][npos[1]] == symbol:
				return self.__find_round_symbol(symbol, npos, "sw", depth+1)
			else:
				return False
		elif direction == "w": # west
			npos = (pos[0], pos[1]-1)
			if self.game_stats[npos[0]][npos[1]] == symbol:
				return self.__find_round_symbol(symbol, npos, "w", depth+1)
			else:
				return False
		elif direction == "nw": # north-west
			npos = (pos[0]-1, pos[1]-1)
			if self.game_stats[npos[0]][npos[1]] == symbol:
				return self.__find_round_symbol(symbol, npos, "nw", depth+1)
			else:
				return False

