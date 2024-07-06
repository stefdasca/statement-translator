\textbf{On a mathematics notebook sheet of size $N \times M$ ($N$ number of rows and $M$ number of columns), all cells are filled with `X` or `0`. For a given natural number $K$, we call a correct sequence, a sequence of $K$ consecutive elements in a row, column, or diagonal that have the same value (`X` or `0`). Two cells on the sheet are neighbors on the same diagonal if they share a single common column element.**

Example in the adjacent figure, for which $N = 4$, $M = 5$, $K = 3$ includes $6$ correct sequences of `X` and $5` correct sequences of `0`.

~[image.png|align=left]

# Task

1. Given natural numbers $N$, $M$ and $K` and a mathematics sheet filled with `X` and `0`, determine how many correct sequences of `X` and how many correct sequences of `0` are present on the given sheet.
2. Given $Q` questions of the form $A, B$, where $A` is the character `X` or `0` and $B` is a natural number, determine how many ways we can cut the mathematics sheet vertically to obtain in the subtable from the left exactly $B` correct sequences of $A`. The sheet can be cut in $M - 1` ways: after the first column, second column, third column, and so on, until after the penultimate column.
# Input data

The input file `jocxzero.in` contains on the first line a natural number $P` representing the task from the problem that needs to be solved.

If $P = 1$ then the second line contains in order the natural numbers $N, M` and $K`, separated by a space, then on the next $N` lines with $M characters of `X` or `0` represent the given sheet.
If $P = 2$ then the second line contains in order the natural numbers $N, M_ and $K`, separated by a space, then on the next $N` lines with $M characters of `X` or `0` representing the given sheet.
On the line $N + 3` contains the natural number $Q`. On the next $Q_ lines contains one character $A` and a natural number $B` separated by a space.

# Output data

If $P = 1$ then the output file `jocxzero.out_ contains on a single line two natural numbers separated by a space, representing, in order, the number of correct sequences of `X` and the number of correct sequences of `0`.

If $P = 2` then the output file jocxzero.out contains $Q` lines, each containing a natural number representing the answer to the corresponding question from the input file.

# Constraints and clarifications

* $1 \leq N \leq 100
* $2 \leq M \leq 10\ 000
* $1 \leq K \leq 100
* $1 \leq Q \leq 100\ 000
* $0 \leq B \leq 1\ 000\ 000\ 000
* In the input files, the character `X` is uppercase and `0` is the digit zero.
* Correctly solving the first task (1) awards 40 points, while correctly solving the second task (2) awards 60 points.

# Example 1

`jocxzero.in`
```
1
4 5 3
XXXX0
0XXX0
00X00
000XX
```

`jocxzero.out`
```
6 5
```

## Explanation

On the first row, there are $2` correct sequences of `X`, on the second there is one correct sequence of `X`, on the diagonal there are $2` correct sequences of `X` and one on the vertical.

On the last row, there is one correct sequence of `0`, on the first column there is one correct sequence of `0`, on the last column there is one correct sequence of `0`, on the diagonal there are $2` more correct sequences of `0`.

# Example 2

`jocxzero.in`
```
2
4 5 3
XXXX0
0XXX0
00X00
000X0
2
0 1
X 1
```

`jocxzero.out`
```
2
0
```

## Explanation

We can cut vertically after the first column, after the second, after the third, and after the fourth column. If we cut after the first and second, we get a single correct sequence of `0`.

Regardless of where we cut, we cannot have a subtable with a single correct sequence of `X`.