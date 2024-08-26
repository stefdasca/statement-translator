# Stars

Lately, having heard that Elon Musk is preparing to reach Mars, Andrei has become interested in astronomy. Since he also has a knack for drawing, he's wondered: how many perfect stars with $N$ vertices can he draw?

A star is perfect if:
* it starts and ends at the same vertex
* it is drawn without lifting the pen from the paper
* the vertices are equidistant points on a circle and the measure of the angle at each vertex is the same

Additionally, a regular polygon is NOT a star, so connecting two adjacent points is forbidden. Two stars are considered different if the angles at the vertices corresponding to each star are different. Therefore, the rotation of a star is NOT considered.

Given $N$, calculate the number of perfect stars with $N$ vertices.

## Example

For $N = 7$, the 2 possible perfect stars are:

## Input data

The input file `stele.in` contains on the first line $K$, the number of tests, and on the following $K$ lines a single value $N$, the number of points.

## Output data

The output file `stele.out` will contain $K$ lines, on each line $i$, the number of perfect stars corresponding to the value on line $i+1$ of the input file.

## Constraints

$1 \leq K \leq 10$ 

$5 \leq N \leq 2500000$

## Example

`stele.in`
```
2
7
23
```

`stele.out`
```
2
210
```