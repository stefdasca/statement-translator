Here is the translated file:

A rooted tree is a structure that contains a special node called the root of the tree and $A_1, A_2, ..., A_n$ (where $n \geq 0$) rooted trees (called subtrees of the root). The root node of each tree $A_i$ is called a child of the root of the tree and is connected by an edge to the root of the tree.
Two rooted trees are identical if the roots of the two have the same number of subtrees and these are identical (more precisely, for any $i=1, 2, ..., n$ the $i$-th subtree of the first is identical to the $i$-th subtree of the second).
A termite can "carve" a tree by acting as follows:
1) the termite starts from the root of the tree;
2) at every moment (in any node it is), the termite can perform one of the following operations:
	* stays in the node and eats the rightmost edge, thus eliminating the rightmost child and the corresponding subtree (these fall and will be eaten by other lazy termites);
	* advances on the right edge, towards the remaining rightmost child of the node it is in;
	* stops.

Two friendly termites choose two trees and carve them as described until they obtain two identical trees.
The similarity between two trees is equal to the maximum number of nodes that remain in each of the two identical trees obtained by carving.

# Task

Given two trees (a model tree and a tree to evaluate), calculate for each node of the tree to evaluate the similarity between the subtree rooted in that node and the given model tree.

# Input data

The first line of the input file `arbfind.in` contains a natural number $N$ representing the number of nodes in the model tree, the nodes being numbered from $1$ to $N$. Lines $2..N+1$ will contain the description of the model tree. More precisely, on line $i$ there will be a natural number $F_{i-1}$ representing the number of direct children of node $i-1$, followed by $F_{i-1}$ natural numbers between $1$ and $N$, representing the children of node $i-1$ from left to right.
Line $N+2$ will contain a natural number $M$ representing the number of nodes in the tree to evaluate. Lines $N+3..N+M+2$ will contain the description of the tree to evaluate, in a way analogous to the description of the model tree.

# Output data

The output file `arbfind.out` will contain $M$ lines. Each line $i$ will contain the similarity of the subtree rooted in node $i$ with respect to the model tree.

# Constraints and clarifications

* The root of the trees is always node $1$.
* $1 \leq M, N \leq 16\ 000$

# Example

`arbfind.in`
```
4
2 2 3
1 4
0
0
9
2 2 3
2 4 5
2 6 7
1 8
0
0
1 9
0
0
```

`arbfind.out`
```
3
4
2
2
1
1
2
1
1
```

## Explanation

Model tree
~[img1.png]

Evaluated tree
~[img2.png]

For example, for node $1$ in the model tree, the subtrees rooted at $3, 5$, and $8$ were removed in order. From the model tree, the subtree rooted at $3$ is removed.

I’ve double-checked the translation to ensure that it meets the rules and proper grammar/syntax of the English language.