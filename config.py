# Imports
from colorama import Fore as F, Back as B, Style as S
from utils import get_terminal_width

# Info
info = f""" {F.GREEN + S.BRIGHT}Brainfuck Interpreter By AloneTeam{F.RESET + S.NORMAL}
 Version: 1.00
 GitHub: {F.BLUE}https://github.com/Alone228YT/Brainfuck-Interpreter{F.RESET}
 E-mail: alonenet.sup@gmail.com
 Telegram
   ├ AloneNet:  @AloneNet_Official
   ├ AloneChat: @AloneNet_Chat
   └ AloneTeam: @AloneTeam_Adapter

 {F.CYAN}python brainfuck.py [<file.bf>|-stdin|-e|-h|-a|-t]{F.RESET}

 optional arguments:
   <file.bf>            Brainfuck script file
   --stdin              STDIN
   -e, --experimental   Experimental mode
   -h, --help           Show help
   -a, --ascii          Show ASCII table
   -t, --tutorial       Show Brainfuck tutorial"""

# Brainfuck tutorial
bf_tutorial = f""" {S.BRIGHT}Brainfuck uses only eight symbols, each with a specific function:{S.NORMAL}

 {S.BRIGHT}1. > (Move pointer right){S.NORMAL}
	This command moves the data pointer one cell to the right. It's like
	shifting your focus to the next memory location.

 {S.BRIGHT}2. < (Move pointer left){S.NORMAL}
	This command moves the data pointer one cell to the left. It shifts
	your focus to the previous memory location.

 {S.BRIGHT}3. + (Increment data){S.NORMAL}
	This command increases the value stored in the current cell by one.
	It adds 1 to the value.

 {S.BRIGHT}4. - (Decrement data){S.NORMAL}
	This command decreases the value stored in the current cell by one.
	It subtracts 1 from the value.

 {S.BRIGHT}5. . (Output character){S.NORMAL}
	This command outputs the ASCII character corresponding to the value
	stored in the current cell. It prints the value as a character.

 {S.BRIGHT}6. , (Input character){S.NORMAL}
	This command reads a single character from the input and stores its
	ASCII value in the current cell. It takes a character from the input
	and stores it as a value.

 {S.BRIGHT}7. [ (Jump forward){S.NORMAL}
	This command marks the beginning of a loop. It checks if the value
	in the current cell is zero. If it is, the instruction pointer skips
	to the matching ] (loop end). If the value is not zero, the
	instruction pointer continues to the next instruction.

 {S.BRIGHT}8. ] (Jump backward){S.NORMAL}
	This command marks the end of a loop. It checks if the value in the
	current cell is zero. If it is not, the instruction pointer jumps
	back to the matching [ (loop start). If the value is zero, the
	instruction pointer continues to the next instruction.

 {S.BRIGHT}Note:{S.BRIGHT} Brainfuck is case-sensitive, and
	   any character not in this list is ignored.


 {S.BRIGHT}This interpreter reacts to 1 more character: ?{S.NORMAL}
	This command shows the value stored in the current cell.
	(for convenience)

 You can find some examples of Brainfuck code on GitHub
 {F.BLUE}https://github.com/Alone228YT/Brainfuck-Interpreter{F.RESET}"""