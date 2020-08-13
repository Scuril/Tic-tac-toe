from Color_Console import *
import platform
import re

from logic import *

def clear_console():
	if is_linux:
		os.system('clear')
	else:
		os.system('cls')

def get_move():
	move = input().upper()
	while not re.match("(1|2|3)-(A|B|C)", move):
		print("Please observe format")
		move = input().upper()
	return move

if __name__ == "__main__":
	game = Game()
	is_linux = platform.system()
	
	while not game.have_winner() and not game.have_draw():
		clear_console()

		game.print_grid()
		print("")

		print(f"Now {game.current_symbol} move")
		print("*Move must be printed in format DIGIT-SYMBOL where DIGIT is column, SYMBOL is row as on the above grid")

		move = get_move()

		while not game.put(move):
			print("Wrong move")
			move = get_move()

	else:
		clear_console()
		game.print_grid()
		print("")
		
		if game.have_winner():
			print(f"Winner is {game.get_winner()}")
		else:
			print("Draw")
