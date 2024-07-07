
Rail Fence Cipher, known as the zigzag cipher, is a method of encoding messages using a grid where the text is written starting from the top-left corner, diagonally from top to bottom, and then, after writing the character on the last line, continues diagonally from bottom to top, as in the example. The number of lines in the grid is the *encoding key*. After the text has been written in this way, the encoded message is obtained by traversing the lines from top to bottom and taking all the characters from left to right on each line.
If we want to encode the text `OLIMPIADA DE INFORMATICA`, with an *encoding key* $6$, then proceed as follows:
1. Write the text in zigzag in the grid;
~[zigzag.png|align=center]
2. Take the characters by lines and form the encoded message: `ODTL EAIIA MCMDIRAPANOIF`.

# Task

Write a program that reads the *encoding key* and an encoded text, and determines the decoded message.

# Input data

The first line of the input file `zigzag.in` contains two natural numbers $c$ and $n$, separated by a space, where $c$ represents the encoding key, and $n$ the number of characters in the message, and the next line contains a string of $n$ characters representing the encoded message.

# Output data

The output file `zigzag.out` will contain a single line, which contains the decoded message.

# Constraints and clarifications

* $1 \\lt c \\lt 5 \\ 000$
* $1 \\lt n \\lt 50 \\ 000$
* In the message, there are only characters with ASCII codes less than $127$ and greater than $31$.

# Example

`zigzag.in`
```
6 24
ODTL EAIIA MCMDIRAPANOIF
```

`zigzag.out`
```
OLIMPIADA DE INFORMATICA
```
