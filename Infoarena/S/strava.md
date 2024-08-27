# Strava

You are given $N$ segments in the plane. We assign a direction to each segment determined by the points $(X1, Y1)$ respectively $(X2, Y2)$ from $(X1, Y1)$ towards $(X2, Y2)$. We say that two segments determined by the points $(S1X1, S1Y1, S1X2, S1Y2)$, respectively $(S2X1, S2Y1, S2X2, S2Y2)$ overlap if and only if the following two conditions are simultaneously satisfied:
$D(S1X1, S1Y1)(S2X1, S2Y1) \leq 1$
$D(S1X2, S1Y2)(S2X2, S2Y2) \leq 1$
where by $D(P1)(P2)$ we refer to the Euclidean distance between points $P1$ respectively $P2$. Determine how many overlaps of two segments are determined by the $N$ segments.

## Input data

The input file `strava.in` contains on the first line a natural number $T$ representing the number of tests.
For each test, the next line contains the value of $N$ representing the number of segments followed by $N$ lines containing 4 numbers $(X1, Y1, X2, Y2)$ representing the coordinates of the segment endpoints.

## Output data

In the output file `strava.out`, print for each test the number of determined overlaps.

## Constraints and clarifications

$T = 5$ 

$N = 100 \ 000$ 

All coordinates are given with exactly 4 decimal places

The coordinate values are all within the interval $[0, 10 \ 000]$ 

It is guaranteed that the result does not exceed $500 \ 000$ 

## Example

`strava.in` 
```
1
3
1.0000 1.0000 5.0000 5.0000
1.1000 0.9000 4.9000 5.1000
5.0000 5.0000 1.0000 1.0000
```

`strava.out`
```
1
```