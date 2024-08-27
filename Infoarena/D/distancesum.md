# DistanceSum

Given $N$ points on a plane and $M$ questions of the form: "What is the sum of distances from each of the $N$ points to the given point $(x, y)$?". The distance between two points $(x_1, y_1)$ and $(x_2, y_2)$ is $\max(|x_2 - x_1|, |y_2 - y_1|)$.

## Input data

The input file `distancesum.in` contains on the first line the numbers $N$ and $M$. The next $N$ lines contain the numbers $x_i$ and $y_i$ representing the coordinates of the $N$ points on the plane. The next $M$ lines contain the numbers $x_i$ and $y_i$ representing the coordinates of the points in the questions.

## Output data

In the output file `distancesum.out` you will print $M$ numbers, one per line, representing the answers to the questions.

## Constraints and clarifications

$1 \leq N \leq 100000$

$1 \leq M \leq 100000$

All coordinates are integers between $-10^9$ and $10^9$

## Example

`distancesum.in`

```
4 3
3 5
-3 -2
1 4
-4 -3
2 -4
1 4
4 2
```

`distancesum.out`

```
28
15
21
```