## Task

A directed acyclic graph with $N$ nodes and $M$ edges and a natural number $K$ is given. The edges are assigned non-negative costs. Determine a path with at least $K$ edges for which the difference between the sum of the largest $K$ edges on the path and the sum of the smallest $K$ edges on the path is maximum. You do not need to find the actual path, just determine this value.

## Input data

The input file `kgraf.in` contains the numbers $N,M$ and $K$ on the first line. Each of the following $M$ lines will contain a triplet in the form $a,b,c$, with the property that there is an edge from $a$ to $b$ with cost $c$.

## Output data

The output file `kgraf.out` will contain a single number $S$ representing the value requested in the statement. If there is no path with at least $K$ edges, print $-1$ as the answer.

## Constraints and clarifications

1 $\leq$ $N,K$ $\leq$ 300

0 $\leq$ $M$ $\leq$ 900

The edge costs are non-negative numbers less than or equal to 1 000 000

For 25% of the tests $N \leq 15$ 

and $M \leq 30$

For another 25% of the tests $N \leq 100$ 

For 70% of the tests $K \leq 200$

## Example

`kgraf.in`
```
3 4 2 
1 3 0 
2 1 0 
1 3 4 
2 1 4 
```

`kgraf.out`
```
0
```