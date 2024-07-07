
# Task

The cheerful city is a row of houses with different heights. We are interested to know for each house which is the nearest house to its left with a strictly smaller height.

# Input data

The first line contains $N$, the number of houses, and the second line contains $N$ numbers, the heights of the houses.

# Output data

Print the indices of the requested houses or 0 if such a house does not exist.

# Constraints and clarifications

* $1 \leq N \leq 2\*10^5$
* $1 \leq \text{Heights} \leq 10^9$

# Example 1

`stdin`
```
8
2 5 1 4 8 3 2 5
```

`stdout`
```
0 1 0 3 4 3 3 7
```

## Explanation

For example, for the $6$-th house, the nearest house to the left with a strictly smaller value is the house at position $3$.

# Example 2

`stdin`
```
3
5 5 5
```

`stdout`
```
0 0 0
```

## Explanation

No house has a strictly smaller house to its left.
