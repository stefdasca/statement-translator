
A sequence of $N$ distinct numbers $a_1, a_2, \dots, a_N$ is given. Any sequence $a_i, a_{i+1}, \dots, a_{j-1}, a_j$, $1 \leq i + 1 < j \leq n$, for which all the values $a_k$, $i < k < j$, are smaller than the extremities $a_i$ and $a_j$, will henceforth be called a "pit."

# Task

Write a program that will determine the number of "pits" in the given sequence.

# Input data

The input file `nrpits.in` contains on the first line the natural number $N$. The second line contains the $N$ natural numbers of the sequence, separated by space.

# Output data

The output file `nrpits.out` will contain a single number representing the number of "pits" in the given sequence.

# Constraints and clarifications

* $2 \leq N \leq 1 \ 000 \ 000$
* $1 \leq a_i \leq 1 \ 000 \ 000$, for each $1 \leq i \leq N$
* any "pit" has at least three elements

# Example 1

`nrpits.in`
```
12
12 1 10 3 4 11 5 8 7 9 2 6
```

`nrpits.out`
```
8
```

## Explanation

The eight "pits" are: $(12, 1, 10)$, $(10, 3, 4)$, $(12, 1, 10, 3, 4, 11)$, $(10, 3, 4, 11)$, $(11, 5, 8)$, $(8, 7, 9)$, $(9, 2, 6)$, $(11, 5, 8, 7, 9)$.
