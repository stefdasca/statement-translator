## Task

Zaharel went out for a walk. He will travel from the coordinate point $(0, 0, 0)$ to the coordinate point $(X, Y, Z)$. It is known that Zaharel moves rather oddly: from a position $(x_1, y_1, z_1)$ he will move only to a position of the form $(x_1 \pm 2^n, y_1 \pm 2^n, z_1 \pm 2^n)$ where $n$ is a natural number. Furthermore, today's walk is special in the sense that Zaharel will only use distinct values for $n$. Given the numbers $X$, $Y$, $Z$, determine a route with the minimum number of positions for Zaharel to reach from $(0, 0, 0)$ to $(X, Y, Z)$.

## Input data

The first line of the input file `plimbare2.in` contains the natural numbers $X$ $Y$ $Z$, separated by spaces.

## Output data

The first line of the output file `plimbare2.out` will contain a single natural number $P_{min}$ representing the minimum number of positions. The next $P_{min}$ lines will contain three integers on a line, representing the positions $(X, Y, Z)$ through which Zaharel passes.

## Constraints and clarifications

$1 \leq X, Y, Z \leq 10^{18}$

It is guaranteed that there is a solution for the given test data.

If there are multiple routes with the minimum number of steps, the one that is lexicographically smallest will be displayed. We say that a route $A=(A_1, A_2, \dots, A_n)$ $(A_i=(A_{i,X}, A_{i,Y}, A_{i,Z}))$ is lexicographically smaller than another route $B=(B_1, B_2, \dots, B_n)$ $(B_i=(B_{i,X}, B_{i,Y}, B_{i,Z}))$ if there is a position $1 \leq i \leq N$ so that $A_1 = B_1$, $A_2 = B_2$, $\dots$, $A_{i-1} = B_{i-1}$ and $A_i < B_i$. A position $A=(A_X, A_Y, A_Z)$ is lexicographically smaller than another position $B=(B_X, B_Y, B_Z)$ if: $A_X < B_X$ or $A_X = B_X$ and $A_Y < B_Y$ or $A_X = B_X$ and $A_Y = B_Y$ and $A_Z < B_Z$.

## Example

`plimbare2.in`
```
16 16 16
```

`plimbare2.out`
```
2
0 0 0
16 16 16
```

`plimbare2.in`
```
123 213 321
```

`plimbare2.out`
```
10
0 0 0
-128 -128 128
-192 -64 64
-194 -62 62
-193 -63 61
-189 -67 57
-181 -59 49
-165 -75 33
-133 -43 65
123 213 321
```