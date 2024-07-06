A child wishes to find an original way to encode his name and uses for this purpose a figure made only of triangles, drawn on a sheet of paper. He places each letter of his name in a triangle. If his name is `DARIUS`, the sheet of paper will look like figure \(1\). On the first row, he places the first letter, on the second row the next three letters, on the third row the next five letters, and so on until he places all the letters of the name. If the name does not have enough letters, the child uses the character `*` to complete the last row on which he has placed letters. Dissatisfied that the name can be read relatively easily, he rotates the figure, rotating the sheet of paper clockwise, thus obtaining figure \(2\).

~[litere1.png|width=40em]

# Task

Knowing the letters of the name, write a program that determines and displays in the output file:

1. The number of `*` characters that need to be used to complete the last row;
2. The first letter of each row in the initial figure;
3. The string of letters on each row, after rotating the sheet of paper.

# Input data

The input file `litere.in` contains:
- The first line contains a natural number $P$ representing the task from the problem that needs to be solved.
- The second line contains a natural number $N$, representing the number of letters in the name.
- The third line of the file contains the child's name formed of $N$ uppercase letters from the English alphabet. The letters are separated by a space.

# Output data

If the value of $P$ is $1$, the output file `litere.out` will contain a natural number, representing the number of `*` characters in the figure.
If the value of $P$ is $2$, the output file `litere.out` will contain, on a single line, a string of letters, separated by a space, formed from the first letter of each row of the figure, before rotating it, starting from the first row to the last.
If the value of $P$ is $3$, the output file `litere.out` will contain the letters obtained after rotating the initial figure. Displaying is done from top to bottom, and within a row, from left to right. Each row of letters will be displayed in the file on separate lines, and the letters located on the same row will be separated by a space.

# Constraints and clarifications

* $1 \leq N \leq 10\ 000$;
* For correctly solving task $1$, $10$ points will be awarded, for correctly solving task $2$, $30$ points will be awarded, and for correctly solving task $3$, $60$ points will be awarded.

# Example 1

`litere.in`
```
1
6
D A R I U S
```

`litere.out`
```
3
```

## Explanation

For writing the name Darius, 3 rows will be completed, formed of 9 triangles, of which 3 will contain the character *.

# Example 2

`litere.in`
```
2
6
D A R I U S
```

`litere.out`
```
D A U
```

## Explanation

The first letter of the first row is $D$, the first letter of the 2nd row is $A$, the first letter of the 3rd row is $U$.

# Example 3

`litere.in`
```
3
6
D A R I U S
```

`litere.out`
```
U
S A
I R D
```

## Explanation

After rotation, on the first row is the letter $U$, on the second row the letters $S \ A$, and on the third row, in order from left to right, the letters $I \ R \ D$.