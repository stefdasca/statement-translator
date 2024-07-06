# Task <br>

Given an undirected connected graph with $n$ nodes and $m$ edges with costs. A black and white coloring of the graph is *correct* if: <br>

- The subgraph obtained from the white nodes and the edges that connect two white nodes is connected;
- The subgraph obtained from the black nodes and the edges that connect two black nodes is connected;

The value of a *correct coloring* is equal to the sum of the costs of the minimum spanning trees of the two resulting subgraphs. <br>

What is the minimum value of a *correct coloring* of the given graph? <br>

# Input data <br>

The input file **retrotrees.in** will contain on the first line two numbers $n$ and $m$ ($2 \le n \le 3 \cdot 10^5$, $1 \le m \le min(3 \cdot 10^5,\frac{n \cdot (n-1)}{2})$) — the number of nodes and the number of edges of the graph, respectively. <br>

Each of the following $m$ lines will contain three numbers $u$, $v$, and $c$ ($1 \le u,v \le n$, $u \neq v$, $1 \le c \le 10^9$), meaning that there is an undirected edge between nodes $u$ and $v$ with cost $c$. <br>

It is guaranteed that for any pair of nodes $(u,v)$, there is at most one edge between $u$ and $v$.

# Output data <br>

The output file **retrotrees.out** will contain the minimum value of a *correct* coloring of the given graph. <br>

# Constraints and clarifications <br>

- For $15$ points, $m=n-1$
- For $25$ points, $n \le 15$
- For $25$ points, $n,m \le 3000$
- For $35$ points, there are no additional constraints.

# Examples <br>

## Example 1:

**retrotrees.in**
```
4 5
1 2 4
2 3 1
2 4 2
1 3 3
3 4 3
```
**retrotrees.out**
```
3
```

## Example 2:

**retrotrees.in**
```
8 12
1 2 2
1 3 2
1 4 3
2 3 3
2 4 5
3 4 5
3 5 4
5 6 3
5 7 5
7 8 2
6 7 3
6 8 5
```
**retrotrees.out**
```
15
```

## Example 3:

**retrotrees.in**
```
15 15
4 1 5
4 2 7
2 6 13
6 11 7
11 13 9
4 12 11
14 6 5
15 14 15
13 8 10
5 2 10
11 10 13
3 10 14
7 5 14
9 4 12
6 5 8
```
**retrotrees.out**
```
125
```

# Explanation
An optimal correct coloring of the graph from the first example <br>
~[retrotrees1.png] <br>

The partial graph formed by the white nodes contains node $1$ and no edges, therefore the minimum spanning tree of the white subgraph will have a total cost equal to $0$. <br>

The partial graph formed by the black nodes contains nodes $2,3,4$ and the edges $(2,3)$, $(2,4)$, and $(3,4)$. The minimum spanning tree obtained from the black subgraph will contain the edges $(2,3)$ and $(2,4)$, with a total cost of $1+2=3$. <br>
** **
An optimal correct coloring of the graph from the second example <br>
~[retrotrees2.png] <br>