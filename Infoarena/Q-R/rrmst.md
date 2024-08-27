# Rrmst

Let $P$ be a permutation of length $N$, chosen randomly with uniform probability from the set of all permutations of length $N$. We will plot in the plane all points of the form $(i, P[i])$. The distance between two points $(x_1, y_1)$ and $(x_2, y_2)$ is given by the value $|x_1 - x_2| + |y_1 - y_2|$. The task is to calculate the cost of the minimum spanning tree of the given set of points.

## Input data

The input file `rrmst.in` will contain on its first line the number $N$. The next $N$ lines will each contain a pair of numbers $x$ $y$, representing the coordinates of a point in the set. It is guaranteed that the set of points is obtained through the method described in the task.

## Output data

The output file `rrmst.out` will contain a single value, the cost of the minimum spanning tree of the given set of points.

## Constraints and clarifications

Tests $1 \dots 3$ have $N = 1\,000$ 

Tests $4 \dots 10$ have $N = 100\,000$

## Example

`rrmst.in`

```
5
2 2
1 4
3 3
5 5
4 1
```

`rrmst.out`

```
12
```