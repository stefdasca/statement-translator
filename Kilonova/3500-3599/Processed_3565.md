
# Task

We are given a matrix with $0$s and $1$s. We consider that $0$ is in the free cells and $1$ is in the occupied cells. We want to fill with $1$ as many consecutive rows as possible from the bottom of the matrix (meaning we want to completely fill row $n$, row $n-1$, $\dots$). We have the operation: select a cell equal to $1$ and then we can drag it to the left, right, or downwards until we fix it where we want. We can drag it from the current position to an adjacent one only if that position is free. Basically, we can move it to another place further down (or on the same row) by passing through free zones. Moving to the left or right costs nothing, but moving downwards has a cost equal to the number of rows descended.

Determine:
1. The maximum number of lines that can be completely filled at the bottom. Note that we are only interested in the number of lines full of $1$s, the partially completed ones are ignored.
2. The minimum cost to fill this maximum number of lines.

# Input data

The first line of the input file `drag.in` contains a number $C$ representing the task to solve and a number $n$ representing the size of the matrix (which is a square). 
Each of the next $n$ lines contains $n$ values $0$ or $1$ representing the configuration of the given matrix. The lines are numbered from top to bottom starting with 1, and the columns are numbered from left to right, also starting with 1. The numbers on the same line are separated by spaces.

# Output data

In the file `drag.out`, it will contain:
* A value representing the maximum number of rows that can be completely filled at the bottom if we have $C = 1$.
* Two values, separated by a space, representing respectively: the maximum number of lines that can be completely filled at the bottom and the minimal cost to fill this number of lines if we have $C = 2$.

# Constraints and clarifications

* $1 \leq n \leq 1\ 000$;
* $1 \leq C \leq 2$;
* For $26$ points $C=1$;
* For $74$ points $C=2$;
* Note that if we have $C = 1$, in the output file we write only one number;

# Example 1

`drag.in`
```
1 4
1 1 0 1
1 0 0 0
1 0 1 1
1 1 0 1
```

`drag.out`
```
2
```

# Example 2

`drag.in`
```
2 4
1 1 0 1
1 0 0 0
1 0 1 1
1 1 0 1
```

`drag.out`
```
2 4
```

## Explanation
* The $1$ on the second row can be dragged one position to the right and then one downward (filling with 1 the element on row $3$ and column $2$). The cost so far is $1$.
* The $1$ on row $3$ and column $3$ moves one position downward. Thus, the last line is completed. The total cost so far is $2$.
* The $1$ on row $1$ and column $4$ moves one position to the left and then two downward, occupying the place left free by the previous move, thus completing the second line from the bottom. The final cost becomes $4$.
