## Task

Given a graph with $N$ nodes and $M$ bidirectional edges. For each edge, the time required to traverse that edge is known. Yoshino is at node $S$ (source) and follows a PREDETERMINED path to node $D$ (destination). Hakaze knows that when Yoshino reaches node $D$, he will die the next second. Therefore, Hakaze must find Yoshino before he reaches the destination (or meet him exactly at the destination). Hakaze is curious about how many nodes she can start from to meet Yoshino before he dies (they can meet either at a node or on an edge).

## Input data

The input file `tempest.in` will contain on the first line a number $T$, the number of tests. For each test:
- The first line will contain $N$, $M$, $S$, and $D$.
- The next $M$ lines will contain 3 numbers $x$ $y$ $time$, representing that there is a bidirectional edge from $x$ to $y$ which takes $time$ units of time to traverse.
- The next line contains a number $K$ (the number of edges traversed by Yoshino).
- The last line will contain $K$ numbers, the indices of the edges.

## Output data

The output file `tempest.out` will contain for each of the $T$ tests 2 lines. On the first line, $R$, the number of nodes from which Hakaze can start. On the second line, the indices of those $R$ nodes.

## Constraints and clarifications

1 $\leq$ $T$ $\leq$ 10

1 $\leq$ $N$ $\leq$ 100,000

1 $\leq$ $M$ $\leq$ 300,000

The edge costs will be in the interval \[1, 1,000,000,000\]

The $K$ nodes must be printed in ascending order

## Example

`tempest.in`
```
1  
5 8 1 2
1 2 5 
2 3 3
1 3 4
1 4 2
4 1 4
4 5 2
5 6 2
1 5 10
3
5 7 2
```

`tempest.out`
```
3  
2 3 4
```

Double-checked and fixed potential grammar and syntax errors.