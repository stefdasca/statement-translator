## Aimin

Consider the $N$ leaves of a strict binary tree (each internal node of the tree has exactly 2 children, the left child and the right child), numbered from 1 to $N$ (in the order they appear from left to right in a left-root-right traversal of the tree). A ribbon of length $L_i$ was attached to each leaf $i$. The level of each node in the tree is equal to the length of the path from the root of the tree to that node (the level of the root is 0). The height of a leaf $i$ is equal to its level plus $L_i$. The height of the entire tree is equal to the maximum height among its $N$ leaves. Determine the minimum possible height of the tree.

## Task

## Input data

The input file `aimin.in` contains on the first line the integer number $N$. The second line contains $N$ integers, separated by spaces, representing the values $L_i$, in order, from 1 to $N$. 

## Output data

In the output file `aimin.out` you will print the minimum possible height of the tree. 

## Constraints and clarifications

$1 \leq N \leq 100\,000$

$1 \leq L_i \leq 100\,000\,000$

## Example

`aimin.in`

```
5 
3 1 2 4 2
```

`aimin.out`

```
6
```