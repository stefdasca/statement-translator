## Tree

Given a tree with $N$ nodes, the following operations can be performed:
- Add an edge between two nodes
- Delete an edge between two nodes

We need to determine the minimum number of operations required to transform the tree into a cycle.

## Input data

The input file `tree.in` contains the following:
- The first line contains $N$, the number of nodes in the tree.
- The second line contains $N$ natural numbers. The $i$-th number on this line represents the parent of node $i$ in the tree. If this number is $0$, then the corresponding node is considered the root.

## Output data

The output file `tree.out` will contain the minimum number of operations required to achieve the desired transformation.

## Constraints and clarifications

$1 \leq N \leq 200\ 000$

## Example

`tree.in` 
```
3 
0 1 1
```

`tree.out` 
```
1
```

## Explanation

An edge will be added between nodes $2$ and $3$, which will result in a cycle.