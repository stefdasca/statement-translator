## Task

Have you ever tried to create tests for flow problems? It's unpleasant. Your friend, whom we'll call Xdărăscu to keep his anonymity, suggested the following construction:
 
Take an undirected rooted tree, $T_1$, make an identical copy of it, $T_2$, and then connect each leaf from $T_1$ with its corresponding leaf in $T_2$ with an undirected edge. Capacities are then assigned to the edges as desired. The root of $T_1$ will be the source of the flow network, and the root of $T_2$ will be the destination. However, this wouldn't be a very good test. To demonstrate this to Xdărăscu, you've decided to write an algorithm that calculates the maximum flow in such a network for much larger instances of the problem than would normally be possible.

## Input data

The input file `symmetricgraph2.in` will contain on its first line the values $N$ and $M$ representing the number of nodes and edges of the graph, respectively. The next $M$ lines contain a triplet of numbers $X \ Y \ C$ with the meaning that there is an undirected edge of capacity $C$ between nodes $X$ and $Y$.

## Output data

The output file `symmetricgraph2.out` will contain a single value, representing the maximum flow that can be sent through the network described in the input file.

## Constraints and clarifications

4 $\leq$ $N$ $\leq$ 100\,000

The capacity of an edge is a natural number in the range [1, $10^9$].

For 40% of the score, $N$ $\leq$ 2\,000

The source of the network described in the input is node 1, and the destination is node $N$.

It is guaranteed that the graph was built according to the method described in the statement.

The root is not considered a leaf, although it may have a degree of 1.

## Example

`symmetricgraph2.in` `symmetricgraph2.out`

```
10 11
1 2 10
1 9 4
9 8 2
8 10 3
2 3 8
2 5 4
3 4 7
4 7 9
7 10 7
5 6 1
6 7 3
9
```