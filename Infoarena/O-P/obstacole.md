## Task

You are given $N$ segments in the plane, non-horizontal and non-vertical, which do not intersect at any point. These segments act as obstacles. There are $M$ hot air balloons that travel upwards (the $x$ coordinate remains the same, $y$ increases). If a balloon reaches an obstacle, the balloon will travel along the obstacle in the direction where $y$ increases. When the balloon reaches the end of the obstacle, it will continue to move upwards as before (the $x$ coordinate remains unchanged until the next obstacle is encountered). For each of the $M$ balloons, you need to output the $x$ coordinate it will have after passing all the obstacles it encounters. Note! If a balloon, moving upwards, reaches the end of an obstacle, then the balloon will follow the obstacle. (see the balloon $1 \ 0$ in the example) Note! Balloons can also start on obstacles. In this case, they will move along the obstacle. (see the balloon $13 \ 7$ in the example)

## Input data

The input file `obstacole.in` will contain on the first line $N$ and $M$. On the next $N$ lines, there will be 4 numbers $x1$, $y1$, $x2$, $y2$ representing the coordinates of the endpoints of a segment. On the following $M$ lines, there will be 2 numbers $x$, $y$ representing the starting coordinates of the balloon.

## Output data

The output file `obstacole.out` will contain $M$ numbers, one per line, each representing the $x$ coordinate the corresponding balloon will reach.

## Constraints and clarifications

$1 \leq N, M \leq 10^5$

$0 \leq x, y, x1, y1, x2, y2 \leq 10^9 + 10^4$

For $20 \ \%$ of the score, $N \leq 100$ 
and $M \leq 100$.

For $50 \ \%$ of the score, $N \leq 1000$ 
and $M \leq 1000$.

## Example

`obstacole.in`
```
6 7
1 1 15 4
1 4 7 8
8 7 9 8
2 9 6 11
6 10 8 8
11 9 13 7
1 3
1 0
3 3
4 8
8 5
11 5
13 7
```

`obstacole.out`
```
6
6
9
11
11
6
13
```

## Explanation