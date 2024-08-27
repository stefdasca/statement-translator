## Task

Given a planar graph, find the two required numbers.

## Input data

The first line of the input file contains two natural numbers separated by spaces $N$ and $M$ (the number of nodes and the number of edges of the planar graph, respectively).

Lines $2 \dots M + 1$ contain two numbers $A$ and $B$ indicating that there is a bidirectional edge between nodes $A$ and $B$ (the nodes of the graph are numbered from $1$ to $N$).

## Output data

The output file will contain on the first line two numbers $X$ and $Y$ representing the maximum number of nodes a complete subgraph can have and the number of complete subgraphs with $X$ nodes in the given planar graph, respectively.

## Constraints and clarifications

$2 \leq N \leq 30\,000$

$1 \leq M \leq 60\,000$

$Y \leq 2^{30}$

For $70\%$ of the tests $N \leq 2000$

## Example

`count.in`

```
5 8
1 2
1 3
1 5
2 4
2 5
3 4
3 5
4 5
```

`count.out`

```
3 4
```

## Explanation

Four complete subgraphs with 3 nodes can be formed. These are: $(1, 2, 5)$, $(2, 4, 5)$, $(3, 4, 5)$, $(1, 3, 5)$