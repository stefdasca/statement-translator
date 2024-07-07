
It is considered two arrays of natural numbers, both of length $n$, $a$ = ($a_1$, $a_2$, $\\dots$, $a_n$) and $b$ = ($b_1$, $b_2$, $\\dots$, $b_n$). It is known that the elements in the two arrays are natural numbers, not necessarily distinct, from the set {$1$, $2$, $\\dots$, $n$}. With the two arrays, the following operation can be performed: two indices $i$ and $j$ are chosen, with $1 \\leq i \\leq j \\leq n$, then by swapping the subarrays $a_i$, $a_{i+1}$, $\\dots$, $a_j$ with $b_i$, $b_{i+1}$, $\\dots$, $b_j$, the arrays obtained are: $a_1$, $a_2$, $\\dots$, $a_{i-1}$, $b_i$ ,$b_{i+1}$, $\\dots$, $b_j$, $a_{j+1}$, $a_{j+2}$, $\\dots$, $a_n$ and $b_1$, $b_2$, $\\dots$, $b_{i-1}$, $a_i$ ,$a_{i+1}$, $\\dots$, $a_j$, $b_{j+1}$, $b_{j+2}$, $\\dots$, $b_n$.

If at least one of the obtained arrays is a permutation of the set {$1$, $2$, $\\dots$, $n$}, then we say that a _mixperm_ is obtained.

# Task

Determine in how many ways a _mixperm_ can be obtained.

# Input data

The file `mixperm.in` contains on the first line the natural number $n$, on the second line, separated by a space, the numbers $a_1$, $a_2$, $\\dots$, $a_n$, and on the third line, separated by a space, the numbers $b_1$, $b_2$, $\\dots$, $b_n$.

# Output data

The file `mixperm.out` contains a single natural number representing the number of possible ways to obtain a _mixperm_.

# Constraints and clarifications

* $1 \\leq n \\leq 10 \\ 000$;

# Example 1

`mixperm.in`
```
6
3 2 1 4 4 5
2 3 3 4 6 5
```

`mixperm.out`
```
8
```

## Explanation

The subarrays that can be swapped starting and ending at positions $(1, 3)$, $(1, 4)$, $(3, 3)$, $(3, 4)$, $(4, 6)$, $(5, 6)$, $(4, 5)$, $(5, 5)$.

# Example 2

`mixperm.in`
```
2
1 2
1 2
```

`mixperm.out`
```
3
```

## Explanation

The subarrays that can be swapped starting and ending at positions $(1, 1)$, $(2, 2)$ and $(1, 2)$.
