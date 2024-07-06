Around the museum in the city of Smallville, there is a fence containing $N$ boards of different heights. We can say that board $i$ has a height $H_i$. The museum director asked the employees to paint this fence with a minimum number of colors, such that the following condition is met: for a given known integer $K$, any sequence of $K$ consecutive boards must not contain 2 boards of the same height, painted identically.

# Task

Write a program that finds the minimum number of colors needed to paint the fence.

# Input data

The input file `culori.in` contains:
- The first line contains `N K` - two integers representing the number of boards and the sequence length.
- The next line contains $N$ natural numbers $H_i$ representing the heights of the $N$ boards.

# Output data

The output file `culori.out` will contain an integer $C$ representing the minimum number of colors used.

# Constraints and clarifications

* $1 \leq K \leq 200\ 000$;
* $1 \leq K \leq N \leq 1\ 000\ 000$;
* $1 \leq H_i \leq 1\ 000$;
* For 50% of the points, $1 \leq K \leq N \leq 5\ 000$;
* For 80% of the points, $1 \leq K \leq N \leq 200\ 000$;

# Example

`culori.in`
```
6 4
1 1 2 1 3 2
```

`culori.out`
```
3
```

## Explanation

A possible painting of the boards using the colors `1, 2, 3` is: `1 2 1 3 1 2`.
There are $3$ sequences: `1 1 2 1`, `1 2 1 3`, and `2 1 3 2`, and any sequence respects the condition given in the statement.