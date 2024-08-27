# Treespotting

Let $G = (V, E)$ be a graph with nodes from the set $V$ and edges from the set $E$. The following pseudocode is given:

$$
E' = \{\} \\
\text{define } \text{dfs}(node) \rightarrow \\
\quad \text{mark } node \text{ as visited} \\
\quad \text{for neighbor of } node \\
\quad \quad \text{if neighbor is not visited} \\
\quad \quad \quad \text{add the edge } (node, neighbor) \text{ to } E' \\
\quad \quad \quad \text{dfs}(neighbor) \\
\text{dfs}(root)
$$

It can be easily observed that $E'$ contains exactly $N - 1$ edges and that $G' = (V, E')$ represents a partial tree of the graph $G$. Given $G'$ and $G$, you have to determine for which possible values of $root$ one could obtain $G'$ from $G$.

## Task

## Input data

The input file `treespotting.in` will contain on the first line 2 natural numbers $N$ and $M$. The next $N - 1$ lines will contain 2 natural numbers each, $x$ and $y$, describing an edge from $E'$. The following $M - N + 1$ lines will contain 2 natural numbers each, $x$ and $y$, describing an edge from $E \setminus E'$.

## Output data

The output file `treespotting.out` must contain on the first line a natural number $K$ representing the number of possible values for $root$ such that one can obtain $E'$ from $G$ by applying the algorithm described in the pseudocode. The next line must contain $K$ natural numbers in increasing order separated by a space representing the possible values for $root$.

## Constraints

$2 \leq N \leq 100\ 000$

$N - 1 \leq M \leq 150\ 000$

For $40\%$ of the tests, $N \leq 3\ 000$ and $M \leq 5\ 000$

There can be self-loops and multiple edges between the same pair of nodes.

It is guaranteed that there is always at least one solution for $root$.

## Example

`treespotting.in`

```
2 1
1 2
```

`treespotting.out`

```
2
1 2
```

`treespotting.in`

```
3 3
1 2
2 3
1 3
```

`treespotting.out`

```
2
1 3
```

## Explanation

For the first test, no matter how we set the root, we obtain the edge $(1, 2)$.

For the second test, if we set the root as $1$ (or $3$), the next neighbor in the pseudocode execution can be $2$, adding the edge $(1, 2)$ (or $(3, 2)$), and then adding the other edge $(3, 2)$ (or $(1, 2)$). However, if we set the root as $2$, we cannot obtain the edges $(1, 2)$ and $(2, 3)$.