Here is the translated and processed text:

---

We define a number puzzle as the addition of two natural numbers, where some of the digits have been replaced with the character `*`. For example, for the addition:

$$
\begin{alignedat}{5}
&9&3&3&4&\\
&&7&8&9&\\
1&0&1&2&3&\\
\end{alignedat}
$$

some corresponding puzzles can be:
$$
\begin{alignedat}{5}
&*&3&*&4&\\
&&7&8&*&\\
1&0&1&2&3&\\
\end{alignedat}
\; \; \;
\begin{alignedat}{5}
&9&*&*&4&\\
&&*&*&9&\\
*&*&*&*&*&\\
\end{alignedat}
\; \; \;
\begin{alignedat}{5}
&*&*&*&*&\\
&&*&*&*&\\
*&*&*&*&*&\\
\end{alignedat}
$$

# Task

Write a program that determines an addition from which a given puzzle originates.

# Input data

The input file `puzzle.in` will contain multiple tests. The first line contains a natural number $T$ representing the number of puzzles in the file. The following $3 \times T$ lines contain $T$ triplets, each triplet representing a puzzle made up of `*` characters and possibly digits.

# Output data

The output file `puzzle.out` will contain exactly $3 \times T$ lines with natural numbers, three lines for each puzzle in the input file. The first and the second lines of a puzzle will contain the numbers to be added, and the third line will contain their sum, in the order read from the input file.

# Constraints and clarifications

* $1 \leq T \leq 10$;
* All numbers in each puzzle cannot have the first digit $0$;
* If there are multiple correct additions corresponding to a puzzle, any of them will be accepted.
* The length of any line of a puzzle does not exceed $100\ 000$ characters;
* A solution exists for all input tests;
* For tests worth $15$ points, the length of any number in each puzzle will be less than or equal to $18$;
* For tests worth an additional $25$ points, the length of any number in each puzzle will be less than or equal to $1\ 000$;
* For tests worth an additional $25$ points, the length of any number in each puzzle will be less than or equal to $20\ 000$;

# Example 1

`puzzle.in`
```
1
*3*4
78*
10123
```

`puzzle.out`
```
9334
789
10123
```

## Explanation

The input file contains a puzzle:
$$
\begin{alignedat}{5}
&*&3&*&4&\\
&&7&8&*&\\
1&0&1&2&3&\\
\end{alignedat}
$$

A correct addition corresponding to this puzzle is:
$$
\begin{alignedat}{5}
&9&3&3&4&\\
&&7&8&9&\\
1&0&1&2&3&\\
\end{alignedat}
$$

# Example 2

`puzzle.in`
```
2
**
*
**7
75
*
*6
```

`puzzle.out`
```
98
9
107
75
1
76
```

## Explanation

The input file contains two puzzles.
For the first puzzle a correct addition is:
$$
\begin{alignedat}{3}
&9&8&\\
&&9\\
1&0&7&\\
\end{alignedat}
$$
For the second puzzle a correct addition is:
$$
\begin{alignedat}{3}
7&5&\\
&1&\\
7&6&\\
\end{alignedat}
$$

---