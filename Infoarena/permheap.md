## Task

We call a heap a binary tree in which each node has associated information greater than the information associated with any of its children. Therefore, we can represent a heap through an array in which elements are stored starting from position $1$, and the children of the node at position $i$ are the nodes at positions $2*i$ and $2*i+1$ (we imagine the nodes at the same level placed from left to right, in increasing order of their positions). All levels of the tree are complete (each node has exactly $2$ children), except possibly the last level, which is complete from the left (i.e., the leaves are filled in smaller positions first). Determine how many permutations of the set $\{1, 2, \dots, n\}$ have a heap structure.

## Input data

The file `permheap.in` contains one natural number $n$ on the first line.

## Output data

The file `permheap.out` contains one natural number on the first line representing the required value, modulo $666013$.

## Constraints and clarifications

$1 \leq n \leq 200000$

## Example

`permheap.in`
```
4
```

`permheap.out`
```
3
```

## Explanation

$4 \ 2 \ 3 \ 1$, 
$4 \ 3 \ 1 \ 2$, 
$4 \ 3 \ 2 \ 1$