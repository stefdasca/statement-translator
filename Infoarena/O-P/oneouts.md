# One Outs

Tokuchi Toua has a new baseball game that he needs to win. We can consider the baseball field as a polygon with $N$ vertices on a plane, and Toua (the pitcher) is located at a point inside the polygon. Toua can position a teammate at one of the $N$ points. When the teammate receives the ball, he starts running to make a home run (running along the perimeter of the polygon until he reaches the point of another teammate). The goal is to position one or more teammates such that they cover the entire perimeter of the polygon in the shortest possible time. For simplicity, we assume that the traversal times of the edges between any two consecutive points on the polygon, as well as the time required to throw the ball to each of the $N$ points, are known. The time required for a teammate to complete his home run is calculated as follows: the time until he receives the ball from the pitcher + the time he runs from his current point to the next teammate's point. Toua can position at most $K$ teammates in $K$ out of the $N$ points. You need to help him achieve this such that the maximum time required for a teammate to complete his home run is minimized.

## Task

## Input data

The input file `oneouts.in` contains on the first line 2 natural numbers $N$ and $K$. On the next line, there will be $N$ natural numbers representing the traversal time of the distance between any 2 consecutive points on the polygon (point $1$ with $2$, $2$ with $3$, $\ldots$, $N$ with $1$). On line 3, there will be another $N$ natural numbers, the $i$-th representing the time required for Toua to throw the ball from his current position to the point with index $i$ on the polygon.

## Output data

The output file `oneouts.out` will contain a single natural number representing the minimum required time.

## Constraints and clarifications

$1 \leq K \leq N \leq 100\ 000$

All values in the input are from the interval $[1, 1\ 000\ 000\ 000]$

The polygon mentioned in the statement is fictitious. Generally, there is no geometric relationship between the times described in the input file.

When teammates are running their home run, they must move to the right. Thus, if they are at point $N$, they will move towards point $1$, and if they are at another point $i$, they will move towards point $i+1$.

For 20% of the tests, $N \leq 20$, and all other values in the input are from the interval $[1, 10\ 000]$.

For 40% of the tests, $N \leq 1\ 500$.

## Example

oneouts.in

`5 2`

`3 1 2 3 2`

`3 3 1 2 4`

oneouts.out

`8`

## Explanation

Toua will place his 2 teammates at vertices 1 and 3. 
The teammate at vertex 1 will complete his home run in $3$ (the time required for Toua to throw the ball to him) + $3$ + $1$ (the time required to run to the position of the next teammate) = $7$.
The teammate at vertex 3 will complete his home run in $1$ (the time until the ball reaches him) + $2$ + $3$ + $2$ = $8$.