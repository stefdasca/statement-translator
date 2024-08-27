# Arbsat

A natural number $T$ is given, followed by $T$ tests as follows: a natural number $N$, followed by $N$ points with integer coordinates. For each of the $T$ tests, you need to print $1$ if the given points satisfy the following condition: any rectangle with an area greater than $0$ determined by two of the $N$ points contains at least one other point either inside or on the edges. Otherwise, the program will print $0$.

## Input data

The input file `arbsat.in` will contain on the first line $T$, the number of tests. Next, there are $T$ tests as follows: $N$, the number of points, and then $N$ lines representing the coordinates in the plane of the given points.

## Output data

The output file `arbsat.out` will contain $T$ lines, with values $0$ or $1$, the $i$-th of these corresponding to the response for the $i$-th test from the input file.

## Constraints and clarifications

$1 \leq T \leq 6$

$1 \leq N \leq 100\,000$

The coordinates of the points are positive, strictly greater than $0$ and less than $1\,000\,000\,000$.

It is not possible for there to be more than one point at the same coordinate pair.

## Example

`arbsat.in`

```
2
4
1 1
3 5
2 4
8 8
3
10 9
13 9
10 8
```

`arbsat.out`

```
0
1
```