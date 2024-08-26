# Subtree

Given a connected, undirected graph with costs that has $N$ nodes and $M$ edges. Additionally, $T$ special nodes are provided. Find a minimum-cost subtree included in the given graph that contains the $T$ special nodes.

## Task

## Input data

The first line of the input file `subarbore.in` contains $N$, the number of nodes, and $M$, the number of edges. The next $M$ lines will contain 3 numbers each, $a$, $b$, and $c$, indicating that there is an edge between nodes $a$ and $b$ with cost $c$. The $M+2$-th line will contain the number of special nodes, $T$. The last line of the file will contain the $T$ special nodes.

## Output data

The output file `subarbore.out` will contain a single number, representing the cost of the subtree with the mentioned property.

## Constraints and clarifications

$1 \leq N \leq 40$

$1 \leq M \leq N * (N - 1) / 2$

$1 \leq T \leq 7$

The costs of the edges will be natural numbers between $1$ and $1\ 000\ 000$

For $30\%$ of the tests, $N \leq 20$

## Example

`subarbore.in`
```
5
5
2 1 1
3 1 2
5 2 10
4 3 6
4 5 6
3
4 2 5
```

`subarbore.out`
```
15
```