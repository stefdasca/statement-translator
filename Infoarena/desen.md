# Drawing

Miruna draws $N$ points on a plane. She defines a spanning tree for a set of $S$ points as a subset of exactly $S-1$ segments, with endpoints among the given points, such that one can reach any point from any other point by traveling along the chosen segments. Miruna also defines the minimum cost spanning tree as the spanning tree for which the sum of the lengths of the segments in the chosen subset is minimal.

## Task

After drawing a new point on the plane, Miruna wants to find the sum of the lengths of the segments that form the minimum cost spanning tree for all the points drawn up to that moment.

## Input data

The first line of the input file `desen.in` contains a single integer $N$, representing the number of points drawn by Miruna.

The next $N$ lines contain $2$ integers each, representing the coordinates of a newly drawn point.

## Output data

The output file `desen.out` will contain $N$ real numbers, representing the sum of the lengths of the segments that form a minimum cost spanning tree after each point drawn by Miruna.

## Constraints and clarifications

$1 \leq N \leq 1000$

The coordinates of the points will be integers between $0$ and $1000$

There is a possibility that some points may coincide

An error of $0.001$ will be accepted

## Example

`desen.in`

$5$

$0$ $0$

$0$ $2$

$2$ $0$

$2$ $2$

$1$ $1$

`desen.out`

$0.000000$

$2.000000$

$4.000000$

$6.000000$
 
$5.656854$