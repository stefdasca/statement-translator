## Task

Two circles are given. Determine the common area of the two circles.

## Input data

The first line of the input file cercuri3.in contains the integer number $T$, representing the number of tests.
The next $T$ lines contain 6 integers and one real number: $x_1$, $y_1$, $R_1$, $x_2$, $y_2$, $R_2$, $A$. $(x_1, y_1)$ are the coordinates of the center of the first circle and $(x_2, y_2)$ are the coordinates of the center of the second circle. $R_1$ is the radius of the first circle, and $R_2$ is the radius of the second circle. $A$ is a real number, and your program must determine if the common area of the two circles is greater than or equal to $A$.

## Output data

For each test, print in the output file cercuri3.out a line containing the string "DA" if the intersection area of the two circles is greater than the number $A$, otherwise "NU".

## Constraints and clarifications

$1 \leq T \leq 30$

$0 \leq x_1, y_1, x_2, y_2 \leq 1000$

$1 \leq R_1, R_2 \leq 1000$

Let $Ac$ be the common area of the two circles. It is guaranteed that $|Ac - A| \geq 0.1$ (i.e., the real number $A$ from each test is at least $0.1$ greater or smaller than the common area). Thus, potential precision errors will be insignificant.

## Example

cercuri3.in

```
5
5 5 5 6 6 6 76.0
5 5 5 6 6 6 76.5
0 0 10 5 5 10 175.0
0 0 10 5 5 10 176.0
0 0 1 1000 1000 1 -1.0
```

cercuri3.out

```
DA
NU
DA
NU
DA
```