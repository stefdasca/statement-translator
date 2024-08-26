Android

Gigel recently bought a new phone running the Android operating system and discovered an ingenious screen locking mechanism in the security menu. A grid of $N \times M$ points appears, which the user can connect following these rules to form a pattern: Each point can be visited only once. From a point $A$, one can move to a point $B$ only if there is no other unvisited point $C$ on the segment connecting point $A$ to point $B$. One can "jump" over visited points – meaning one can move from point $A$ to point $B$ even if there is another point on the segment between them, provided the intermediate point has been visited. The order of traversing the points is relevant.

## Input data

The input file `android.in` will contain two numbers $N$ and $M$, the dimensions of the grid.

## Output data

The output file `android.out` will contain a single number, representing the number of distinct ways to form the screen unlocking pattern. Since this number can be very large, the remainder of its division by $666013$ will be printed.

## Constraints and clarifications

$
1 \leq N, M \leq 20
$

$
1 \leq N * M \leq 20
$

## Example

`android.in`

$
2 \ 2
$

`android.out`

$
64
$

## Explanation

There are $64$ distinct ways to form the screen unlocking pattern for a grid of size $2 \times 2$.