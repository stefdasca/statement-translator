## Task

Ion and Vasile are two Mioritic shepherds. Over time, while they were friends, they placed $N$ stakes in the ground at the edge of the village. If we consider this ground as a plane, then the stakes can be considered lattice points (points with integer coordinates). After they quarreled, the two decided to divide the land. For this, each stake must be assigned to either Ion or Vasile. The stakes thus form 2 polygons, and their interiors (together with the boundary area) will belong either to Ion or to Vasile. Obviously, the two regions belonging to the shepherds must not have even a single point in common, otherwise new conflicts might arise. Moreover, the two regions must have the shape of a convex polygon. Given the $N$ stakes, determine a way to distribute them such that the difference between the areas of the two resulting lands is as minimal as possible while satisfying all the above conditions.

## Input data

The first line of the file `gradina.in` contains $N$, the number of stakes. Each of the following $N$ lines contains a pair of integers $x$ $y$, representing the coordinates of a stake. All coordinates are, in absolute value, less than or equal to $50\,000\,000$.

## Output data

The first line of the file `gradina.out` contains a real number, displayed with exactly one decimal place, the minimum difference between the areas of the two lands. The next line contains a distribution of the stakes that results in the minimum difference. Thus, it will contain $N$ characters. If the $i$-th character is $I$, then the $i$-th stake from the input file is assigned to Ion. If the character is $V$, then the stake will be assigned to Vasile.

## Constraints and clarifications

$6 \leq N \leq 250$

Any 3 points from the $N$ are not collinear.

If there are multiple distributions of the stakes for which the same minimum difference is obtained, the lexicographically smallest one will be displayed.

The two regions will not contain a stake inside them.

## Example

`gradina.in`
```
7
0 0
2 0
1 4
4 5
0 2
2 2
4 3
```

`gradina.out`
```
1.0
IIVVIIV
```