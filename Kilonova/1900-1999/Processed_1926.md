We have a tree with $N$ nodes and the root in node $1$, indexed from $1$ to $N$. Each edge is labeled with a letter.
For two nodes $(x, y)$ where $x$ is an ancestor of $y$, we define the ancestral string as the concatenation of the edges on the path from $y$ to $x$.

# Task

On this tree, $Q$ queries are made, a query has the form of a pair $(x, y)$ where $x$ is an ancestor of $y$. Let $S$ be the ancestral string corresponding to nodes $x$ and $y$.

For each query, you need to find how many pairs $(a, b)$ (including $(x, y)$) give the ancestral string equal to $S$.

# Input data

The input file `parb.in` contains the number $N$ of nodes, followed by the number $Q$ of queries on the first line. There will follow $N-1$ lines, each line will contain a triplet $(x, y, c)$ representing that there exists an edge from $x$ to $y$ which is labeled with the character $c$. Next, $Q$ lines follow, each line contains a pair $(x, y)$ corresponding to a query.

# Output data

The output file `parb.out` will contain $Q$ lines. Each line $i$ will contain a single integer, the answer to the query $i$.

# Constraints and clarifications

* $1 \leq N \leq 100\ 000$
* $0 \leq Q \leq 100\ 000$
* The edges are labeled with lowercase English letters.
* For tests worth $20$ points, $N \leq 100$.

# Example

`parb.in`
```
10 4
1 2 m
2 3 m
3 4 c
3 5 c
5 6 l
2 7 c
1 8 c
8 9 m
9 10 c
2 5
1 9
9 10
1 4
```

`parb.out`
```
4
1
5
2
```