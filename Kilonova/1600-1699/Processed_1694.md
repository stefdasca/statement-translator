A thief who wants to empty a safe needs its code, and for this, he already has a sequence of $K$ natural numbers that certainly represent part of the code, which unfortunately may not necessarily be complete. He receives from two associates a sequence of $M$ and $N$ natural numbers, respectively, which each one claims is the correct and complete code. Because the two codes do not match, the thief, in order to maximize his chances, tries to determine the longest possible code formed from a series of numbers that is common to the two sequences received from the associates and, in addition, contains his code as a subsequence.

# Task

Given a sequence of natural numbers $c_1$, $c_2$, $\\dots$, $c_K$ representing the thief's code, as well as two other sequences of natural numbers $x_1$, $x_2$, $\\dots$, $x_M$ and $y_1$, $y_2$, $\\dots$, $y_N$, representing the codes of the two associates, determine the maximum length of a sequence of numbers that is a common code for the two associates' codes and also contains the thief's code as a subsequence.

# Input data

The file `cod.in` contains on the first line three natural numbers $K$, $M$, and $N$ separated by a space, representing the lengths of the three codes. The second line contains $K$ natural numbers separated by a space, representing the thief's code. The third line contains $M$ natural numbers separated by a space, representing the first associate's code, and the fourth line contains $N$ natural numbers separated by a space, representing the second associate's code.

# Output data

The file `cod.out` contains one natural number on the first line, which represents the maximum length of a code that meets the requirements.

# Constraints and clarifications

* $1 \\leq K \\leq M,N \\leq 255$
* The codes contain natural numbers from the interval $[1, 255]$
* A subsequence is obtained from a sequence by removing zero, one, or more elements, not necessarily located on consecutive positions
* For the input data, there will always be a solution of at least length $K$

# Example

`cod.in`
```
2 8 9
5 2
2 5 6 2 9 5 9 6
5 6 5 9 2 6 2 9 7
```

`cod.out`
```
4
```

## Explanation

The thief's code has length $K = 2$ and is the sequence $5$, $2$. The two codes of the associates are of lengths $M = 8$ and $N = 9$, respectively, and are given by the sequences on lines $3$ and $4$.

$4$ is the maximum length of the common code of the two associates' codes that contains the thief's code as a subsequence. This is $5$, $6$, $2$, $6$. There is a code of length $5$ common to the two associates' codes, namely $5 \\ 6 \\ 5 \\ 9 \\ 6$, but it does not contain the subsequence $5 \\ 2$.