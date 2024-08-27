## Task

Robert Acrisor has moved to New York, a city known for the Manhattan style layout of its streets. Knowing that his house is located at the coordinates $X_i$, $Y_i$, and that his goal is to reach the Sun Highway, which is a straight line defined by the equation $A \cdot X + B \cdot Y = 1$, and that his only ways to reach the highway are by moving in the 4 directions: $N$, $S$, $E$, and $W$, and that Robert can change the direction of travel at any time, as long as he complies with one of the 4 directions, you need to tell Robert what the minimum distance is from his home to the highway.

## Input data

The input file `distanta.in` contains on the first line a natural number $T$ representing the number of tests. The next $T$ lines each contain a test description, with each line containing 4 integers separated by a space representing $A$, $B$, $X_i$, and $Y_i$.

## Output data

The output file `distanta.out` will contain $T$ lines representing the answer to each of the $T$ tests.

## Constraints

$T = 1000$

$A$, $B$, $X_i$, $Y_i$ are 32-bit signed integers.

$A$ and $B$ are not both $0$ at the same time.

To receive points for this problem, the absolute difference between your solutions and the jury’s solutions must be less than $10^{-6}$, and the jury suggests using 8 decimals in your output.

## Example

`distanta.in`
```
2
1 2 3 4
-1 -2 3 4
```

`distanta.out`
```
5.00000000
6.00000000
```