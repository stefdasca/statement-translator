Given a tree (an undirected connected acyclic graph) with $N$ nodes and $N-1$ edges, each labeled with a **lowercase** letter. We define a path $(x, y)$ as the sequence of edges leading from node $x$ to node $y$. Also, we consider the paths $(x, y)$ and $(y, x)$ to be the same path. A path can be palindromic if there is a way to permute all the letters along the path such that a palindromic path is formed.

# Task

Determine how many paths can be palindromic.

# Input data

The first line contains the number $N$, representing the number of nodes.

The following $N-1$ lines contain a triplet $a \\ b \\ ch$, representing the edge from node $a$ to node $b$, labeled with the character $ch$.

# Output data

Print on one line the number of paths that can be palindromic.

# Constraints and clarifications

* $1 \leq N \leq 100 \ 000$

# Example

`stdin`
```
8
1 2 a
1 3 a
2 7 b
2 8 b
3 4 b
4 5 a
4 6 a
```

`stdout`
```
21
```

## Explanation

The paths that can be palindromic are: $(1, 2)$, $(1, 3)$, $(1, 5)$, $(1, 6)$, $(2, 3)$, $(2, 4)$, $(2, 7)$, $(2, 8)$, $(3, 4)$, $(3, 7)$, $(3, 8)$, $(4, 5)$, $(4, 6)$, $(4, 7)$, $(4, 8)$, $(5, 6)$, $(5, 7)$, $(5, 8)$, $(6, 7)$, $(6, 8)$, $(7, 8)$.

~[tree.png]