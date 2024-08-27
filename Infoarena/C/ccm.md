# CCM

Given an undirected bipartite graph $G = (V = (L, R), E)$. A matching in $G$ is a subset of edges $M$ such that for any vertex $v$ in $V$, there is at most one edge in $M$ incident to $v$.

## Task

Given an undirected bipartite graph $G$, determine the number of maximum cardinality matchings.

## Input data

The input file `ccm.in` contains on the first line three natural numbers $n$, $m$ and $e$, where $n$ represents the cardinality of set $L$ and $m$ the cardinality of set $R$.
On the next $e$ lines, there are two natural numbers, separated by a space, $u$ and $v$, signifying that there is an edge from node $u$ in $L$ to node $v$ in $R$.

## Output data

In the output file `ccm.out`, print two values separated by a space, representing the value of the maximum cardinality matching and their number modulo $9901$.

## Constraints and clarifications

$1 \leq n, m \leq 16$

$1 \leq e \leq n * m$

Nodes in sets $L$ and $R$ are represented by natural numbers from $1$ to $n$ and from $1$ to $m$, respectively.

## Example

`ccm.in`
```
3 2 5
1 1
1 2
2 1
2 2
3 2
```

`ccm.out`
```
2 4
```

## Explanation

The four maximum matchings are $(1, 1), (2, 2)$, $(1, 1), (3, 2)$, $(1, 2), (2, 1)$, and $(2, 1), (3, 2)$.