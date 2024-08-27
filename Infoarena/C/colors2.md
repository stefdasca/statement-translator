# Colors2

## Task

A connected undirected graph with $N$ nodes and $M$ edges is given. Initially, each node $u$ has a color $a_u$, encoded by a natural number between 1 and $N$. You can repeatedly modify the colors of the nodes using the operation $a_u = \min(a_u, a_v)$, where $u$ and $v$ are connected by an edge. Given a final coloring $b_1 \dots b_N$, determine if it is possible to transform $a$ into $b$.

## Input data

The input file `colors2.in` contains multiple tests which must be answered separately. The first line contains the number of tests. Each test is structured as follows:
$N$
$M$
$a_1 \; a_2 \dots a_N$
$b_1 \; b_2 \dots b_N$
$u_1 \; v_1$
$u_2 \; v_2$
$\dots$
$u_M \; v_M$

## Output data

In the output file `colors2.out`, for each test, you must print on separate lines $1$ if $a$ can be transformed into $b$ using the mentioned operation, and $0$ otherwise.

## Constraints

$1 \leq N \leq 150\,000$  
$N - 1 \leq M \leq 250\,000$

For 15 points, the graph is a star ( $M = N - 1$ and one node is connected to all other nodes),  
$N^2 \leq 5\,000\,000$  

For 7 points, the graph is complete,  
$N \leq 50$,  
$N \times M \leq 12\,000\,000$

For 8 points, the graph is a chain ( $M = N - 1$),  
$N^2 \leq 5\,000\,000$  

For 15 points, the graph is a chain with no other restrictions

For 7 points, the graph is a tree,  
$N^2 \leq 5\,000\,000$  

For 16 points, the graph is a tree, and the coloring $a$ is a permutation of the set $\{1, 2, \dots, N\}$

For 10 points,  
$N \times M \leq 5\,000\,000$  

## Example

`colors2.in`
```
2
4 4
3 3 2 1
2 1 2 1
1 2
2 3
3 4
4 2
4 4
3 3 2 1
1 1 2 2
1 2
2 3
3 4
4 2
```

`colors2.out`
```
1
0
```

## Explanations

For the first graph, the required operations are:  
$a_2 = \min(a_2, a_3) = 2$  
$a_1 = \min(a_1, a_2) = 2$  
$a_2 = \min(a_2, a_4) = 1$