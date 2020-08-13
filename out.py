from Color_Console import *
import platform
import re

from logic import *

if __name__ == "__main__":
	is_linux = platform.system()
	
	while not have_winner():
		#game stats
		print("  1 2 3")
		print(f"A {game_stats['1-A']} {game_stats['2-A']} {game_stats['3-A']}")
		print(f"B {game_stats['1-B']} {game_stats['2-B']} {game_stats['3-B']}")
		print(f"C {game_stats['1-C']} {game_stats['2-C']} {game_stats['3-C']}")
		print("")

		print(f"Now {current_symbol} move")
		print("*Move must be printed in format DIGIT-SYMBOL where DIGIT is column, SYMBOL is row as on the above grid")

		move = input()
		while not re.match("(1|2|3)-(A|B|C)", move):
			print("Please observe format")
			move = input()

		put(move)

		current_symbol = (lambda: 'X' if current_symbol == 'O' else 'O')()

		#clearing
		if is_linux:
			os.system('clear')
		else:
			os.system('cls')

	print(f"Winner is {(lambda: 'X' if current_symbol == 'O' else 'O')()}")
		

