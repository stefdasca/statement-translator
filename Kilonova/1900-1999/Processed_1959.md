# "Una e să te spargi în figuri, și alta e să spargi figuri"

Nea Puiu loves breaking figures. In this case, the figures he wants to break are trees with $N$ nodes that have a fixed root (a tree represents an undirected, connected, and acyclic graph). Breaking a tree means cutting one of its edges, which causes all nodes that are no longer connected to the tree's root to detach from it.

Before making the cut, Nea Puiu has thoroughly studied the properties of trees and has defined the depth of a subtree as the largest distance between the root of the subtree and one of its leaves.

Because Nea Puiu does not want to leave many traces after his actions, he wants to answer questions in the form: "In how many ways can we cut an edge from the subtree with root in node $x$ so that after the cut, the new depth of the subtree remains the same as before?"

However, Nea Puiu is a professional, so he wonders what would happen if the tree changes between different questions. Therefore, there can be two events that modify the tree: either a specific leaf of the tree is deleted, or a new node is added, connected to one of the already existing nodes in the tree.

# Task
Since Nea Puiu needs to handle gas contributions, you must, given the initial tree and $M$ operations of the forms described above, respond to his questions!

# Input data
The input file `neapuiu.in` contains two natural numbers: $N$, the number of nodes in the tree, and $M$, the number of operations to be conducted.
The next $N - 1$ lines contain the edges of the tree. Each line contains two natural numbers, $x$ and $y$, separated by a space, representing an edge from $x$ to $y$ in the tree.
The next $M$ lines describe the operations. Each line is made up of natural numbers and can have one of the following formats:
* $0 \\ x \\ y$ – node with index $y$ is added as a child of node with index $x$; it is guaranteed that there was no node with index $y$ in the tree before this moment.
* $1 \\ x$ – node with index $x$ is deleted – it is guaranteed that node $x$ is a leaf in the current tree.
* $2 \\ x$ – respond to the question: "In how many ways can we cut an edge from the subtree with root in node $x$ so that after the cut, the new depth of the subtree remains the same as before?"

# Output data
The output file `neapuiu.out` must contain the answers to the questions from the input file, one per line.

# Constraints and clarifications
* $1 \leq N, M \leq 100 \ 000$;
* The root of the tree is node 1; it is guaranteed that this node will not be deleted;
* It is guaranteed that once a node is deleted from the tree, there will never be another node added with the same index;
* It is guaranteed that there will not be two nodes with the same index in the tree.

# Example

`neapuiu.in`
```
9 14 
1 2
1 6 
2 3 
2 4 
4 5 
6 7 
6 8 
6 9 
2 1 
2 2 
0 3 10 
2 2 
2 6 
1 8 
2 6 
0 9 11 
0 11 12 
2 6 
0 7 13 
1 12 
2 6 
2 5
```

`neapuiu.out`
```
5 
1 
4 
3 
2 
1 
4 
0
