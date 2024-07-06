Zebughil decided to expand his chicken business to a more exotic place like Hawaii. The territory occupied by the Hawaiian islands can be seen as a Cartesian plane, where Zebughil pounded $N$ stakes at integer coordinate points. Also, Zebu discovered in Hawaii the famous golden hen that lays magic eggs.

He wants to encircle $3$ of the stakes with string so that the golden hen is inside the formed triangle, but first, he wants to know in how many ways he can do this.

# Task

Given the coordinates of the golden hen and the $N$ stakes, find out in how many ways Zebughil can choose $3$ stakes so that the formed triangle contains the golden hen inside.

# Input data

The first line of the input file `hawaii.in` contains $3$ integers $N$, $X_c$, and $Y_c$, representing the number of stakes pounded by Zebughil and the coordinates where the golden hen is located. The next $N$ lines each contain two numbers $X_i$ and $Y_i$ representing the coordinates of the stakes.

# Output data

The first line of the output file `hawaii.out` will contain a single number representing in how many ways Zebughil can choose $3$ stakes to meet the condition described in the task.

# Constraints and clarifications

* $3 \leq N \leq 50\ 000$
* For $40\%$ of the tests, $N \leq 1\ 000$
* For $60\%$ of the tests, $N \leq 4\ 000$
* Any $3$ points in the input file are not collinear.
* The coordinates of the points will be in the range $[-100\ 000\ 000, 100\ 000\ 000]$

# Example

`hawaii.in`
```
5 5 4
1 2
3 1
5 6
6 1
8 6
```

`hawaii.out`
```
5
```

## Explanation

Zebughil can encircle the following $5$ triplets of stakes: $(1, 2, 5), (1, 3, 4), (1, 4, 5), (2, 3, 4), (2, 3, 5)$.