# Cars

## Task

To reach the XXXIII edition of the Grigore Moisil contest, the $N+M$ members of the committee decided to take advantage of the new Cluj-Napoca - Târgu Mureș highway. Each member of the committee drives their own car, represented as a point. The cars are classified into two categories: $N$ of them are fast cars, with a constant speed equal to $A$ m/s. $M$ of them are slow cars, with a constant speed equal to $B$ m/s. Each car starts from a certain integer position, representing the distance from Cluj-Napoca, measured in meters. The highway is $L$ meters long and, unfortunately, offers only a single lane. However, it is partitioned into two types of segments: Segments with dashed lines, where overtaking can be performed. If a faster car catches up to a slower car on such a segment, the faster car will overtake. The overtaking happens instantly, without the cars involved changing their speeds. Overtaking can be performed even at the ends of a segment with dashed lines. Segments with continuous lines, where overtaking cannot be performed. If a faster car catches up to a slower car on such a segment, the faster car will instantly slow down to match the speed of the slower car. Until the end of the segment, the two cars will continue their journey together, having the same position and the same speed. If a segment with dashed lines follows, the faster car will overtake at the first point of the segment and will instantly revert to its initial speed. It is guaranteed that all encounters between any two cars will occur at integer positions. Determine for each of the $N+M$ cars the number of seconds needed to reach the destination.

## Input data

The input file `cars.in` contains the integers $N$, $M$, $K$, $L$, $A$, and $B$ on the first line. The next line contains $N$ integers separated by spaces, representing the positions of the $N$ fast cars, in ascending order. The next line contains $M$ integers separated by spaces, representing the positions of the $M$ slow cars, in ascending order. Each of the next $K$ lines contains a pair of integers $l_i$ $r_i$, representing the endpoints of a segment of road with continuous lines. The segments do not overlap and do not share endpoints. Any point of the highway that is not part of a segment with continuous lines is part of a segment with dashed lines.

## Output data

The output file `cars.out` must contain $N+M$ real values, each on a new line. Each of the first $N$ values represents the travel duration of a fast car, in the same order as the input data. Each of the next $M$ values represents the travel duration of a slow car, in the same order as the input data.

## Constraints

$1 \leq N, M \leq 20\ 000$

$1 \leq K \leq 100$

$N + M < L \leq 1\ 000\ 000\ 000$

$1 \leq B < A \leq 1\ 000$

$0 \leq$ position of any car $< L$

$0 \leq l_1 < r_1 < \dots < l_i < r_i < \dots l_k < r_k \leq L$

There are no cars starting from the same position.

The time for each car will be considered correct if it differs by at most $10^{-4}$ from the correct answer.

For some tests worth 5 points, $N = M = 1$.

For other tests worth 5 points, $K = 1$, $l_1 = 0$, $r_1 = L$.

For other tests worth 10 points, $N, M \leq 100$, $L \leq 1\ 000$.

For other tests worth 30 points, $N, M \leq 1\ 000$, $L \leq 500\ 000$.

The problem will be evaluated on tests worth 90 points.

## Example

`cars.in`

```
1 1 2 100 12 8
18
25
0 20
25 50
```

`cars.out`

```
7.291667
9.375000
```

## Explanation

There is only one fast car and one slow car. The fast car starts from position $18$ and has a speed of $12$ m/s. The slow car starts from position $25$ and has a speed of $8$ m/s. The two segments of road with continuous lines are on the intervals $(0, 20)$ and $(25, 50)$. Implicitly, the segments with dashed lines are on the intervals $[20, 25]$ and $[50, 100]$. The cars meet at position $39$ (after $1.75$ seconds), at a point on a segment with continuous lines. As a result, they will continue together at a speed of $8$ m/s until position $50$, where a segment with dashed lines begins. At this point, the fast car overtakes the slow car instantly and reverts to the initial speed of $12$ m/s. It reaches the destination after $7.291667$ seconds from the start of the journey. The slow car reaches the destination after $9.375$ seconds from the start of the journey.