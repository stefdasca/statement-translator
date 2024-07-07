
Gigel has invented a new programming language which he named GCL (Gigel Champion Language). In GCL, up to $26$ variables can be used, denoted by lowercase letters of the English alphabet. The initial value of each variable (at the start of program execution) is $0$. A program written in GCL consists of a sequence of commands, one command per line.

Command|Meaning|
|-|--------|
|**INCEPE**|Marks the beginning of the program (appears only once at the beginning).|
|**`var = expression`**|Assigns to the variable $var$ on the left side of the `=` sign the value of the expression on the right side. An expression consists of one or more terms which may have the `+` operator or the `–` operator (meaning addition and subtraction, respectively). A term can be a constant, a variable, or a variable preceded by a constant (which means the variable is multiplied by the constant). For example, `a = 2b + 4 – c`|
|**REPETA** $n$|Indicates the start of a block of instructions that will be repeated $n$ times.|
|**STOP**|Indicates the end of a **REPETA** block or the end of the program|
|**SCRIE** var|Displays a line in the following form: `var = value` where $var$ represents the name of the variable to be printed, and $value$ represents the value of the variable. The `=` sign must be preceded and followed by a single space.|

# Task

Write a program that reads a program written in the GCL language and meets the following two requirements:
1. determines the number of executed **SCRIE** commands;
2. determines the results displayed by the **SCRIE** commands in the program written in the GCL language.

# Input data

The input file `gcl.in` contains on the first line the task ($1$ or $2$), then on the following lines a **correct** program written in the GCL language.

# Output data

If the task is 1, the output file `gcl.out` will contain on the first line the number of executed **SCRIE** commands.
If the task is 2, the output file `gcl.out` will contain the results displayed by the **SCRIE** commands in the program written in the GCL language, in the order of execution of these commands.

# Constraints and clarifications

* The program in the GCL language will have a maximum of $50$ lines of at most $100$ characters.
* The commands in a GCL program may contain any number of spaces, placed anywhere, but not within the keywords (**REPETA**, **INCEPE**, **STOP**, **SCRIE**) and constants.
* Constants that appear in expressions are natural numbers, ranging from $0$ to $2 \ 000 \ 000 \ 000$.
* The number $n$ that appears in **REPETA** commands is a natural number, $0 \leq n \leq 10$.
* There cannot be nested **REPETA** commands. Specifically, after a **REPETA** command and until **STOP**, which marks the end of **REPETA**, there cannot be another **REPETA** command.
* The values calculated in expressions are, at any time, integers in the interval $[-2^{31}$, $2^{31}-1]$.
* All keywords in GCL commands are written in uppercase letters.
* For task 1, $40\\%$ of the score will be awarded, while for task 2, $60\\%$ of the score will be awarded.

# Example 1

`gcl.in`
```
1
INCEPE
   a = 1
   b = a
   SCRIE a
   SCRIE b
   REPETA 10
      c = a + b
      a = b
      b = c
      SCRIE c
   STOP
STOP
```

`gcl.out`
```
12
```

# Example 2

`gcl.in`
```
2
INCEPE
   n = 10
   k = 1
   REPETA 9
      n = n + k
      SCRIE n
      k = 3 – k
   STOP
STOP
```

`gcl.out`
```
n = 11
n = 13
n = 14
n = 16
n = 17
n = 19
n = 20
n = 22
n = 23
```

# Example 3

`gcl.in`
```
2
INCEPE
   x = 1
   REPETA 10
      x = 2x
   STOP
   SCRIE x
STOP
```

`gcl.out`
```
x = 1024
```
