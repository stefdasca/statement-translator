Sure, here is the translated text along with the corrections as requested:

---

A rooted tree is formed from a set of nodes, among which one is called the root. Each node has an ordered list of child nodes, and each node different from the root is the child of exactly one other node called the parent. The root has no parent.  
The subtree of a node $X$ is a rooted tree obtained by removing any node that is not a direct or indirect child of node $X$ and considering node $X$ as the root.  
Let $A$, $B$ be two rooted trees with roots $r_A$ and respectively $r_B$. Let $a_1 \\ a_2 \\ a_3 \\dots a_k$ be the ordered list of children of $r_A$, $b_1 \\ b_2 \\ b_3 \\dots b_p$ be the ordered list of children of $r_B$. We say that the trees $A$, $B$ are equal if $p=k$ and for any $1 \\leq i \\leq k$ the subtrees with roots $a_i$ and $b_i$ are equal.  
We say that tree $A$ appears in tree $B$ if there exists a node $n_B$ in $B$ such that the subtree with root $n_B$ is equal to tree $A$.  
Gigel has a business involving a set of $T$ rooted trees (called models) $A_1, A_2, \\dots, A_T$. Gigel sells only rooted trees with $N$ nodes in which none of the model trees appear.

# Task

Write a program that calculates how many distinct rooted trees with $N$ nodes Gigel can sell.

# Input data

The input file `arbnr.in` contains on the first line the natural numbers $N$ and $T$ representing the number of nodes in the trees sold by Gigel and respectively the number of model trees. Subsequently, follow $T$ data blocks, each block representing the description of a model tree. The block describing a model tree contains on the first line a natural number $M$ representing the number of nodes in the tree. The second line contains $M-1$ natural numbers separated by spaces. The $i$-th number on the line is the parent node of node $i+1$. The root is the node numbered $1$. The order of the children is considered in the ascending order of their node numbers.

# Output data

The output file `arbnr.out` will contain a single line with a natural number representing the number of distinct rooted trees with $N$ nodes in which none of the model trees appear **modulo $9 \ 907$**.

# Constraints and clarifications

* $1 \leq N \leq 10 \ 000$
* $0 \leq T \leq 40$
* $2 \leq M \leq 10 \ 000$
* $30\\\%$ of the score is awarded for $N,M \leq 100$ and $T \leq 10$
* $65\\\%$ of the score is awarded for $M \leq 500$

# Example

`arbnr.in`
```
4 2
3
1 2
3
1 1
```

`arbnr.out`
```
3
