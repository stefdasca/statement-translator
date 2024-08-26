## Task

An tree with $N$ nodes, numbered from $1$ to $N$, is given. The root of the tree is node $1$. In node $P$ there is a blue ball. In each of the other nodes, there is either a red ball or no ball at all. The goal is to clear all nodes on the path from node $P$ to the root of the tree. More precisely, some red balls must be moved such that in every node on the path from node $P$ to node $1$ (except for node $P$) there is no ball. A move consists of taking a red ball from a node $x$ and placing it in a node $y$ which is a child of $x$, provided that node $y$ is empty (i.e., does not contain any ball, be it red or blue). The blue ball cannot be moved from node $P$. Determine the minimum number of moves necessary so that none of the nodes on the path from node $P$ to node $1$ contains a red ball.

## Input data

The first line of the file `bile7.in` contains the integers $N$, $P$, and $K$. $K$ represents the total number of red balls present in the nodes of the tree. The next $N$ lines describe the structure of the tree: the $i$-th of these lines contains the number $nfii(i)$, followed by $nfii(i)$ numbers $f_1, \dots, f_{nfii(i)}$, meaning that nodes $f_1, \dots, f_{nfii(i)}$ are the children of node $i$. The last line contains $K$ integers, representing the numbers of the nodes in which there is one red ball. All numbers on the same line are separated by a space.

## Output data

In the output file `bile7.out` print the required minimum number of moves. If there is no sequence of moves that meets the problem's requirements, print the number $-1$.

## Constraints

$1 \leq N \leq 5000$ 

$1 \leq P \leq N$ 

$1 \leq K \leq N-1$ 

## Example

`bile7.in` 
```
8 5 3
1 3 1 7 2
2 4 2 5 6 0 0 1 8 0 2 3 7 2
```

`bile7.out`
```
2
```

