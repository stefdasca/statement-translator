Given an array of integers $a_0, a_1, \dots, a_{N-1}$. Each value $a_i$ represents the maximum size of a jump that can be made from position $i$. From position $i$, a jump can reach any of the positions $i+1$, $i+2$, $\dots$, $i+a_i$, if $a_i$ is positive, and if $a_i$ is negative, a jump can reach any of the positions $i-1$, $i-2$, $\dots$, $i-a_i$. We need to reach, through jumps, from position $0$ to a position greater than $N - 1$ (outside the array, to the right).

# Task

Write a program that determines the **minimum number** of jumps required to reach from position $0$ to a position greater than $N - 1$.

# Input data

The input file `salturi.in` contains on the first line the natural number $N$. The second line contains the $N$ numbers of the array, separated by spaces.

# Output data

The output file `salturi.out` will contain a single natural number representing the minimum number of jumps required to reach from position $0$ to a position greater than $N - 1$.

# Constraints and clarifications

* $2 \leq N \leq 1 \ 000 \ 000$
* $-1 \ 000 \ 000 \leq a_i \leq 1 \ 000 \ 000$, for each $0 \leq i \leq N - 1$.
* It is always possible to reach a position greater than $N - 1$.
* Competitors writing programs in C/C++ are advised to read the input data using the functions from the C library.

# Example

`salturi.in`

```
5
2 3 -10 1 1
```

`salturi.out`

```
3
```

## Explanation

From position $0$ jump to position $1$, then to position $4$, then outside the array.

~[example.png]