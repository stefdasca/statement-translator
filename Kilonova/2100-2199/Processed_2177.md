
A tree is given with $n$ nodes numbered from $1$ to $n$ and the root is node $1$, in which each node has a distinct value associated with it. An infinite number of paths are taken on this tree: starting from the root node and at each step, for the current node, the child with the greatest value is chosen until a leaf is reached. Once a node is traversed, its value decreases by one unit. If at some point there are two children with the same value, the one that initially had the greater value is chosen. Moreover, it is guaranteed that the height of the tree is less than or equal to $20$.

# Task
Answer questions of the form $(x,y)$ with the following meaning: after how many such paths will node $x$ be traversed exactly $y$ times? (that is, the path in which node $x$ was accessed for the $y^{th}$ time)

# Input data

The input file `arb.in` contains on the first line two natural numbers $n$ and $q$ separated by a space, representing the number of nodes in the tree and the number of questions, in that order. The second line of the file contains $n-1$ natural numbers separated by spaces. The $i^{th}$ number on this line represents the parent of the node with index $i+1$. The third line contains $n$ natural numbers separated by spaces representing the values of the $n$ nodes in increasing order of indices. The following $q$ lines contain two natural numbers $x$ and $y$ separated by a space: the node of interest and the number of accesses to it.

# Output data

The output file `arb.out` will contain $q$ lines representing the answer to each question.

# Constraints and clarifications

* $2 \leq n , q \leq 100\ 000$
* The values in the nodes are natural numbers less than or equal to $1\ 000\ 000\ 000$.
* For each question the answer is represented on 32-bit signed integers.
* **The height of the tree is less than or equal to $20$**.

# Example

`arb.in`
```
5 3
1 1 3 3
10 7 5 2 3
4 2
5 3
3 1
```

`arb.out`
```
12
10
4
```
