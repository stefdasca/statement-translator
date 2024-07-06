Certainly! Here is the translated problem statement:

---

To spend her time in a pleasant way, Hetty decided to open her math book and choose a problem to think about while cleaning the house. In the book, she found the following task:

Given an undirected graph with $N$ nodes and $M$ edges, which has the property of being almost $R$-regular, where $R$ is a given natural number. A graph is almost $q$-regular if the degree of any node $x$ (the number of nodes adjacent to $x$) is either $q$ or $q-1$. We need to determine if it is possible to remove a subset of edges from the initial graph so that the resulting graph is almost $(R-1)$-regular. If this is possible, we also need to determine the subset of edges that should be removed.

# Input data

The input file `ar.in` contains the natural numbers $N$, $M$, and $R$ on the first line, representing the number of nodes, the number of edges, and the fact that the given graph is almost $R$-regular. On the next $M$ lines, there will be $M$ pairs of numbers $x$ and $y$, indicating the existence of an edge between nodes $x$ and $y$.

# Output data

In the output file `ar.out`, the first line will contain the natural number $K$. This has the value $-1$ if the initial graph cannot be transformed into an almost $(R-1)$-regular graph by removing a subset of edges. Otherwise, $K$ represents the number of edges removed, and on the next $K$ lines, there will be $K$ pairs of numbers $x$ and $y$, each representing the fact that the edge between nodes $x$ and $y$ in the initial graph has been removed.

# Constraints and clarifications

* $1 \leq N \leq 20 \ 000$ 
* $1 \leq M \leq 200 \ 000$
* $2 \leq R < N$
* Any correct solution will be accepted if it exists.
* There is at most one edge between each pair of nodes.
* For tests worth $20$ points, $M \leq 20$.

# Example

`ar.in`

```
4 5 3
1 2
2 3
3 4
4 1
1 3
```

`ar.out`

```
1
1 3
```

## Explanation

The given graph is almost $3$-regular: nodes $1$ and $3$ each have $3$ neighbors, while nodes $2$ and $4$ each have $2$ neighbors. By removing the edge $(1, 3)$, all nodes have exactly $2$ neighbors, and the graph becomes almost $2$-regular.
Another possible solution is:
$2$
$1 \\ 2$
$3 \\ 4$
Thus, nodes $2$ and $4$ remain with $1$ neighbor each, and nodes $1$ and $3$ each remain with $2$ neighbors. In this case, the graph becomes almost $2$-regular.

---

I have carefully translated and checked the problem statement to ensure it follows the rules of English grammar and syntax.