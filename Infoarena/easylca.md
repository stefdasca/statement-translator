## Task

Given an infinite complete binary tree (each node has exactly 2 children) in which the nodes are numbered by level from left to right, with the root numbered $1$, determine the lowest common ancestor for each pair of nodes given $Q$ pairs of nodes.

## Input data

The input file `easylca.in` contains on the first line a natural number $Q$, the number of queries. The following $Q$ lines each contain two integers $X$ and $Y$ representing a pair of nodes.

## Output data

The output file `easylca.out` will contain, for each pair $(X, Y)$, the lowest common ancestor of nodes $X$ and $Y$.

## Constraints

$1 \leq Q \leq 20000$

$1 \leq X, Y \leq 10^{100}$

## Example

`easylca.in`
```
3
2 9
7 8
30 25
```

`easylca.out`
```
2
1
3
```