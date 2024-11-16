from argparse import ArgumentParser
from utils import get_terminal_width, Error
from config import info, bf_tutorial
from ASCII import ASCII_table
import os, sys
from colorama import Fore as F, Back as B, Style as S

parser = ArgumentParser(description="Brainfuck interpreter", add_help=False)
# Add arguments
parser.add_argument('file', type=str, nargs='?', default=None, help="Braifuck script")
parser.add_argument('-stdin', '--stdin', type=str, nargs='?', default=None, help="stdin")
parser.add_argument('-e', '--experimental', action='store_true', help="experimantal mode")
parser.add_argument('-i', '--info', '-h', '--help', action='store_true', help="show info")
parser.add_argument('-a', '--ascii', action='store_true', help="show ASCII table")
parser.add_argument('-t', '--tutorial', action='store_true', help="show Brainfuck tutorial")

def args_reader():
	args = parser.parse_args()
	width = get_terminal_width()
	if args.info:
		# Info output
		print(F.GREEN + S.BRIGHT + ("=" * (width - 1)))
		print(info)
		print(F.GREEN + S.BRIGHT + ("=" * (width - 1)))

	if args.ascii:
		# ASCII table output
		print(ASCII_table)

	if args.tutorial:
		# Brainfuck tutorial output
		print(F.GREEN + S.BRIGHT + ("=" * (width - 1)))
		print(bf_tutorial)
		print(F.GREEN + S.BRIGHT + ("=" * (width - 1)))


	if not any(vars(args).values()):
		raise Error(f"USE          {F.CYAN}python brainfuck.py <file.bf>{F.RESET}\n\
OR SEE HELP  {F.CYAN}python brainfuck.py -h{F.RESET}")

	if args.stdin and not args.file:
		raise Error(f"ERROR: you need to use file with stdin.\n\
USE    {F.CYAN}python brainfuck.py <file.bf> --stdin{F.RESET}")

	if args.experimental and not args.file:
		raise Error(f"ERROR: you need to use file with experimental mode.\n\
USE    {F.CYAN}python brainfuck.py <file.bf> -e{F.RESET}")

	if not args.file:
		sys.exit(0)

	file = args.file

	# Check if file exists
	if not os.path.exists(file):
		raise Error(f"File  '{file}'  doesn't exists.")

	# Get Brainfuck code from file
	with open(file, "r", encoding="utf-8") as file:
		code = file.read()

	stdin = list(args.stdin) if args.stdin else []

	experimental_mode = True if args.experimental else False
	
	return code, experimental_mode, stdin