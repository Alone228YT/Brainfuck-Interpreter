# Imports
import sys
import curses
import traceback
from colorama import Fore as F, Back as B, Style as S
from ASCII import ASCII, NUMPAD
from utils import Error, BrainfuckRuntimeError

# Interpreter
class Interpreter():
	def __init__(self, stdscr, code, experimental_mode, stdin):
		# Variables
		self.code = code
		self.experimental_mode = experimental_mode
		self.stdin = stdin
		self.memory_cells = [0]
		self.memory_pointer = 0
		self._output = ""
		self.i = 0
		self.last_i = 0
		self.line = 1
		self.column = 1
		self.stack = []

		curses.cbreak()
		stdscr.keypad(True)

		# Terminal size
		self.height, self.width = stdscr.getmaxyx()

		# Create window for input
		self.output_win = curses.newwin(self.height - 2, self.width, 0, 0)
		self.output_win.scrollok(True)
		
		self.input_win = curses.newwin(2, self.width, self.height - 2, 0)
		self.input_win.addstr("Ctrl + C to EXIT\n")
		self.input_win.addstr("Input: ")
		self.input_win.keypad(True)
		self.input_win.refresh()
		try:
			self.run()

		except KeyboardInterrupt:
			if self._output: self.result()
			Error("The program has been terminated by user.")
		
		except SystemExit: pass
		except: Error(traceback.format_exc()[:-1])

		finally:
			# End curses
			curses.nocbreak()
			stdscr.keypad(False)
			curses.endwin()

	def run(self):
		while self.i < len(self.code):
			char = self.code[self.i]
			if char == "\n":
				self.line += 1
				self.column = 0
			else:
				self.column += self.i-self.last_i
			self.last_i = self.i

			if not char in "><+-.,[]?": self.i += 1; continue
			self.handle_char(char)
			self.i += 1
		
		self.result()
		if self.stack:
			for char in self.stack: BrainfuckRuntimeError("Unmatched '[' detected", char[1], char[2], _exit=char == self.stack[-1])

	def handle_char(self, char):
		if len(self.memory_cells) == self.memory_pointer: self.memory_cells.append(0)
		
		if char == ">":
			self.memory_pointer += 1
		
		elif char == "<":
			if self.memory_pointer == 0:
				self.error('Attempt to access a negative memory location')
			else: self.memory_pointer -= 1
		
		elif char == "+":
			self.memory_cells[self.memory_pointer] = (self.memory_cells[self.memory_pointer] + 1) % 256

		elif char == "-":
			self.memory_cells[self.memory_pointer] = (self.memory_cells[self.memory_pointer] - 1) % 256

		elif char == ".":
			if self.memory_cells[self.memory_pointer] in ASCII.keys(): self.output(ASCII[self.memory_cells[self.memory_pointer]])
			else:
				try: self.output(chr(self.memory_cells[self.memory_pointer]))
				except: self.output(" ")

		elif char == ",":
			_char = self.input()
			if _char in ASCII.values():
				self.memory_cells[self.memory_pointer] = next((k for k, v in ASCII.items() if v == _char), None)
			else:
				self.memory_cells[self.memory_pointer] = ord(_char)

		elif char == "[":
			if self.memory_cells[self.memory_pointer] == 0:
				self.open_brackets = 1
				while self.open_brackets > 0:
					self.i += 1
					if self.code[self.i] == '[':
						self.open_brackets += 1
					elif self.code[self.i] == ']':
						self.open_brackets -= 1
			else:
				self.stack.append((self.i, self.line, self.column))
		
		elif char == "]":
			if not self.stack:
				self.error("Unmatched ']' detected")
			if self.memory_cells[self.memory_pointer] != 0:
				self.i = self.stack[-1][0]
			else:
				self.stack.pop()

		elif char == "?":
			self.output("\n" + str(self.memory_cells[self.memory_pointer]) + "\n")

	def error(self, message):
		if self._output:
			self.result()
		BrainfuckRuntimeError(message, self.line, self.column)

	def input(self):
		self.input_win.clear()
		self.input_win.addstr("Ctrl + C to EXIT\n")
		self.input_win.addstr("Input: ")
		self.input_win.refresh()
		_char = 0
		while _char in [0, 8, 127]:
			if len(self.stdin) == 0: _char = self.input_win.getkey()
			else: _char = self.stdin[0]; self.stdin.pop(0)
			if _char in NUMPAD:
				_char = NUMPAD[_char]
			try:
				_char = ord(_char)
			except:
				_char = 0
		
		return chr(_char)

	def output(self, text):
		self.output_win.addstr(text)
		self.output_win.refresh()
		self._output += text

	def result(self):
		print(F.GREEN + S.BRIGHT + ("=" * (self.width - 1)))
		print(self._output)
		if self.experimental_mode:
			print(F.YELLOW + S.BRIGHT + ("=" * (self.width - 1)))
			print("MEMORY CELLS:\n", self.memory_cells, "\nMEMORY POINTER:\n", self.memory_pointer)