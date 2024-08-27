# Christmas Trees

This year, the Christmas trees have the shape of binary trees. A tree is identified by the number of nodes $N$ and $N-1$ edges, which can be of two types: $x \ y \ 0$ meaning that $y$ is the left child of $x$ $x \ y \ 1$ meaning that $y$ is the right child of $x$ Two trees are similar if, by changing the labeling of one of them, the edges match exactly with those of the other. For example: the tree $1 \ 2 \ 0$, $1 \ 3 \ 1$, $2 \ 4 \ 0$ is not similar to the tree $1 \ 2 \ 1$, $1 \ 3 \ 0$, $2 \ 4 \ 1$ but it is similar to $1 \ 3 \ 0$, $1 \ 2 \ 1$, $3 \ 4 \ 0$. We are given $T$ such trees containing at most $10$ nodes. For each tree $i$, print the number of trees from the first $i-1$ that are similar to it.

## Input data

The input file `brazi.in` contains on the first line a natural number $T$, the number of trees. Each tree is described in $N$ lines. The first line contains $N$, the number of nodes. The following $N-1$ lines contain $3$ numbers $x \ y \ 0$ or $x \ y \ 1$ representing an edge of the tree.

## Output data

The output file `brazi.out` will contain $T$ lines. On line $i$ it will print the number of trees from the first $i-1$ that are similar to tree $i$.

## Constraints

$1 \leq T \leq 100000$  
$1 \leq N \leq 10$  
$1 \leq x, y \leq N$  

## Example

`brazi.in`  
```
3
4
1 2 0
1 3 1
2 4 0
4
1 2 1
1 3 0
2 4 1
4
1 3 0
1 2 1
3 4 0
```

`brazi.out`  
```
0
0
1
```