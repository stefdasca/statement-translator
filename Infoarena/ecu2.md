# Ecu2

Given an equation of the form $a*X^2 + b*X + c = 0$. Determine how many real solutions the given equation has.

## Input data

The first line of the input file `ecu2.in` contains an integer $Q$, representing the number of equations that follow. Each of the next $Q$ lines contains 3 integer numbers, separated by spaces, $a$, $b$, and $c$, which define an equation.

## Output data

For each of the $Q$ equations, in the given order in the input file, print in the output file `ecu2.out` a line containing the number of real solutions of the equation. Print "INF" if the equation has an infinite number of real solutions.

## Constraints

$1 \leq Q \leq 100$

$-1000 \leq a, b, c \leq 1000$

## Example

`ecu2.in`
```
3
1 0 0
1 0 -1
0 0 0
```

`ecu2.out`
```
1
2
INF
```