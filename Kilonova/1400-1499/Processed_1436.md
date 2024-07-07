
It is considered a sequence of $N$ natural numbers, denoted $x_1, x_2, x_3, ..., x_N$. We define for any pair of indices $i, j, 1 \leq i \leq j \leq N$, the distance between elements $x_i$ and $x_j$ as being equal to $j - i$.

This sequence will be encoded according to the following rules:
* each element in the sequence is replaced with the index of the closest element in the sequence (the one to which the distance is minimal) strictly greater than it;
* if for an element in the sequence there are two elements that respect the above rule, then it will be replaced with the larger index, that is, the index of the element strictly greater than it, located to its right;
* elements of maximum value in the sequence will be replaced with $-1$.

# Task

Write a program that encodes a sequence of $N$ values, according to the described rules.

# Input data

The input file `codat.in` contains:
* the first line contains the natural number $N$
* the next line contains $N$ non-zero natural numbers, separated by a space, representing the sequence $x_1, x_2, x_3, ..., x_N$

# Output data

The output file `codat.out` will contain the first line with $N$ non-zero integers, separated by a space, representing the encoded sequence.

# Constraints and clarifications

* $1 \leq N \leq 1\ 000\ 000$
* $1 \leq x_i \leq 2\ 000\ 000\ 000, 1 \leq i \leq N$

# Example

`codat.in`
```
7
2 9 3 5 1 1 4
```

`codat.out`
```
2 -1 4 2 4 7 4
```

## Explanation

$x_1 = 2$: the closest strictly greater element is $x_2$
$x_2 = 9$: it has no element greater than it
$x_3 = 3$: the strictly greater elements are at an equal distance, so it will be replaced with the larger index, that is $4$
$x_4 = 5$: the closest strictly greater element is $x_2$
$x_5 = 1$: the closest strictly greater element is $x_4$
$x_6 = 1$: the closest strictly greater element is $x_7$
$x_7 = 4$: the closest strictly greater element is $x_4$
