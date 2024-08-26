
Euler

The tests for this problem are not well constructed enough to accurately differentiate between inefficient or incorrect solutions. Click here if you want to help us improve the quality of the tests for this problem! Given a rooted general tree. The tree has $N$ nodes numbered from $1$ to $N$. An Euler traversal of this tree is done as follows: print the root of the current tree and for each child of the root display the Euler traversal of the respective subtree, and then print the root again. For example, for a tree with $7$ nodes, with the root in node $5$ and the list of edges $(5, 3)$, $(5, 7)$, $(3, 6)$, $(3, 1)$, $(3, 2)$, $(7, 4)$, the Euler traversal is $5, 3, 6, 3, 1, 3, 2, 3, 5, 7, 4, 7, 5$.

## Task

The problem asks, given a number $N$ and a sequence of numbers, to determine whether the sequence represents a correct Euler traversal of a tree with $N$ nodes and, if so, to reconstruct the tree.

## Input data

The input file `euler.in` will contain on the first line the number $N$, and on the second line a sequence of natural numbers between $1$ and $N$. The number of numbers is unknown.

## Output data

The output file `euler.out` will contain on the first line one of the messages $DA$ or $NU$, depending on whether the sequence of numbers is an Euler sequence of a tree with $N$ nodes or not. If the answer is $DA$, the second line will contain $N$ natural numbers, where the $i$-th number will be the parent of node $i$. If node $i$ is the root, $0$ will be printed in the corresponding position.

## Constraints and clarifications

$1 \leq N \leq 262144$

$ The$ $number$ $of$ $given$ $numbers$ $does$ $not$ $exceed$ $524288$

## Example

`euler.in` 

```
7
5 3 6 3 1 3 2 3 5 7 4 7 5
```

`euler.out` 

```
DA
3 3 5 7 0 3 5