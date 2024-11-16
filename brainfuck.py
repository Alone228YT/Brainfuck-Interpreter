import signal
import curses
from args import args_reader
from utils import handle_sigint
from interpreter import Interpreter
import colorama
from colorama import Fore as F, Back as B, Style as S

# Initialization
stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(True)

colorama.init(autoreset=True)
try:
    colorama.just_fix_windows_console()
except:
    pass


def main():
	# Get data from arguments
	code, experimental_mode, stdin = args_reader()

	# Register a signal handler for Ctrl + C
	signal.signal(signal.SIGINT, handle_sigint)

	# Run the function via curses in the main thread
	curses.wrapper(lambda stdcr: Interpreter(stdscr, code, experimental_mode, stdin))

# Program launch
if __name__ == "__main__":
	main()