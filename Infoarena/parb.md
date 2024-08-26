# Parb

We are given a tree with $N$ nodes. Each node contains a character from '$a$' to '$z$'. Let the function $Parb(x,y)$ return the string of characters formed on the path from node $x$ to node $y$. Node $x$ must be an ancestor of node $y$. Determine 2 nodes $x$ and $y$ such that the string returned by the function $Parb(x,y)$ is lexicographically maximum.

## Input data

The input file `parb.in` will contain on the first line a natural number $N$. The $2$nd line will contain $N$ characters from '$a$' to '$z$' without spaces between them. Node $i$ contains the $i$-th character from this string. The next $N - 1$ lines will contain $2$ numbers $a$ and $b$ each, representing that there is an edge between node $a$ and node $b$. 

## Output data

The output file `parb.out` will contain on one line a string representing $Parb(x,y)$. 

## Constraints and clarifications

$1 \leq N \leq 500\ 000$

Node $1$ is the root of the tree

A string $(x _1 ,x _2 \dots x _N )$ is lexicographically smaller than another string $(y _1 ,y _2 \dots y _M )$ if there exists a position $p$ such that $x _p < y _p$ and $x _1 = y _1$, $x _2 = y _2 \dots x _{p-1} = y _{p-1}$ 

or $N < M$ and $x _1 = y _1$, $x _2 = y _2 \dots x _N = y _N$ 

## Example

`parb.in` 
```
5
zabac
1 2
2 3
1 4
4 5
```

`parb.out`
```
zac
```
