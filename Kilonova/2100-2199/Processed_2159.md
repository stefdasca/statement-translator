
# Task

Given $N$ and $K$, display the $K$-th permutation of order $N$ in lexicographic order.

# Input data

A single line contains $N$ and $K$.

# Output data

A sequence of $N$ numbers.

# Constraints and clarifications

* $1 \\leq N \\leq 18$
* $1 \\leq K \\leq N!$
* For $40$ points, $1 \\leq N \\leq 10$

# Example 1

`stdin`
```
4 6
```

`stdout`
```
1 4 3 2
```

## Explanation

The first $6$ permutations are:
$(1, 2, 3, 4)$
$(1, 2, 4, 3)$
$(1, 3, 2, 4)$
$(1, 3, 4, 2)$
$(1, 4, 2, 3)$
$(1, 4, 3, 2)$

# Example 2

`stdin`
```
9 74812
```

`stdout`
```
2 8 7 9 4 1 5 6 3
```
