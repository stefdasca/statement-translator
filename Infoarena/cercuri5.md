## Cercuri5

In a plane, a number of circles are drawn, all having radius $R$. Knowing all the pairs of points that determine the intersection of two circles, determine the minimum number of circles drawn. To simplify the problem we will ignore the case where the circles are tangent.

## Input Data

The input file `cercuri5.in` contains on the first line a natural number $T$, the number of tests. The $T$ tests follow:
The first line of each test contains the natural number $R$, the radius of the circles, and $M$, the number of circle intersections.
The next $M$ lines each contain 4 real numbers $x_1$, $y_1$, $x_2$, $y_2$, where $(x_1, y_1)$ are the coordinates of the first intersection point, and $(x_2, y_2)$ are the coordinates of the second intersection point.

## Output Data

In the output file `cercuri5.out` you will print in order for each test a line of the form "Case $<t>: <n>$" (without quotes) where $<t>$ is the test number, and $<n>$ is the minimum number of circles drawn.

## Constraints and clarifications

$1 \leq T \leq 10$ 

$1 \leq R \leq 1000$ 

$1 \leq M \leq 100\ 000$ 

$|x|, |y| \leq 20\ 000$
  
It is recommended to use a precision of $10^{-3}$ for operations with real numbers

## Example

`cercuri5.in`

```
1
5 2
3.0 4.0 3.0 -4.0
9.0 4.0 9.0 -4.0
```

`cercuri5.out`

```
Case 1: 3
```