class Game:
	def __init__(self):
		self.__move_i = 0
		self.have_draw = lambda: self.__move_i == 9

		self.current_symbol = 'X'
		self.game_stats = {
			"1-A": " ",
			"1-B": " ",
			"1-C": " ",
			"2-A": " ",
			"2-B": " ",
			"2-C": " ",
			"3-A": " ",
			"3-B": " ",
			"3-C": " "
		}

	def paint_symbol(self, symbol):
		if symbol == 'X':
			return f"\033[1;31;40m{symbol}\033[1;37;40m"
		
		return f"\033[1;34;40m{symbol}\033[1;37;40m"

	def put(self, postition):
		if self.game_stats[postition] != " ":
			return False

		self.game_stats[postition] = self.current_symbol
		self.current_symbol = self.__change_symbol(self.current_symbol)
		self.__move_i += 1
		return True

	def have_winner(self):
		result = [
			self.game_stats["1-A"] == self.game_stats["1-B"] == self.game_stats["1-C"] != " ",
			self.game_stats["2-A"] == self.game_stats["2-B"] == self.game_stats["2-C"] != " ",
			self.game_stats["3-A"] == self.game_stats["3-B"] == self.game_stats["3-C"] != " ",
			self.game_stats["1-A"] == self.game_stats["2-A"] == self.game_stats["3-A"] != " ",
			self.game_stats["1-B"] == self.game_stats["2-B"] == self.game_stats["3-B"] != " ",

			self.game_stats["1-A"] == self.game_stats["2-B"] == self.game_stats["3-C"] != " ",
			self.game_stats["1-C"] == self.game_stats["2-B"] == self.game_stats["3-A"] != " "
		]
		return any(result)

	def get_winner(self):
		if not self.have_winner():
			raise Exception("Have not winner yet")

		return self.__change_symbol(self.current_symbol)

	def print_grid(self):
		print("\033[1;37;40m  1 2 3")
		print(f"A {self.paint_symbol(self.game_stats['1-A'])} {self.paint_symbol(self.game_stats['2-A'])} {self.paint_symbol(self.game_stats['3-A'])}")
		print(f"B {self.paint_symbol(self.game_stats['1-B'])} {self.paint_symbol(self.game_stats['2-B'])} {self.paint_symbol(self.game_stats['3-B'])}")
		print(f"C {self.paint_symbol(self.game_stats['1-C'])} {self.paint_symbol(self.game_stats['2-C'])} {self.paint_symbol(self.game_stats['3-C'])}")

	def __change_symbol(self, symbol):
		if symbol == 'X':
			return 'O'
		else:
			return 'X'

