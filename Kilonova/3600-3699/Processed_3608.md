A sequence $x_1, x_2, \dots x_k$ is called **small** if for each $i$ from $1$ to $k$, we have $x_i \leq i$.

# Task

You are given $N$ and a **small** sequence $a_1, a_2, \dots a_N$ of non-zero natural numbers. Each element from $1$ to $N$ needs to be associated with a number, $1$ or $2$, such that the sum of the values at the positions with $1$ is equal to the sum of the values at the positions with $2$. If it's not possible, output $-1$.

More specifically, partition the sequence into two subsets of equal sum.

# Input Data

The first line of the input file `partitie.in` contains the natural number $N$. The second line contains the sequence $a_1, a_2, \dots a_N$.

# Output Data

The first line of the output file `partitie.out` will contain $-1$ if there is no partition. If there is, it will display a sequence of length $N$. The $i$-th character is $1$ if element $i$ is part of the first subset or $2$ if it is part of the second.

# Constraints and Clarifications

* $1 \leq N \leq 100 \ 000$
* **$1 \leq a_i \leq i$** for each $i$ from $1$ to $N$.
* For test cases worth $31$ points, $N \leq 4$

# Example 1

`partitie.in`
```
6
1 1 2 4 3 5
```

`partitie.out`
```
211221
```

## Explanation

The sum of values at positions with $1$ is $1 + 2 + 5 = 8$, and the sum of values at positions with $2$ is $1 + 4 + 3 = 8$. We observe that these sums are equal.

# Example 2

`partitie.in`
```
4
1 2 3 3
```

`partitie.out`
```
-1
```

## Explanation

It is observed that there is no partition into two subsets of equal sum.