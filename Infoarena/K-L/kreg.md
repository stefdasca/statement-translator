## Task

The $N$ nodes of an undirected graph are numbered with integers from $1$ to $N$. The degree of a node $X$ of the graph is equal to the number of edges that have one of their $2$ endpoints in $X$. An undirected graph is called $K$-regular if the degree of each node is equal to $K$. An undirected graph is called connected if it is possible to reach any node from any other node by traversing only the edges of the graph. Given $K$ and $N$, construct a connected and $K$-regular undirected graph.

## Input data

The first line of the input file `kreg.in` contains the integers $K$ and $N$, separated by a space.

## Output data

The output file `kreg.out` will contain $N \cdot K / 2$ lines. Each line corresponds to an edge of the constructed graph and will contain two integers $A$ and $B$, separated by a space, representing the endpoints of the edge $(1 \leq A, B \leq N, A \ne B)$.

## Constraints and clarifications

$2 \leq K \leq 50$

$K$ is an even number.

$K + 1 \leq N \leq 10\,000$

In general, there are many connected $K$-regular graphs. You can determine any of them. The edges of the graph can be displayed in any order. Two distinct nodes of the graph can be connected by at most $1$ edge.

## Example

`kreg.in`
```
4 6
```

`kreg.out`
```
1 2
1 6
5 4
6 3
5 1
2 5
5 3
2 6
3 4
4 1
6 4
2 3
```