
Given four natural numbers $a, b, k1, k2$. Determine the number of subsets formed from two natural elements $x$ and $y$, where $x$ and $y$ are between $a$ and $b$, such that the greatest common divisor of $x$ and $y$ is a multiple of $k1$ or a multiple of $k2$.

# Input data

The input file contains four numbers, each on its own line, in order: $a, b, k1, k2$ with the above meaning.

# Output data

The output file will contain on the first line the required value.

# Constraints and clarifications

* $a$ and $b$ are between $1$ and $10^{9}$ inclusive, $a \leq b$.
* $k1$ and $k2$ are between $2$ and $10^{9}$ inclusive.
* Pairs for which we have $x = y$ are not counted.

# Example

`abk1k2.in`
```
4
10
2
4
```

`abk1k2.out`
```
6
```

## Explanation

The subsets that are counted are: `{4}, {6, 4}, {8, 4}, {10, 6}, {8, 6}, {10, 8}, {10}`.
