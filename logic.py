current_symbol = 'X'

game_stats = {
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

def put(postition):
	if game_stats[postition] != " ":
		return False
	global current_symbol
	game_stats[postition] = current_symbol
	current_symbol = (lambda: 'X' if current_symbol == 'O' else 'O')()
	return True

def have_winner():
	return (game_stats["1-A"] == game_stats["1-B"] == game_stats["1-C"] != " ") or (game_stats["2-A"] == game_stats["2-B"] == game_stats["2-C"] != " ") or (game_stats["3-A"] == game_stats["3-B"] == game_stats["3-C"] != " ") or (game_stats["1-A"] == game_stats["2-A"] == game_stats["3-A"] != " ") or (game_stats["1-B"] == game_stats["2-B"] == game_stats["3-B"] != " ") or (game_stats["1-A"] == game_stats["2-B"] == game_stats["3-C"] != " ") or (game_stats["1-C"] == game_stats["2-B"] == game_stats["3-A"] != " ")
