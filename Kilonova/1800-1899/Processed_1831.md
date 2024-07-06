A binary tree is a rooted tree in which each node has at most $2$ children. A Binary Search Tree (**B**inary **S**earch **T**ree) is a binary tree in which each node is associated with a value, and the value of a node is strictly greater than all the values in its left subtree and strictly less than all the values in its right subtree. An example of a binary search tree is shown on the left below, while an incorrect one is shown on the right (since $9$ is in the left subtree of $5$ and $3$).

~[countbst.png]

# Task
Given the natural numbers $N$, $K$ and an array $A_1, A_2, ..., A_K$ with all elements being distinct non-zero natural numbers less than or equal to $N$, you are asked to count how many binary search trees exist with $N$ nodes having node values $1, 2, ..., N$ (in any valid order), such that the array $A_1, A_2, ..., A_K$ forms a chain in the tree **in this order**. For example, for $N=8$, $K=5$, $A=(6, 7, 5, 3, 4)$, the tree on the left above is a valid one.

# Input data
The input file `countbst.in` will contain on the first line a natural number $T$ (number of tests), followed by $T$ tests. Each test will be described by two lines:
* The first line will contain two natural numbers $N$ and $K$ separated by a space.
* The second line will contain the $K$ distinct non-zero natural numbers $A_1, A_2, ..., A_K$ separated and followed by a space.

# Output data
The output file `countbst.out` will contain the answers for each of the $T$ tests, one per line: the number of binary search trees that contain the array of $K$ numbers as a chain, printed modulo $1\ 000\ 000\ 007$ in the order of the tests in the input file.

# Constraints and clarifications
* $N \leq 3\ 000\ 000$
* $\sum K \leq 200\ 000$
* $T \leq 200\ 000$

## Subtask 0 (3 points)
* $N \leq 12$
* $K \leq N$
* $T \leq 10$

## Subtask 1 (4 points)
* $N \leq 200$
* $K \leq N$
* $T \leq 10$

## Subtask 2 (7 points)
* $N \leq 2\ 000$
* $K \leq N$
* $T \leq 10$

## Subtask 3 (5 points)
* $N \leq 50$
* $\sum K \leq 2\ 000$
* $T \leq 2\ 000$

## Subtask 4 (6 points)
* $N \leq 200$
* $\sum K \leq 2\ 000$
* $T \leq 2\ 000$

## Subtask 5 (7 points)
* $N \leq 2\ 000$
* $\sum K \leq 2\ 000$
* $T \leq 2\ 000$

## Subtask 6 (8 points)
* $N \leq 500\ 000$
* $\sum K \leq 2\ 000$
* $T \leq 2\ 000$

## Subtask 7 (9 points)
* $N \leq 2\ 000$

## Subtask 8 (50 points)
* $N \leq 500\ 000$

## Subtask 9 (1 point)
* Without additional constraints

# Example
`countbst.in`
```
2
10 3
2 7 5
10 5
1 7 4 6 2
```
`countbst.out`
```
84
0
```

Explanations
---
For the first test, we have $84$ binary search trees with nodes $1, 2, ..., 10$ that contain the chain $(2, 7, 5)$.
For the second test, there is no valid binary search tree.