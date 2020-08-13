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
	global current_symbol
	game_stats[postition] = current_symbol
	current_symbol = (lambda: 'X' if current_symbol == 'O' else 'O')()

def have_winner():
	pass
