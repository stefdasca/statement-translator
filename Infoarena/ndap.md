Ndap

Let $G = (V, E)$ be an undirected graph with $V$ being the set of vertices, and $E$ the set of edges. We define a partial graph of $G$ as the graph $P = (V, E')$ with $E'$ being a subset of $E$. Given $G$, a connected undirected graph, determine how many connected partial graphs $G$ has.

## Task

## Input data

The first line of the input file `ndap.in` contains two numbers $N$ and $M$ representing the number of nodes, and the number of edges in the graph $G$, respectively. The file then contains $M$ lines that describe the graph. On line $i+1$, with $1 \leq i \leq M$, there will be two numbers $a_i$ $b_i$ indicating that there is an edge from $a_i$ to $b_i$ in $G$. The nodes will be numbered from $0$ to $N-1$.

## Output data

The output file `ndap.out` will contain on the first line the required number modulo $30103$.

## Constraints

$1 \leq N \leq 15$

$0 \leq a_i$, $b_i \leq N-1$

Any edge will appear at most once in the input file.

## Example

`ndap.in`
`ndap.out`
```
4 3
0 1
2 1
1 3
1
```
```
4 4
0 1
1 2
2 3
3 0
5
```
```
5 4
0 1
1 2
2 3
3 0
14
```

## Explanation

In the first example, the graph is a tree and therefore has only one connected partial graph (any edge removal makes the graph disconnected). In the second example, the graph is a cycle consisting of 4 edges. There are 5 connected partial graphs because at most one edge can be removed while the graph remains connected.