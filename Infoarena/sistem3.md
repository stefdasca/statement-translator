## Task

You are given an undirected and connected graph $G$ with $N$ nodes and $N$ edges. Each node in this graph has an associated value called potential. The potential of node $i$ is $p[i]$. Additionally, each edge of the graph has an associated cost. We define the gradient of a node $i$ as the sum $(p[j] - p[i]) * w[j][i]$ modulo $M$ (given $M$) where $j$ is a neighbor of $i$, and $w[j][i]$ is the cost of the edge between $i$ and $j$. Unfortunately, the potentials of the nodes have been lost. However, we know the gradients for each node and the costs on the edges. You are asked to reconstruct the potentials of the nodes knowing that they had values between $0$ and $M - 1$.

## Input data

The input file `sistem3.in` will contain on the first line two natural numbers $N$ and $M$ representing the number of nodes (and edges) in the graph, respectively the value against which the modulo is taken. The next $N$ lines will each contain 3 natural numbers $x$, $y$ and $w$ with the meaning: there is an edge between node $x$ and node $y$ with cost $w$. The last line will contain $N$ natural numbers, the $i$-th value representing the gradient of node $i$.

## Output data

The output file `sistem3.out` should contain $N$ lines each containing a natural value between $0$ and $M - 1$, these representing in order the potentials of nodes $1$, $2$, $\dots$, $N$.

## Constraints and clarifications

$1 \leq N \leq 100\,000$

$1 \leq x, y \leq N$

$1 \leq w \leq M - 1$

$2 \leq M \leq 46\,000$

$M$ is prime

$0 \leq gradient$ of any node $\leq M - 1$

For 30% of tests $N \leq 100$

For 50% of tests one of the edges is of the form $x$ $x$ $w$

## Example

`sistem3.in`

```
4 2
4 2 1
2 1 1
4 1 1
3 1 1
0 1 0 0
```

`sistem3.out`

```
0
0
1
0
```

`sistem3.in`

```
5 5
2 4 4
4 3 5
4 3 1
3 4 1
4 1 5
4 4 1 2 2
```

`sistem3.out`

```
0
4
4
3
0
```