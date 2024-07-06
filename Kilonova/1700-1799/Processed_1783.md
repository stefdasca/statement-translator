Miruna and Laura are playing with their best friend, Caterpillar. Miruna has a string of $N$ natural numbers and wants to find a subarray $S$ of maximum length that meets the following property:

It contains at least once each number between $1$ and $Max_S$, where $Max_S$ represents the maximum value in the subarray $S$.

# Task

Help Laura and Caterpillar respond to Miruna.

# Input data

The input file `unique.in` will contain:

- The first line contains a single natural number $T$, representing the number of tests in the file.
- On line $2 \cdot i$, $(i = 1, 2, \dots, T)$, a natural number representing the number of elements in an array.
- On line $2 \cdot i + 1$, $(i = 1, 2, \dots, T)$, the elements of the array whose length is given on the previous line.

# Output data

The output file `unique.out` will contain $T$ lines; on line $i$, the maximum length of a subarray in the array that meets the imposed requirement, given by lines $2 \cdot i$ and $2 \cdot i + 1$ in the input file $(i = 1, 2, \dots, T)$ will be written.

# Constraints and clarifications

- $1 \leq T \leq 10$
- $1 \leq N \leq 100 \ 000$
- The elements of the arrays will be between $1$ and $N$.

# Example

`unique.in`
```
1
16
3 1 4 5 2 7 5 2 8 3 1 3 1 2 3 9
```

`unique.out`
```
6
```

## Explanation

The longest subarray that meets the imposed condition starts at position $10$ and ends at position $15$.