# Task

Given a matrix, you can choose any two adjacent cells as many times as you want in one of the $4$ directions and subtract an integer of your choice from them. Can you obtain a matrix filled with $0$ values?

# Input data

The first line contains two numbers, $N$ and $M$, specifying the matrix dimensions. The following lines contain the matrix.

# Output data

The first line will contain a single message with the text $"DA"$ (meaning "YES") or $"NU"$ (meaning "NO"), indicating whether or not a matrix full of $0$ values can be achieved.

# Constraints and clarifications

* $1 \leq N, M \leq 1000$
* $-10^9 \leq A_{i,j} \leq 10^9$
* After performing an operation, it is allowed for negative elements to exist in the matrix even if they didn't exist initially.
* Messages such as "Da", "nU", "da" ... are considered **incorrect**.

# Example 1

`stdin`
```
2 3
0 1 2
-1 -1 1
```

`stdout`
```
DA
```

## Explanation

You can choose the cells $(2,1), (2,2)$ and subtract $-1$ from them. Next, you can choose the elements $(1,2), (1,3)$ and subtract $1$ from them. Finally, if you choose the elements $(1,3), (2,3)$, and subtract $1$, you obtain a matrix filled with $0$s.

# Example 2

`stdin`
```
2 2
0 1
0 -1
```

`stdout`
```
NU
```

## Explanation

There is no sequence of moves.