# Imports
from colorama import Fore as F, Back as B, Style as S

NUMPAD = {
	"PADENTER": "\n",
	"PADPLUS": "+",
	"PADMINUS": "-",
	"PADSTAR": "*",
	"PADSLASH": "/"
}

# ASCII table
ASCII_table = f"""
{B.BLUE} Bin        Dec   Hex  Char                        Abbr   Printable        {B.RESET}
===========================================================================
 0000 0000 | 0   | 00 | Null                      | NUL  | NO
 0000 0001 | 1   | 01 | Start of Heading          | SOH  | NO
 0000 0010 | 2   | 02 | Start of Text             | STX  | NO
 0000 0011 | 3   | 03 | End of Text               | ETX  | NO
 0000 0100 | 4   | 04 | End of Transmission       | EOT  | NO
 0000 0101 | 5   | 05 | Enquiry                   | ENQ  | NO
 0000 0110 | 6   | 06 | Acknowledge               | ACK  | NO
 0000 0111 | 7   | 07 | Bell                      | BEL  | NO
 0000 1000 | 8   | 08 | Backspace                 | BS   | NO
 0000 1001 | 9   | 09 | Horizontal Tab            | HT   | NO
 0000 1010 | 10  | 0A | Line Feed                 | LF   | YES
 0000 1011 | 11  | 0B | Vertical Tab              | VT   | NO
 0000 1100 | 12  | 0C | Form Feed                 | FF   | NO
 0000 1101 | 13  | 0D | Carriage Return           | CR   | IN SOME SYSTEMS
 0000 1110 | 14  | 0E | Shift Out                 | SO   | NO
 0000 1111 | 15  | 0F | Shift In                  | SI   | NO
 0001 0000 | 16  | 10 | Data Link Escape          | DLE  | NO
 0001 0001 | 17  | 11 | Device Control 1 (XON)    | DC1  | NO
 0001 0010 | 18  | 12 | Device Control 2          | DC2  | NO
 0001 0011 | 19  | 13 | Device Control 3 (XOFF)   | DC3  | NO
 0001 0100 | 20  | 14 | Device Control 4          | DC4  | NO
 0001 0101 | 21  | 15 | Negative Acknowledge      | NAK  | NO
 0001 0110 | 22  | 16 | Synchronous Idle          | SYN  | NO
 0001 0111 | 23  | 17 | End of Transmission Block | ETB  | NO
 0001 1000 | 24  | 18 | Cancel                    | CAN  | NO
 0001 1001 | 25  | 19 | End of Medium             | EM   | NO
 0001 1010 | 26  | 1A | Substitute                | SUB  | NO
 0001 1011 | 27  | 1B | Escape                    | ESC  | NO
 0001 1100 | 28  | 1C | File Separator            | FS   | NO
 0001 1101 | 29  | 1D | Group Separator           | GS   | NO
 0001 1110 | 30  | 1E | Record Separator          | RS   | NO
 0001 1111 | 31  | 1F | Unit Separator            | US   | NO
 0010 0000 | 32  | 20 | Space                     |      | YES
 0010 0001 | 33  | 21 | !                         |      | YES
 0010 0010 | 34  | 22 | "                         |      | YES
 0010 0011 | 35  | 23 | #                         |      | YES
 0010 0100 | 36  | 24 | $                         |      | YES
 0010 0101 | 37  | 25 | %                         |      | YES
 0010 0110 | 38  | 26 | &                         |      | YES
 0010 0111 | 39  | 27 | '                         |      | YES
 0010 1000 | 40  | 28 | (                         |      | YES
 0010 1001 | 41  | 29 | )                         |      | YES
 0010 1010 | 42  | 2A | *                         |      | YES
 0010 1011 | 43  | 2B | +                         |      | YES
 0010 1100 | 44  | 2C | ,                         |      | YES
 0010 1101 | 45  | 2D | -                         |      | YES
 0010 1110 | 46  | 2E | .                         |      | YES
 0010 1111 | 47  | 2F | /                         |      | YES
 0011 0000 | 48  | 30 | 0                         |      | YES
 0011 0001 | 49  | 31 | 1                         |      | YES
 0011 0010 | 50  | 32 | 2                         |      | YES
 0011 0011 | 51  | 33 | 3                         |      | YES
 0011 0100 | 52  | 34 | 4                         |      | YES
 0011 0101 | 53  | 35 | 5                         |      | YES
 0011 0110 | 54  | 36 | 6                         |      | YES
 0011 0111 | 55  | 37 | 7                         |      | YES
 0011 1000 | 56  | 38 | 8                         |      | YES
 0011 1001 | 57  | 39 | 9                         |      | YES
 0011 1010 | 58  | 3A | :                         |      | YES
 0011 1011 | 59  | 3B | ;                         |      | YES
 0011 1100 | 60  | 3C | <                         |      | YES
 0011 1101 | 61  | 3D | =                         |      | YES
 0011 1110 | 62  | 3E | >                         |      | YES
 0011 1111 | 63  | 3F | ?                         |      | YES
 0100 0000 | 64  | 40 | @                         |      | YES
 0100 0001 | 65  | 41 | A                         |      | YES
 0100 0010 | 66  | 42 | B                         |      | YES
 0100 0011 | 67  | 43 | C                         |      | YES
 0100 0100 | 68  | 44 | D                         |      | YES
 0100 0101 | 69  | 45 | E                         |      | YES
 0100 0110 | 70  | 46 | F                         |      | YES
 0100 0111 | 71  | 47 | G                         |      | YES
 0100 1000 | 72  | 48 | H                         |      | YES
 0100 1001 | 73  | 49 | I                         |      | YES
 0100 1010 | 74  | 4A | J                         |      | YES
 0100 1011 | 75  | 4B | K                         |      | YES
 0100 1100 | 76  | 4C | L                         |      | YES
 0100 1101 | 77  | 4D | M                         |      | YES
 0100 1110 | 78  | 4E | N                         |      | YES
 0100 1111 | 79  | 4F | O                         |      | YES
 0101 0000 | 80  | 50 | P                         |      | YES
 0101 0001 | 81  | 51 | Q                         |      | YES
 0101 0010 | 82  | 52 | R                         |      | YES
 0101 0011 | 83  | 53 | S                         |      | YES
 0101 0100 | 84  | 54 | T                         |      | YES
 0101 0101 | 85  | 55 | U                         |      | YES
 0101 0110 | 86  | 56 | V                         |      | YES
 0101 0111 | 87  | 57 | W                         |      | YES
 0101 1000 | 88  | 58 | X                         |      | YES
 0101 1001 | 89  | 59 | Y                         |      | YES
 0101 1010 | 90  | 5A | Z                         |      | YES
 0101 1011 | 91  | 5B | [                         |      | YES
 0101 1100 | 92  | 5C | \\                         |      | YES
 0101 1101 | 93  | 5D | ]                         |      | YES
 0101 1110 | 94  | 5E | ^                         |      | YES
 0101 1111 | 95  | 5F | _                         |      | YES
 0110 0000 | 96  | 60 | `                         |      | YES
 0110 0001 | 97  | 61 | a                         |      | YES
 0110 0010 | 98  | 62 | b                         |      | YES
 0110 0011 | 99  | 63 | c                         |      | YES
 0110 0100 | 100 | 64 | d                         |      | YES
 0110 0101 | 101 | 65 | e                         |      | YES
 0110 0110 | 102 | 66 | f                         |      | YES
 0110 0111 | 103 | 67 | g                         |      | YES
 0110 1000 | 104 | 68 | h                         |      | YES
 0110 1001 | 105 | 69 | i                         |      | YES
 0110 1010 | 106 | 6A | j                         |      | YES
 0110 1011 | 107 | 6B | k                         |      | YES
 0110 1100 | 108 | 6C | l                         |      | YES
 0110 1101 | 109 | 6D | m                         |      | YES
 0110 1110 | 110 | 6E | n                         |      | YES
 0110 1111 | 111 | 6F | o                         |      | YES
 0111 0000 | 112 | 70 | p                         |      | YES
 0111 0001 | 113 | 71 | q                         |      | YES
 0111 0010 | 114 | 72 | r                         |      | YES
 0111 0011 | 115 | 73 | s                         |      | YES
 0111 0100 | 116 | 74 | t                         |      | YES
 0111 0101 | 117 | 75 | u                         |      | YES
 0111 0110 | 118 | 76 | v                         |      | YES
 0111 0111 | 119 | 77 | w                         |      | YES
 0111 1000 | 120 | 78 | x                         |      | YES
 0111 1001 | 121 | 79 | y                         |      | YES
 0111 1010 | 122 | 7A | z                         |      | YES
 0111 1011 | 123 | 7B | """+"{"+"""                         |      | YES
 0111 1100 | 124 | 7C | |                         |      | YES
 0111 1101 | 125 | 7D | }                         |      | YES
 0111 1110 | 126 | 7E | ~                         |      | YES
 0111 1111 | 127 | 7F | Delete                    | DEL  | NO
 1000 0000 | 128 | 80 | €                         |      | NO
 1000 0001 | 129 | 81 |                           |      | UNUSED
 1000 0010 | 130 | 82 | ‚                         |      | NO
 1000 0011 | 131 | 83 | ƒ                         |      | NO
 1000 0100 | 132 | 84 | „                         |      | NO
 1000 0101 | 133 | 85 | …                         |      | NO
 1000 0110 | 134 | 86 | †                         |      | NO
 1000 0111 | 135 | 87 | ‡                         |      | NO
 1000 1000 | 136 | 88 | ˆ                         |      | NO
 1000 1001 | 137 | 89 | ‰                         |      | NO
 1000 1010 | 138 | 8A | Š                         |      | NO
 1000 1011 | 139 | 8B | ‹                         |      | NO
 1000 1100 | 140 | 8C | Œ                         |      | NO
 1000 1101 | 141 | 8D |                           |      | NO
 1000 1110 | 142 | 8E | Ž                         |      | NO
 1000 1111 | 143 | 8F |                           |      | UNUSED
 1001 0000 | 144 | 90 |                           |      | UNUSED
 1001 0001 | 145 | 91 | ‘                         |      | NO
 1001 0010 | 146 | 92 | ’                         |      | NO
 1001 0011 | 147 | 93 | “                         |      | NO
 1001 0100 | 148 | 94 | ”                         |      | NO
 1001 0101 | 149 | 95 | •                         |      | NO
 1001 0110 | 150 | 96 | –                         |      | NO
 1001 0111 | 151 | 97 | —                         |      | NO
 1001 1000 | 152 | 98 | ˜                         |      | NO
 1001 1001 | 153 | 99 | ™                         |      | NO
 1001 1010 | 154 | 9A | š                         |      | NO
 1001 1011 | 155 | 9B | ›                         |      | NO
 1001 1100 | 156 | 9C | œ                         |      | NO
 1001 1101 | 157 | 9D |                           |      | UNUSED
 1001 1110 | 158 | 9E | ž                         |      | NO
 1001 1111 | 159 | 9F | Ÿ                         |      | NO
 1010 0000 | 160 | A0 | Non-breaking space        | NBSP | NO
 1010 0001 | 161 | A1 | ¡                         |      | YES
 1010 0010 | 162 | A2 | ¢                         |      | YES
 1010 0011 | 163 | A3 | £                         |      | YES
 1010 0100 | 164 | A4 | ¤                         |      | YES
 1010 0101 | 165 | A5 | ¥                         |      | YES
 1010 0110 | 166 | A6 | ¦                         |      | YES
 1010 0111 | 167 | A7 | §                         |      | YES
 1010 1000 | 168 | A8 | ¨                         |      | YES
 1010 1001 | 169 | A9 | ©                         |      | YES
 1010 1010 | 170 | AA | ª                         |      | YES
 1010 1011 | 171 | AB | «                         |      | YES
 1010 1100 | 172 | AC | ¬                         |      | YES
 1010 1101 | 173 | AD | Soft hyphen               | SHY  | NO
 1010 1110 | 174 | AE | ®                         |      | YES
 1010 1111 | 175 | AF | ¯                         |      | YES
 1011 0000 | 176 | B0 | °                         |      | YES
 1011 0001 | 177 | B1 | ±                         |      | YES
 1011 0010 | 178 | B2 | ²                         |      | YES
 1011 0011 | 179 | B3 | ³                         |      | YES
 1011 0100 | 180 | B4 | ´                         |      | YES
 1011 0101 | 181 | B5 | µ                         |      | YES
 1011 0110 | 182 | B6 | ¶                         |      | YES
 1011 0111 | 183 | B7 | ·                         |      | YES
 1011 1000 | 184 | B8 | ¸                         |      | YES
 1011 1001 | 185 | B9 | ¹                         |      | YES
 1011 1010 | 186 | BA | º                         |      | YES
 1011 1011 | 187 | BB | »                         |      | YES
 1011 1100 | 188 | BC | ¼                         |      | YES
 1011 1101 | 189 | BD | ½                         |      | YES
 1011 1110 | 190 | BE | ¾                         |      | YES
 1011 1111 | 191 | BF | ¿                         |      | YES
 1100 0000 | 192 | C0 | À                         |      | YES
 1100 0001 | 193 | C1 | Á                         |      | YES
 1100 0010 | 194 | C2 | Â                         |      | YES
 1100 0011 | 195 | C3 | Ã                         |      | YES
 1100 0100 | 196 | C4 | Ä                         |      | YES
 1100 0101 | 197 | C5 | Å                         |      | YES
 1100 0110 | 198 | C6 | Æ                         |      | YES
 1100 0111 | 199 | C7 | Ç                         |      | YES
 1100 1000 | 200 | C8 |	È                         |      | YES
 1100 1001 | 201 | C9 |	É                         |      | YES
 1100 1010 | 202 | CA |	Ê                         |      | YES
 1100 1011 | 203 | CB |	Ë                         |      | YES
 1100 1100 | 204 | CC |	Ì                         |      | YES
 1100 1101 | 205 | CD |	Í                         |      | YES
 1100 1110 | 206 | CE |	Î                         |      | YES
 1100 1111 | 207 | CF |	Ï                         |      | YES
 1101 0000 | 208 | D0 |	Ð                         |      | YES
 1101 0001 | 209 | D1 |	Ñ                         |      | YES
 1101 0010 | 210 | D2 |	Ò                         |      | YES
 1101 0011 | 211 | D3 |	Ó                         |      | YES
 1101 0100 | 212 | D4 |	Ô                         |      | YES
 1101 0101 | 213 | D5 |	Õ                         |      | YES
 1101 0110 | 214 | D6 |	Ö                         |      | YES
 1101 0111 | 215 | D7 |	×                         |      | YES
 1101 1000 | 216 | D8 |	Ø                         |      | YES
 1101 1001 | 217 | D9 |	Ù                         |      | YES
 1101 1010 | 218 | DA |	Ú                         |      | YES
 1101 1011 | 219 | DB |	Û                         |      | YES
 1101 1100 | 220 | DC |	Ü                         |      | YES
 1101 1101 | 221 | DD |	Ý                         |      | YES
 1101 1110 | 222 | DE |	Þ                         |      | YES
 1101 1111 | 223 | DF |	ß                         |      | YES
 1110 0000 | 224 | E0 |	à                         |      | YES
 1110 0001 | 225 | E1 |	á                         |      | YES
 1110 0010 | 226 | E2 |	â                         |      | YES
 1110 0011 | 227 | E3 |	ã                         |      | YES
 1110 0100 | 228 | E4 |	ä                         |      | YES
 1110 0101 | 229 | E5 |	å                         |      | YES
 1110 0110 | 230 | E6 |	æ                         |      | YES
 1110 0111 | 231 | E7 |	ç                         |      | YES
 1110 1000 | 232 | E8 |	è                         |      | YES
 1110 1001 | 233 | E9 |	é                         |      | YES
 1110 1010 | 234 | EA |	ê                         |      | YES
 1110 1011 | 235 | EB |	ë                         |      | YES
 1110 1100 | 236 | EC |	ì                         |      | YES
 1110 1101 | 237 | ED |	í                         |      | YES
 1110 1110 | 238 | EE |	î                         |      | YES
 1110 1111 | 239 | EF |	ï                         |      | YES
 1111 0000 | 240 | F0 |	ð                         |      | YES
 1111 0001 | 241 | F1 |	ñ                         |      | YES
 1111 0010 | 242 | F2 |	ò                         |      | YES
 1111 0011 | 243 | F3 |	ó                         |      | YES
 1111 0100 | 244 | F4 |	ô                         |      | YES
 1111 0101 | 245 | F5 |	õ                         |      | YES
 1111 0110 | 246 | F6 |	ö                         |      | YES
 1111 0111 | 247 | F7 |	÷                         |      | YES
 1111 1000 | 248 | F8 |	ø                         |      | YES
 1111 1001 | 249 | F9 |	ù                         |      | YES
 1111 1010 | 250 | FA |	ú                         |      | YES
 1111 1011 | 251 | FB |	û                         |      | YES
 1111 1100 | 252 | FC |	ü                         |      | YES
 1111 1101 | 253 | FD |	ý                         |      | YES
 1111 1110 | 254 | FE |	þ                         |      | YES
 1111 1111 | 255 | FF |	ÿ                         |      | YES
===========================================================================
"""

# ASCII dict
ASCII = {}
for b in ASCII_table.split("\n"):
	c = b.split(" | ")
	if len(c) < 3: continue
	if c[-1].strip() == "YES" or c[3].strip() in """☻♥♦\n♫☼►◄↕‼¶§▬↨↑↓→←∟↔▲▼ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~⌂ ¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ""":
		if int(c[1].strip()) in [10, 13]:
			ASCII.setdefault(int(c[1].strip()), "\n")
		elif int(c[1].strip()) == 32:
			ASCII.setdefault(int(c[1].strip()), " ")
		else:
			ASCII.setdefault(int(c[1].strip()), c[3].strip())

# Some colors
ASCII_table = ASCII_table.replace("NO", f"{F.RED}NO{F.RESET}").replace("UNUSED", f"{F.RED}UNUSED{F.RESET}").replace("YES", f"{F.GREEN}YES{F.RESET}")