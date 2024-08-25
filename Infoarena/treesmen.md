## Task

Antonio believes that the final step to winning Antonia’s heart is to show her that he is serious professionally as well. He will impress her with the following problem: Given a tree with $N$ nodes numbered from $1$ to $N$ and root at node $1$. Initially, each node contains the value $0$. There are $M$ operations, which can be of $2$ types:
$0$ $x$ $y$ $p$ $r$: with $x$ being an ancestor of $y$; the nodes on the path $x - y$ increase by the terms of an arithmetic progression with the first term equal to $p$ and ratio $r$. More precisely, node $x$ increases by the value $p$, the next node increases by the value $p + r$, the following node increases by the value $p + 2 * r$, etc.
$1$ $x$: query the current value in node $x$.
To prove his mastery, which he hopes will impress Antonia, Antonio needs to respond to the type $1$ operations in the given order.

## Input data

The input file `treesmen.in` contains on the first line a natural number $N$, representing the number of nodes in the tree.
The second line of the file contains $N - 1$ natural numbers separated by a space. The $i$-th number on this line represents the parent of the node with index $i + 1$.
The next line contains a natural number $M$, representing the number of operations.
The next $M$ lines contain the operations, in the format described in the statement.

## Output data

The output file `treesmen.out` will contain the answers to the type $1$ operations in the order they are received in the input file.

## Constraints and clarifications

$1 \leq N, M \leq 10^5$

$1 \leq p, r \leq 10^3$

$x$ will always be an ancestor of $y$

If Antonio solves this $100$ points problem, Antonia will be impressed and they will live happily ever after!

## Example

`treesmen.in`
```
10
1 1 1 2 2 4 7 8 7 9
0 1 5 3 2
0 2 5 2 3
1 1
1 5
0 4 9 1 3
1 7
0 4 10 2
1 8
1 10
```

`treesmen.out`
```
3
12
4
7
4
```