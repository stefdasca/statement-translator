
We consider the non-zero natural numbers $X$, $N$, $K$, where $N$ is a power of $2$. For a permutation $p = (p_1, p_2, \dots, p_N)$ of the set $\{1, 2, \dots, N\}$, determine the maximum following the example below:

~[xnk.png]

# Task

Determine the number of permutations of the set $\{1, 2, \dots, N\}$ where the value $X$ is present at level $K$ but not at level $K - 1$. Since this number can be very large, determine it modulo $1 \ 234 \ 577$.

# Input data

The input file `xnk.in` contains three natural numbers $X$, $N$ and $K$ separated by space on the first line.

# Output data

In this case, the output file `xnk.out` will contain a single natural number on the first line representing the number of permutations that meet the required conditions, modulo $1 \ 234 \ 577$.

# Constraints and clarifications

* $N \in \{2^2, 2^3, \dots, 2^{20}\}$
* $1 \leq X \leq N$
* $1 \leq K \leq 1 + \log_{2} N$
* $1 \ 234 \ 577$ is a prime number

# Example 1

`xnk.in`
```
1 8 3
```

`xnk.out`
```
0
```

## Explanation

The value $1$ cannot appear at level $3$, only at level $4$.

# Example 2

`xnk.in`
```
2 4 2
```

`xnk.out`
```
8
```

## Explanation

The $8$ permutations are: $(1 \ 2 \ 3 \ 4)$, $(1 \ 2 \ 4 \ 3)$, $(2 \ 1 \ 3 \ 4)$, $(2 \ 1 \ 4 \ 3)$, $(3 \ 4 \ 1 \ 2)$, $(3 \ 4 \ 2 \ 1)$, $(4 \ 3 \ 1 \ 2)$, $(4 \ 3 \ 2 \ 1)$
