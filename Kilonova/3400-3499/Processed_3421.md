George is a great lover of computer science, but he is still at the beginning and that's why he needs your help.

In computer science class, the teacher writes $N$ natural numbers on the board, and at each step, George has to pick two numbers from consecutive positions and replace them with a single number equal to the integer part of their arithmetic mean. For example, $7$ and $9$ are replaced with $8$, $7$ and $12$ with $9$, and $101$ and $102$ with $101$. George must do these replacements until only one number is left on the board.

# Task

Help George find out what is the largest number that can be obtained at the end.

# Input data

The first line will contain a natural number $N$, and the second line will contain $N$ numbers $a_1, a_2, \dots, a_N$, the $N$ numbers originally written on the board.

# Output data

Print a single number, the largest number that can be obtained at the end, after all operations have been performed.

# Constraints and clarifications

* $1 \leq N \leq 200$
* $1 \leq a_i \leq 1 \ 000 \ 000 \ 000$, for $i$ from $1$ to $N$

| # | Score | Constraints |
| --- | ---- | ------------ |
| 1 | 30 | $N < 10$ |
| 2 | 70 | No additional constraints |

# Example

`stdin`
```
4
2 4 5 7
```

`stdout`
```
5
```

## Explanation

Initial sequence: $2 \ 4 \ 5 \ 7$

Replace elements at positions $2$ and $3$: $2 \ 4 \ 7$

Replace elements at positions $1$ and $2$: $3 \ 7$

Replace elements at positions $1$ and $2$: $5$