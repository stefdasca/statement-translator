# The Wave

On the surface of the water in a well at a certain tourist site $X$, there are $N$ floating leaves. Damia throws a 50 bani coin into the well to bring good luck. The wave created by the coin hits the $N$ leaves in the order $1, 2, \dots, N$ at distinct moments in time. Damia, not knowing exactly where the coin hit the surface of the water, will ask for a possible position such that the leaves have been hit by the resulting wave in the above order. (Damia firmly believes that the luck resulting from throwing the coin into the well is strictly related to the spot where it hit the surface of the water.)

## Input data

The input file `unda.in` contains on the first line the number $N$. On each of the following $N$ lines, there is a pair of numbers representing the coordinates of a leaf. The leaves will be given in the order in which they are hit by the wave.

## Output data

The output file `unda.out` will contain a possible position for the spot where the coin could have hit the surface of the water.

## Constraints and clarifications

$1 \leq N \leq 100$

The coordinates of the leaves are real numbers with an absolute value less than $1\ 000\ 000\ 000$.

The wave can be considered as a circle with a continually increasing radius, centered at the point where the coin hit the water.

The leaves will not change their coordinates after being hit by the wave.

If there is no solution, print "Nu exista solutie.", without quotes.

If there is a solution, then the coordinates of the solution lie within the interval $[-2\ 000\ 000\ 000, 2\ 000\ 000\ 000]$.

## Example

`unda.in`
```
3
0 3
0 2
0 1
```

`unda.out`
```
0.000000 3.000000
```

## Explanation

Another solution could have been $0, 4$.