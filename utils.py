# Imports
import sys, shutil
from colorama import Fore as F, Back as B, Style as S

# Functions
def Error(message, _exit=True):
	# Get terminal width
	width = get_terminal_width()
	
	message = " " + message.replace("\n", "\n ")
	
	# Error output
	print(F.RED + S.BRIGHT + ("=" * (width - 1)))
	print(message)
	print(F.RED + S.BRIGHT + ("=" * (width - 1)), end="" if _exit else "\n")
	
	# Program termination
	if _exit: sys.exit(1)

def BrainfuckRuntimeError(message, line, column, _exit=True):
	location = f" at line {line}, column {column}" if line and column else ""
	Error(f"{message}{location}", _exit)

def get_terminal_width():
	# Get terminal size
	terminal_size = shutil.get_terminal_size()
	# Get terminal width
	width = terminal_size.columns
	return width

def handle_sigint(signum, frame):
	raise KeyboardInterrupt