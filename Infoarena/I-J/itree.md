## Itree

Given a set of intervals on the OX axis. We consider that two intervals intersect if and only if they have more than one point in common (for example, intervals $[ 1, 5 ]$ and $[ 3, 10 ]$ intersect, but $[ 1, 2 ]$ and $[ 2, 3 ]$ do not intersect). The graph associated with this set of intervals is the graph in which a node is associated with each interval and an edge between the nodes corresponding to each pair of intersecting intervals. A graph $G$ is called an interval graph if there exists at least one set of intervals whose associated graph is isomorphic with $G$. A tree (a connected acyclic graph with $N$ vertices and $N-1$ edges) is called an interval tree if it is also an interval graph.

## Task

Given a tree, determine if it is an interval tree.

## Input data

The file `itree.in` will contain the first line an integer $T$ representing the number of tests in the file. The description of $T$ trees follows. For each tree, the first line will contain a number $N$ - the number of nodes of the tree. The next $N-1$ lines contain a pair of numbers $A$ $B$ , indicating that there is an edge between nodes $A$ and $B$.

## Output data

The file `itree.out` will contain $T$ lines. For each tree in the input file, print $YES$ if it is an interval tree, otherwise print $NO$.

## Constraints

$1 \leq N \leq 100 000$

## Example

`itree.in`

```
3
3
1 2
2 3
1
4
1 2
1 3
3 4
```

`itree.out`

```
YES
YES
YES
```