Given are $N$ and $K$.

# Task

It is required to determine for the $K$-th permutation in lexicographic order, of the sequence $1, 2, 3, \dots, N$, how many positions $p$ exist such that neither $p$ nor the value at position $p$ contain the digit zero.

# Input data

The input file `nozero.in` contains on the first line the numbers $N$ and $K$, separated by a space.

# Output data

The output file `nozero.out` will contain the sought value.

# Constraints and clarifications

* $1 \leq N, K \leq 1 \ 000 \ 000 \ 000$
* A sequence $p_1, p_2, \dots, p_N$ is lexicographically smaller than another sequence $q_1, q_2, \dots, q_N$, if there exists a position $i$, $1 \leq i \leq N$, such that $p_i < q_i$ and $p_j = q_j$, for any $j$, $1 \leq j < i$.
* For tests worth 16 points, $1 \leq K, N \leq 1\ 000$.
* For other tests worth 33 points, $N \leq 500\ 000$.
* For other tests worth 14 points, $K = 1$.

# Example

`nozero.in`
```
10 2
```

`nozero.out`
```
8
```

## Explanation

The second permutation in lexicographic order, of length $10$, is $1, 2, 3, 4, 5, 6, 7, 8, 10, 9$.
The value $9$ does not contain the digit $0$, but it is at position $10$, which contains the digit $0$.
The value $10$, at position $9$, contains the digit $0$.
All other $8$ values do not contain the digit $0$ and are at positions that do not contain the digit $0$.