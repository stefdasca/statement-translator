# Task

For any tree with $N$ nodes, the nodes are labeled with numbers from $1$ to $N$ as follows: the nodes are considered ordered by levels starting with the root which has level $1$, and on the same level, the nodes are ordered from left to right. For two nodes on different levels, the node on the lower level will have a smaller label. For two nodes on the same level, the node further to the left has a smaller label.

All trees with $N$ nodes are considered, labeled according to the presented rule, and the parent array is formed for each (it is known that any node except the root has a parent node). For the root, by convention, we consider that it has a parent $0$.

The trees are sorted based on the lexicographical order of the parent arrays. The task is to display the parent array of the tree situated in the specified position after sorting the trees.

# Input data

The first line of the file `arbsort.in` contains a natural number $N$, representing the number of nodes in the considered trees. The second line contains a number $P$ representing the position of the required tree after sorting.

# Output data

The file `arbsort.out` will contain a single line on which there will be $N$ numbers representing the parent array for the required tree.

# Constraints and clarifications

* $1 \leq N \leq 200$
* $1 \leq P \leq$ the number of trees labeled with $N$ nodes.

# Example

`arbsort.in`
```
4
3
```

`arbsort.out`
```
0 1 1 3
```

