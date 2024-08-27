## Task

You have probably all heard of the Roy-Floyd algorithm. This algorithm determines the minimum distances between any two nodes of an undirected graph, with positive edge costs. Given a connected undirected graph, from which the edge costs have been deleted, as well as the result of applying the Roy-Floyd algorithm on this graph (before the deletion of edge costs), you have to determine if edge costs can be assigned to all edges of the graph such that the given result is obtained.

## Input data

The first line of the input file `rfinv.in` contains the integer $T$, representing the number of tests. In the following, the $T$ tests follow. Each test has the following structure. The first line of each test contains $2$ integers $N$ and $M$, representing the number of nodes and the number of edges in the graph. The next $M$ lines contain $2$ different integers $a$ and $b$, indicating the existence of an edge between nodes numbered $a$ and $b$. The next $N$ lines contain $N$ integers each, representing the result of the Roy-Floyd algorithm. The $i$-th line among these $N$ lines contains the minimum distances between node $i$ and each of the $N$ graph nodes.

## Output data

For each test, print in the output file `rfinv.out` one line containing the string "DA" if it is possible to assign costs to the edges of the graph such that the result of the Roy-Floyd algorithm matches the given one, or the string "NU" otherwise.

## Constraints and clarifications

$1 \leq T \leq 30$

$1 \leq N \leq 50$

$0 \leq M \leq N*(N-1)/2$

Let $d_{min}(i,j)$ be the minimum distance between nodes $i$ and $j$ resulting from applying the Roy-Floyd algorithm. It is guaranteed that $d_{min}(i,i)=0$ and $d_{min}(i,j)=d_{min}(j,i)$.

The minimum distances between any $2$ different nodes are integers within the range $[1, 10000]$.

## Example

`rfinv.in`

```
2
3 2
1 2
3 2
0 5 10
5 0 4
10 4 0
2 1
1 2
0 13 13 
13 0 
NU 
DA
```