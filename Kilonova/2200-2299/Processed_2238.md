```markdown
# Task

Given an undirected graph with $N$ nodes (numbered from $1$ to $N$) and $M$ edges, we define $A(i,j) = 1$ if nodes $i$ and $j$ are adjacent (there is an edge between them), and $A(i,j) = 0$ if nodes $i$ and $j$ are not adjacent.
A subset $S$ of the graph's nodes is called a *module* if it meets the following condition: for any three nodes $x$, $y$, and $z$ such that $x \in S$, $y \in S$ and $z \notin S$, we have $A(x, z) = A(y, z)$.
More precisely, for any node $z$ outside the set $S$, either all nodes in $S$ are adjacent to $z$ or no nodes in $S$ are adjacent to $z$. Some simple examples of modules are: the empty set, the set of all nodes in the graph, sets that consist of a single node of the graph.
Determine the number of modules of the given graph, modulo $34949$.

# Input data

The first line of the input file `module.in` contains the integers $N$ and $M$, separated by a space. The next $M$ lines contain two integers $i$ and $j$, separated by a space, indicating that there is an edge between node $i$ and node $j$ in the graph.

# Output data

The output file `module.out` will contain the number of modules of the given graph, modulo $34949$.

# Constraints and clarifications

* $1 \leq N \leq 100$
* $0 \leq M \leq \frac{N \cdot (N - 1)}{2}$
* $1 \leq i, j \leq N$
* $i \neq j$
* In the input file, edges will not be repeated.

# Example

`module.in`
```
7 11
5 1
5 6
1 2
1 3
1 7
6 2
6 3
6 7
4 2
4 3
4 7
```

`module.out`
```
14
```

## Explanation

The $14$ modules are:
$\{ \}, \{1\}, \{2\}, \{3\}, \{4\}, \{5\}, \{6\}, \{7\}, \{1,6\}, \{2,3\}, \{2,7\}, \{3,7\}, \{2,3,7\}, \{1,2,3,4,5,6,7\}$.
```