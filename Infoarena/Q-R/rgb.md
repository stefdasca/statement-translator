## Task

Georgel is playing with points on the $OX$ axis. Each point has a color: red, green, or blue. Let $P$ be a point. We consider the 2 closest points to $P$ and denote them as $A$ and $B$ respectively. In case of a tie, the leftmost point is chosen. A point $P$ is called $OK$ if $P$, $A$, and $B$ have different colors. A set of points is called diverse if each point in it is $OK$. Given three integers $r$, $g$, and $b$, help Georgel construct a diverse set of $r+g+b$ different points such that $r$ of them are red, $g$ of them are green, and $b$ of them are blue.

## Input data

The input file `rgb.in` will contain on the first line an integer $T$ representing the number of tests. The following $T$ lines will contain three integers $r$, $g$, and $b$ as described in the statement.

## Output data

The output file `rgb.out` will contain the answers for the $T$ tests. The answer for each test has the following format: if a solution exists, it will contain the constructed set split across three lines. The first among the 3 lines will contain $r$ integers representing the coordinates of the $r$ red points in the set. The second and third lines will follow the same format, containing $g$ green points, respectively $b$ blue points. If there is no solution for that test, a single line containing $-1$ will be printed.

## Constraints and clarifications

$1 \leq T \leq 10$ 

$1 \leq r, g, b \leq 100$ 

The coordinates of the displayed points must be distinct and have an absolute value less than $10^9$. 

If there are multiple solutions, any of them is acceptable.

## Example

`rgb.in`
```
2
1 2 1
1 1 100
```

`rgb.out`
```
5 2 7 4
-1
```

## Explanations

In the first test, the points can be arranged as follows:
G BR G $<-\text{ Colors}$
$2 \, 45 \, 7 \, \text{<-- Coordinates }(x)$ 

It is impossible to construct a diverse set with one red point, one green point, and 100 blue points.