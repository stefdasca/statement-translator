# Sase49

Andrei, a lottery enthusiast, is studying a different variant of the 6 out of 49 game. In this version, 49 natural numbers from the interval $[1, 16]$ are initially displayed. Then, 6 numbers are drawn from these, not necessarily distinct. Andrei wins if he can guess these 6 numbers before the draw. He considers the probability that a set of 6 numbers is drawn to be directly proportional to the greatest common divisor of those 6 numbers. Thus, he looks at an array of 49 numbers and wants to choose 6 of them, not necessarily distinct, such that the greatest common divisor of the chosen numbers is as large as possible. If the solution is not unique, he wants to choose the solution that represents a lexicographically smallest array.

## Input data

The input file `sase49.in` contains the number of tests $T$ on the first line. The next $T$ lines contain 49 numbers from the interval $[1, 16]$ each.

## Output data

In the output file `sase49.out`, for each test, print the greatest common divisor of the chosen numbers on one line and on the next line print the 6 numbers chosen in ascending order.

## Constraints

$T \leq 20$

An array $(x_1, x_2 \dots x_K)$ is lexicographically smaller than another array $(y_1, y_2 \dots y_K)$ if there exists a position $p$ such that $x_p < y_p$ and $x_1 = y_1$, $x_2 = y_2$ $\dots$ $x_{p-1} = y_{p-1}$.

## Example

`sase49.in`
```
1
1 5 1 2 1 2 1 1 2 12 1 4 1 2 2 2 2 2 1 1 3 1 12 2 4 1 1 3 1 1 3 2 2 1 2 5 2 1 1 2 2 3 1 1 1 2 1 1 1 3 3 3 3 3 12 12
```

`sase49.out`
```
1
1 1 1 1 1 1
```