# Ring

A ring consists of $N$ circles as shown in the adjacent drawing. Place natural numbers $1 , 2 , \dots , N$ in each circle separately, such that the sum of the numbers in two adjacent circles on the ring is a prime number. Note! To avoid counting the same solution multiple times, we consider that the number $1$ is fixed in one circle on the ring.

## Task

Write a program that calculates the number of ways in which the natural numbers $1 , 2 , \dots , N$ can be placed in the circles so that the given conditions are met.

## Input data

The input file `inel.in` contains a natural number $N$, having the significance from the statement.

## Output data

The output file `inel.out` will contain a single natural number, representing the required number.

## Constraints

$2 \leq N \leq 18$

## Example

`inel.in`
```
8
```

`inel.out`
```
4
```

## Explanation

The $4$ ways to arrange the numbers are:
$1 , 2 , 3 , 8 , 5 , 6 , 7 , 4$
$1 , 2 , 5 , 8 , 3 , 4 , 7 , 6$
$1 , 4 , 7 , 6 , 5 , 8 , 3 , 2$
$1 , 6 , 7 , 4 , 3 , 8 , 5 , 2$