We have \(N\) people labeled with tags \(1, 2, \ldots, N\), in some order, and a ladder with \(N\) rungs. The people are lined up in Indian file, facing the location of the ladder. The rungs of the ladder are initially unoccupied. Repeatedly, the person currently at the right end of the line positions themselves on the ladder on the first unoccupied rung, and each of the people on the lower rungs descends from the ladder and repositions themselves at the right end of the line, starting with the one on the first rung of the ladder. The action stops when all the rungs on the ladder are occupied.

Example: Initially, at stage 0 we have line=$(4,2,1,3)$ and ladder=$(0,0,0,0)$.

Stage \(1\): \((4,2,1)/(3,0,0,0)\) \\
Stage \(2\): \((4,2,3)/(0,1,0,0)\) \\
Stage \(3\): \((4,2)/(3,1,0,0)\) \\
Stage \(4\): \((4,3,1)/(0,0,2,0)\) \\
Stage \(5\): \((4,3)/(1,0,2,0)\) \\
Stage \(6\): \((4,1)/(0,3,2,0)\) \\
Stage \(7\): \((4)/(1,3,2,0)\) \\
Stage \(8\): \((1,3,2)/(0,0,0,4)\) \\
...\ \\
Final: \(()/(3,2,1,4)\)

# Task

Display the labels of the people in the order in which they are positioned on the ladder at the end.

# Input data

In the input file `scara.in`, the first line contains the number \(N\). The second line contains \(N\) natural numbers separated by spaces, representing the labels of the \(N\) people, in the initial order in the line, from left to right.

# Output data

In the output file `scara.out`, the first line will contain the \(N\) natural numbers representing the labels of the people corresponding to their position on the ladder, separated by spaces.

# Constraints and clarifications

* \(1 \leq N \leq 2\ 000\);
* For 22 points \(N \leq 15\).

# Example 1

`scara.in`
```
4
4 2 1 3
```

`scara.out`
```
3 2 1 4 
```

## Explanation

\((4,2,1,3)/(0,0,0,0)\), \\
\((4,2,1)/(3,0,0,0)\), \\
\((4,2,3)/(0,1,0,0)\), \\
\((4,2)/(3,1,0,0)\) \\
\((4,3,1)/(0,0,2,0)\) \\
\((4,3)/(1,0,2,0)\), \\
\((4,1)/(0,3,2,0)\), \\
\((4)/(1,3,2,0)\), \\
\((1,3,2)/(0,0,0,4)\), \\
\((1,3)/(2,0,0,4)\), \\
\((1,2)/(0,3,0,4)\), \\
\((1)/(2,3,0,4)\), \\
\((2,3)/(0,0,1,4)\), \\
\((2)/(3,0,1,4)\), \\
\((3)/(0,2,1,4)\), \\
\(()/(3,2,1,4)\).

# Example 2

`scara.in`
```
3
2 3 1
```

`scara.out`
```
3 1 2
```

## Explanation

\((2,3,1)/(0,0,0)\), \\
\((2,3)/(1,0,0)\), \\
\((2,1)/(0,3,0)\), \\
\((2)/(1,3,0)\), \\
\((1,3)/(0,0,2)\), \\
\((1)/(3,0,2)\), \\
\((3)/(0,1,2)\), \\
\(()/(3,1,2)\).

