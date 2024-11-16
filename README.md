# Brainfuck-Interpreter
<b>Brainfuck Interpreter on Python By AloneTeam</b><br>
<b>Version:</b> 1.00<br>
<b>E-mail:</b> alonenet.sup@gmail.com<br>
<b>Telegram</b><br>
&nbsp;&nbsp;├ <b>AloneNet:</b>  https://t.me/AloneNet_Official<br>
&nbsp;&nbsp;├ <b>AloneChat:</b> https://t.me/AloneNet_Chat<br>
&nbsp;&nbsp;└ <b>AloneTeam:</b> https://t.me/AloneTeam_Adapter<br>

# Usage

```
python brainfuck.py [<file.bf>|-stdin|-e|-h|-a|-t]
brainfuck.exe       [<file.bf>|-stdin|-e|-h|-a|-t]

optional arguments:
  <file.bf>            Brainfuck script file
  --stdin              STDIN
  -e, --experimental   Experimental mode
  -h, --help           Show help
  -a, --ascii          Show ASCII table
  -t, --tutorial       Show Brainfuck tutorial
```

# Examples
## Hello, World!
```batch
> python brainfuck.py "brainfuck scripts\hello world.bf"
======================================================
Hello, World!
```

## Brainfuck (experimental mode)
```batch
> python brainfuck.py "brainfuck scripts\brainfuck.bf" -e
======================================================
Brainfuck
======================================================
MEMORY CELLS:
 [0, 107]
MEMORY POINTER:
 1
```

## String reverser (STDIN)
```batch
> python brainfuck.py "brainfuck scripts\string reverser.bf" -stdin="My string!"
======================================================
Input text: My string!

Reversed text: !gnirts yM
```

## Char ASCII: Question mark (?) (experimental mode & stdin)
```batch
> python brainfuck.py "brainfuck scripts\char ascii.bf" -stdin="ABCDE" -e
======================================================
A:
65
B:
66
C:
67
D:
68
E:
69

======================================================
MEMORY CELLS:
 [58, 0, 0, 0, 0]
MEMORY POINTER:
 2
```
