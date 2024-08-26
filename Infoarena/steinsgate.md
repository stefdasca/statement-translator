# Steins;Gate

Okabe needs to decipher a new mystery. To achieve this goal, he must determine the risk of forming a paradox in each timeline he is in. Specifically, consider a graph with $N$ nodes and $M$ ORIENTED edges (the nodes represent states in time and the edges represent relationships between these states, which is irrelevant). For each node $X$, a value $risc[X]$ at event $0$ is known. After each new event, the risk in a node $X$ propagates to all its neighbors (if there is an edge from $X$ to $Y$). Because the universe is complicated, the risk of a node becomes, after each event, the maximum of the values that propagate to this node. Okabe's mission is to find the risk in each node after $K$ events.

## Input data

The input file `steinsgate.in` will contain on the first line 3 natural numbers $N$, $M$ and $K$. The next $M$ lines contain 2 natural numbers $X$ and $Y$ representing an edge from $X$ to $Y$. On the last line, there will be $N$ natural numbers, the $i$-th element representing the risk of node $i$ at event $0$.

## Output data

The output file `steinsgate.out` will contain a single line with $N$ natural numbers representing the risk of each node after $K$ events.

## Constraints

$1 \leq N \leq 200$

$1 \leq M \leq N \times N$

$1 \leq K \leq 1\,000\,000\,000$

$1 \leq risc[i] \leq 1\,000\,000\,000$

It is guaranteed that for each node $X$, there is at least one node $Y$ such that there is an edge from $Y$ to $X$ (there is at least one node $Y$ that propagates its risk to $X$).

For tests worth 30 points $K \leq 100\,000$

## Example

`steinsgate.in`

```
5 6 3
1 2
2 3
3 4
4 5
5 1
1 4
7 3 9 1 4
```

`steinsgate.out`

``>
9 1 4 7 4
```