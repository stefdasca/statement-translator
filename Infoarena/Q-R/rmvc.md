## Task

We conclude this year's MVC trilogy with the following problem: Given a graph $G$ with $N$ nodes and $M$ edges. We call a node cover of the graph a set of nodes $A$ with the property that every edge in the graph has at least one of its endpoints in the set $A$. In this problem, you need to find a node cover of the graph $G$ with the minimum cardinality. It is guaranteed that for the given graphs in the input, there exists a node cover of size at most 18.

## Input data

The input file `rmvc.in` contains on its first line the numbers $N$ and $M$ signifying the number of nodes and the number of edges of the graph. The following $M$ edges contain each a pair $x$ $y$ signifying that there is an edge between node $x$ and node $y$. It is guaranteed that there are no edges with both endpoints in the same node, but there can be double edges.

## Output data

The first line of the output file `rmvc.out` will contain the size of the found cover. The second line will contain the nodes in the cover displayed in any order. Any solution with minimal cardinality is accepted.

## Constraints

$1 \leq N \leq 90$  
$1 \leq M \leq 320$

## Example

`rmvc.in`
```
5 6
1 2
1 3
1 4
2 3
2 4
3 4
```

`rmvc.out`
```
3
3 4 2
```