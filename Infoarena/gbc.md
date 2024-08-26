## Gbc

Let $G = (V, E)$ be an undirected graph with $V$ being the set of vertices, and $E$ being the set of edges. We want to choose two sets $A, B \subseteq V$ such that $|A| = n$ ( $A$ has n elements), $|B| = m$ ( $B$ has m elements), $A \cap B = \emptyset$ ( $A$ and $B$ are disjoint), $\forall i \in A, j \in B$, edge $(i, j) \in E$ (there exists an edge between any node of $A$ and any node of $B$).

## Task

Given $G$, a connected undirected graph, count the number of ways the two sets can be chosen.

## Input data

The first line of the input file `gbc.in` contains three integers $k$ - the number of nodes in the graph $G$, $n$ and $m$ - with the meanings described above. The next $k$ lines contain $k$ numbers $0$ or $1$ with the meaning that if on line $i+1$, on column $j$ there is $1$, then there is an edge between the nodes $i$ and $j$.

## Output data

The output file `gbc.out` will contain the number of ways the two sets can be chosen on the first line.

## Constraints

$1 \leq n, m \leq 8$

$1 \leq k \leq 30$

there is no edge from a node to itself

## Example

`gbc.in`
$4$ $2$ $2$
$0101$
$1010$
$0101$
$1010$

`gbc.out`
$2$

## Explanation

Set $A=\{1,3\}$, $B=\{2,4\}$

Set $A=\{2,4\}$, $B=\{1,3\}$