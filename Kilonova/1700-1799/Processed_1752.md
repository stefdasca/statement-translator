
Arrange the first $N$ positive natural numbers in the form of an array $A_1, A_2, \dots, A_N$.

Let $X_1, X_2, \dots, X_K$, ($K \geq 3$), be a subsequence of the array $A$. We call a term of the subsequence $X$ an *local extremum* if it is the middle of a subarray of length $3$ in the subsequence, $X_{i-1}, X_i, X_{i+1}$, with the property:
$X_{i-1} < X_i > X_{i+1}$, $1 < i < K$
or
$X_{i-1} > X_i < X_{i+1}$, $1 < i < K$.

We denote by $\text{nrex}(X)$ the number of local extrema in the subsequence $X$. We say that a subsequence $X_1, X_2, \dots, X_K$, ($K \geq 2$) of the array $A$ is an *alternating subsequence* if $\text{nrex}(X) = K-2$, meaning excepting the first and the last term in the subsequence, all other terms are *local extrema* of the subsequence $X$.

Among all the *alternating subsequences* of the array $A$, we are interested in those of maximum length, which we shall call *maximal alternating subsequences*.

# Task

Given $N$ and the array $A$, determine the remainder obtained by dividing the number $M$ of *maximal alternating subsequences* of the array $A$ by the number $1 \ 000 \ 003$.

# Input data

The input file `sam.in` contains on the first line the natural number $N$. The second line contains the $N$ numbers of the given array separated by a space.

# Output data

The output file `sam.out` will contain the remainder obtained by dividing the number $M$, having the significance described above, by the number $1 \ 000 \ 003$.

# Constraints and clarifications

* $3 \leq N \leq 100 \ 000$;

# Example

`sam.in`
```
7
1 3 5 4 7 6 2
```

`sam.out`
```
6
```

## Explanation

The given array contains three *local extrema*, the values $5$, $4$ and $7$. The six *maximal alternating subsequences* with the given array are: $(1, 5, 4, 6, 2)$, $(1, 5, 4, 7, 2)$, $(1, 5, 4, 7, 6)$, $(3, 5, 4, 6, 2)$, $(3, 5, 4, 7, 2)$, $(3, 5, 4, 7, 6)$.
