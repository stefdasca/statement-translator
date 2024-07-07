
Anda has created her own method of encoding numbers. Any number is transformed into a sequence of the characters `.` and `-` as follows: she associates the character `.` with the bit $0$ of the number and the character `-` with the bit $1$ of the number in its base $2$ representation.

# Task

Two natural numbers $a$ and $b$ are given. The task is to print the encoding of those numbers between $a$ and $b$ (including $a$ and $b$) which have the maximum number of $1$ bits in their binary representation.

# Input data

The first line of the input file `morse.in` will contain two integers, $a$ and $b$, separated by a space.

# Output data

The first line of the output file `morse.out` will contain the encodings of the numbers, separated by a space.

# Constraints and clarifications

* $1 \leq a, b \leq 30\ 000$

# Example

`morse.in`
```
7 13
```

`morse.out`
```
--- -.-- --.-
```
