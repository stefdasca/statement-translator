One of Zahărel's newest passions is to study various properties of permutations. For example, he is interested in permutations where the longest increasing subsequence and the longest decreasing subsequence have given lengths.

# Task

Write a program that determines a permutation of length $N$ in which the longest increasing subsequence has length $A$ and the longest decreasing subsequence has length $B$.

# Input data

The input file `ab.in` will contain on the first line the numbers $N \\ A \\ B$.

# Output data

The output file `ab.out` will contain on the first line $N$ numbers separated by a space, representing a permutation that satisfies the above conditions.

If there are multiple solutions, the lexicographically smallest one will be displayed.

# Constraints and clarifications

* $1 \leq N, A, B \leq 30\ 000$
* It is guaranteed that there is always a solution for the input data
* A subsequence of the string $X = ( x_1, x_2, \ldots x_N )$ is a string $Y = ( x_{i1}, x_{i2}, \ldots x_{iM})$ with the property $1 \leq i_1 < i_2 < \ldots < i_M \leq N$
* A string $(x_1, x_2, \ldots x_K)$ is lexicographically smaller than another string $(y_1, y_2, \ldots y_K)$ if there is a position $p \leq K$, such that $x_p < y_p$ and $x_1=y_1$, $x_2=y_2 \ldots x_{p-1}=y_{p-1}$
* For a test case, $70\\%$ of the score will be awarded if the presented permutation has the longest increasing subsequence of length $A$ and the longest decreasing subsequence of length $B$, but is not lexicographically smallest.

# Example

`ab.in`
```
4 2 3
```

`ab.out`
```
1 4 3 2
```

# Explanation

The longest increasing subsequence has length $2 \\ (1 \\ 4, \\ 1 \\ 3 $ or $1 \\ 2)$, and the longest decreasing subsequence has length $3 \\ (4 \\ 3 \\ 2)$.

Another possible solution is $2 \\ 4 \\ 3 \\ 1$, but it is not lexicographically smallest.