## Task

Ghita the Shepherd owns an orchard with $M$ trees near his sheepfold. The orchard is enclosed by a fence made up of $N$ stakes connected with barbed wire, thus isolating all $M$ trees inside a polygon. Advised by a friend on Facebook, Ghita built the fence so that the polygon formed is convex, and the trees are strictly inside this polygon. Two other shepherds from neighboring sheepfolds plotted against Ghita and, one night when he was on the phone, they destroyed the orchard's fence, stealing the stakes and the wire. Ghita needs to rebuild the fence as quickly as possible, but he only found $P$ stakes and does not have time to dig new holes for them, so he will reuse the old ones. Because $P \leq N$, he has to select only $P$ from the initial $N$ coordinates of the stakes and construct the fence using them, positioning the new stakes at these coordinates. His aim is to choose the positions of the stakes such that the number of trees strictly inside the new polygon is maximized. It is possible that one of the trees is now on the boundary of the polygon, but it should not be taken into account because it is not truly enclosed.

## Input data

The input file `pomi.in` contains on the first line the number of tests $T$. Following this, the description of each test is as follows:
The first line contains the integers $N, M, P$.
The next $N$ lines contain pairs of coordinates $(x, y)$ representing the coordinates of the vertices of the initial polygon, specified in a clockwise order.
The next $M$ lines contain the coordinates of the trees that are inside the initial polygon, and they are also integers.

## Output data

In the output file `pomi.out`: for each test, print the maximum number of trees that can be enclosed according to the constraints, on separate lines.

## Constraints and clarifications

$3 \leq N, M \leq 100$

$3 \leq P \leq N$

The coordinates are natural numbers $\leq 100000$

The input file will contain a maximum of 5 tests.

## Example

`pomi.in`
```
1
6 17 3
6 13
13 10
13 4
8 2
3 4
1 9
2 8
2 9
3 6
3 9
5 5
5 11
6 4
7 9
7 11
8 6
9 4
9 8
10 9
11 5
11 10
12 7
12 9
8
```

`pomi.out`
```
8
```

## Explanation

The triangle with vertices at coordinates $(6, 13)$ $(13, 10)$ $(8, 2)$ contains 8 trees inside: $(7, 9)$ $(7, 11)$ $(8, 6)$ $(9, 4)$ $(9, 8)$ $(10, 9)$ $(11, 10)$ $(12, 9)$, and 8 is the maximum number of trees that can be enclosed by a triangle with vertices at the initial points.