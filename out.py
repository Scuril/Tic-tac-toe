from Color_Console import *
import platform
import re

from logic import *

def clear_console():
	if is_linux:
		os.system('clear')
	else:
		os.system('cls')

def print_grid(game):
	print("  1 2 3")
	print(f"A {game.game_stats['1-A']} {game.game_stats['2-A']} {game.game_stats['3-A']}")
	print(f"B {game.game_stats['1-B']} {game.game_stats['2-B']} {game.game_stats['3-B']}")
	print(f"C {game.game_stats['1-C']} {game.game_stats['2-C']} {game.game_stats['3-C']}")
	print("")

def get_move():
	move = input()
	while not re.match("(1|2|3)-(A|B|C)", move):
		print("Please observe format")
		move = input()
	return move

if __name__ == "__main__":
	game = Game()
	is_linux = platform.system()
	counter = 0
	
	while not game.have_winner():
		clear_console()

		print_grid(game)

		if counter == 9:
			print("Draw")
			break

		print(f"Now {game.current_symbol} move")
		print("*Move must be printed in format DIGIT-SYMBOL where DIGIT is column, SYMBOL is row as on the above grid")

		move = get_move()

		while not game.put(move):
			print("Wrong move")
			move = get_move()
			

		counter += 1
	else:
		print(f"Winner is {(lambda: 'X' if game.current_symbol == 'O' else 'O')()}")
