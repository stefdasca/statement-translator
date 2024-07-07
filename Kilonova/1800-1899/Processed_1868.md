
Given a natural number $N$.
We define a **binary string** of length $N$ as the sequence $x_0, x_1, \dots, x_{N-1}$, where

* $x_i = 1$ if $i$ has an odd number of bits equal to $1$ in binary representation
* $x_i = 0$ if $i$ has an even number of bits equal to $1$ in binary representation

For example, for $N = 7$ we obtain the following **binary string** of length $7$: $0110100$

Explanation of obtaining the **binary string**:

|$i$ (in base $10$)|$i$ (in base $2$)|value at position $i$ in **binary string**|
|-|-|-|
|0|0|0|
|1|1|1|
|2|10|1|
|3|11|0|
|4|100|1|
|5|101|0|
|6|110|0|

# Task

Determine the number $M$ of palindromic subarrays of length at least $2$ in a **binary string** of length $N$.

# Input data

The input file `bsir.in` contains on the first line the natural number $N$.

# Output data

The output file `bsir.out` will contain $M$ modulo $30\ 103$ (the remainder of dividing $M$ by $30\ 103$).

# Constraints and clarifications

* $2 \leq N \leq 10^{18}$
* The subarray $x_i, x_{i+1}, \dots, x_{j-1}, x_j$ is called palindromic if $x_i = x_j, x_{i+1} = x_{j-1}, \dots$

# Example 1

`bsir.in`
```
10
```

`bsir.out`
```
8
```

# Example 2

`bsir.in`
```
21
```

`bsir.out`
```
30
```
