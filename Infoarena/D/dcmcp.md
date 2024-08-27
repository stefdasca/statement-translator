## Task

Consider an undirected graph with $N$ nodes, numbered from $1$ to $N$, and $M$ edges. Node $1$ corresponds to a mine where some precious minerals are extracted. Node $N$ corresponds to a processing factory for the minerals. Each edge has an associated traversal duration (expressed in time units) and capacity (expressed in units of minerals). It has been decided that the minerals extracted from the mine will be transported to the factory using a single path. This path must have the highest possible capacity, to be able to transport as many units of minerals at the same time as possible. The capacity of a path is equal to the minimum capacity of an edge on the path. Because the minerals are very sensitive, they will decompose after $T$ units of time from their extraction at the mine. Therefore, the total traversal duration of the chosen path (the sum of the traversal durations of the edges on the path) must be less than or equal to $T$.

## Input data

The first line of the input file `dcmcp.in` contains an integer $X$, representing the number of tests to follow. The first line of each test contains 3 integers, separated by spaces: $N$, $M$, and $T$. Each of the next $M$ lines will contain 4 integers, separated by spaces: $A$, $B$, $C$, and $D$, indicating that there is an edge between nodes $A$ and $B$, with capacity $C$ and traversal duration $D$. $A$ and $B$ are different integers between $1$ and $N$.

## Output data

For each of the $X$ tests, in the order from the input file, print in the output file `dcmcp.out` a line containing the maximum capacity of a path from the mine to the factory, having the required properties.

## Constraints and clarifications

$1 \leq X \leq 10$

$2 \leq N \leq 10\ 000$

$1 \leq M \leq 50\ 000$

$1 \leq T \leq 500\ 000$

$1 \leq$ capacity of any edge $\leq 2\ 000\ 000\ 000$

$1 \leq$ traversal duration of any edge $\leq 50\ 000$

There will be at most one edge between any 2 nodes.

## Example

`dcmcp.in`
```
2
2 1 10
1 2 13 10
4 4 20
1 2 1000 15
2 4 999 6
1 3 100 15
3 4 99 4
```

`dcmcp.out`
```
13
99
```