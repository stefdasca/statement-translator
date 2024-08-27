## Task

Qwerty found a set of $N$ points in his old toy box. Chewbacca, learning about this set of points, challenges Qwerty to a game with quadrants. In this game, the first player chooses one of the $N$ points and draws a vertical line passing through that point, while the second player also chooses one of the $N$ points and draws a horizontal line passing through that point. The two lines form four quadrants similar to coordinate axes. The first player receives one point for each point located in the NE or SW quadrant, the second player receives one point for each point located in the NW or SE quadrant. Qwerty makes the first move, and he wants to choose a point such that his minimum possible score is maximized. Help Qwerty find the maximum score he can obtain. 

## Input data

The input file `cadrane.in` contains on the first line a single natural number $N$ representing the number of points from the set found by Qwerty. The following $N$ lines will contain two integers each, representing the coordinates of the points. 

## Output data

The output file `cadrane.out` will contain a single number representing the maximum score Qwerty can obtain. 

## Constraints and clarifications

$1 \leq N \leq 100\ 000$ 

The coordinates of the points can be represented on 32-bit signed integers.

A point on the line that separates two quadrants is considered as part of both quadrants.

If both players draw lines through the same point, the point is considered as part of all four quadrants.

Attention

Relative to the point $(0, 0)$, the point $(-1, -1)$ is located in the SW quadrant, the point $(1, 1)$ in the NE quadrant, the point $(-1, 1)$ in the NW quadrant, and the point $(1, -1)$ in the SE quadrant.

## Example

`cadrane.in` 
```
10
5 -1
2 4
-4 -3
-2 2
1 -5
4 -1
-1 3
-3 4
-3 -5
-4 4
```
`cadrane.out`
```
5
```

## Explanation

By choosing any of the points $(2, 4)$, $(-2, 2)$, $(1, -5)$, $(-1, 3)$, $(-3, 4)$, $(-3, -5)$ Qwerty will obtain at least 5 points.