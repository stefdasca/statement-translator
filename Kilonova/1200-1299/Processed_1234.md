
We define a programming language with assignment and decision instructions. The syntax of the instructions is:

Assignment instruction
```
variable=variable
```

Decision instruction
```
if
sign variable variable
{yes
instructions}
{no
instructions}
fi
```
\
The language variables (`variable`) are identified by a single character, lowercase, from the English alphabet. The values of the variables are integers. The sign (`sign`) can be one of the characters `<`, `>` or `=`. The instruction lines do not contain spaces. Instructions within `{}` can be omitted.

# Task

The initial values of all variables (from $a$ to $z$), in alphabetical order starting with $a$, are given. The task is to determine the values of all variables from $a$ to $z$, after the execution of the program sequence.

# Input data

The input file is `limbaj.in`.

The first line contains the numbers $V_a, V_b, \dots, V_z$, separated by a space, representing the initial values of the variables from $a$ to $z$.

The following lines, until the end of the file, contain lines of the program, with syntactically correct instructions.

# Output data

The output file is `limbaj.out`.

The first line contains the numbers $V_a, V_b, \dots, V_z$, separated by a space.

# Constraints and clarifications

* $-30\ 000 < a, b, \dots, z < 30\ 000$;
* The number of program lines is less than $10\ 000$;
* The language is case sensitive (only lowercase letters from $a$ to $z$ are used).

# Example

`limbaj.in`
```
1 3 5 7 4 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
if
=ab
no
if
<ab
yes
b=d
fi
f=d
fi
```

`limbaj.out`
```
1 7 5 7 4 0 7 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
```
