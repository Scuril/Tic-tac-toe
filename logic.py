class Game:
	def __init__(self):
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

	def put(self, postition):
		if self.game_stats[postition] != " ":
			return False
			
		self.game_stats[postition] = self.current_symbol
		self.current_symbol = (lambda: 'X' if self.current_symbol == 'O' else 'O')()
		return True

	def have_winner(self):
		return (self.game_stats["1-A"] == self.game_stats["1-B"] == self.game_stats["1-C"] != " ") or (self.game_stats["2-A"] == self.game_stats["2-B"] == self.game_stats["2-C"] != " ") or (self.game_stats["3-A"] == self.game_stats["3-B"] == self.game_stats["3-C"] != " ") or (self.game_stats["1-A"] == self.game_stats["2-A"] == self.game_stats["3-A"] != " ") or (self.game_stats["1-B"] == self.game_stats["2-B"] == self.game_stats["3-B"] != " ") or (self.game_stats["1-A"] == self.game_stats["2-B"] == self.game_stats["3-C"] != " ") or (self.game_stats["1-C"] == self.game_stats["2-B"] == self.game_stats["3-A"] != " ")
