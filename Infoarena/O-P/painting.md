## Task

Given a tree with $N$ nodes, each node having a color. Initially, all nodes have color $1$. On this tree, $M$ operations are performed, each of the type: all nodes in the subtree of node $X$ are colored with color $Y$. It is considered that the root of the tree is node $1$. The color of a node is given by the color of the last operation applied to that node. What is the color of each node after executing all operations?

## Input data

The input file `painting.in` will contain on the first line the numbers $N$ and $M$.  
The next $N - 1$ lines will contain pairs $X Y$, indicating that there is an edge in the tree between the respective nodes.  
The following $M$ lines will contain $2$ numbers each, $X Y$, indicating that the subtree of node $X$ is colored with color $Y$.

## Output data

The output file `painting.out` will contain $N$ numbers, the $i$-th number representing the color of node $i$.

## Constraints and clarifications

$1 \leq N, M \leq 10^5$

$1 \leq$ Color of a node $\leq 10^4$

## Example

`painting.in`
```
7 4
1 2
1 3
2 4
2 5
4 6
3 7
2 7
4 5
3 9
5 4
```

`painting.out`
```
1 7 9 5 4 5 9
```