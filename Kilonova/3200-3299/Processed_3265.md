
# Task

We have a sequence of natural numbers arranged in positions from $1$ to $n$. The task is to determine a position $p$ ($1 \leq p < n$) with the property that the sum of the elements in the sequence from positions $1$ to $p$ (inclusive) multiplied by the sum of the elements in the sequence from positions $p+1$ to $n$ (inclusive) is maximized. If there are multiple choices for the position $p$, the solution with minimum $p$ is required.

# Input data

The file `splitmax.in` contains the value $n$ on the first line, and on the second line, the elements of the given sequence, separated by space.

# Output data

The file `splitmax.out` contains an integer representing the value of $p$ determined according to the task.

# Constraints and clarifications

* $2 \leq n \leq 100 \ 000$;
* The values in the sequence are non-zero natural numbers with at most $9$ digits.

# Example

`splitmax.in`
```
3
6 3 4
```

`splitmax.out`
```
1
```

## Explanation

The maximum product that can be obtained is $6 \cdot (3+4)$.
