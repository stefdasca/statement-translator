# J-Tree

The J-tree is an infinite tree with the following properties:
- On level $1$ of the tree, there is a single node (the root).
- Each node on level $i$ has exactly $i$ children.
- The edges of the tree are labeled with consecutive integers starting from the first level of the tree, going from left to right.
- All nodes, except for the root, are labeled with integers equal to the sum of the edges on the path from the root to that node.

Below are the first levels of such a tree.

## Task

Given a natural number $X$, you are required to determine if there exists a node labeled with the value $X$ and display the labels of the edges on the path from the root to that node.

## Input Data

The input file `jarbore.in` will contain multiple tests. The first line contains $T$, the number of tests. The following $T$ lines contain one number $X$ each.

## Output Data

The output file `jarbore.out` will contain $T$ lines. Each line will contain the labels of the edges on the path from the root to the node with the required property or $-1$ if such a node does not exist.

## Constraints

$1 \leq X \leq 10^{18}$

$1 \leq T \leq 1000$

## Example

`jarbore.in`
```
7
100
1
2
12
17
89
666
```

`jarbore.out`
```
-1
1
-1
1 3 8
1 2 4 10
1 2 5 16
1 3 7 22 97 536
```