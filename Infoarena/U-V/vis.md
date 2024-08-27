# Dream

Ojilă is so obsessed with preparing for OJI that he even solves problems in his dreams. He is dreaming that he finds himself at position $(1,1)$ of a square matrix where rows and columns are numbered from $1$ to $N$. In the matrix, there are two special positions $(L1,C1)$ and $(L2,C2)$. Ojilă can move in four directions (north, south, east, west) without leaving the matrix and only on cells marked with $0$. However, if he passes through the position $(L1,C1)$, he can further move on cells that have values less than or equal to a given number $K1$, and if he passes through the position $(L2,C2)$, he can then move on cells that have values greater than or equal to a given number $K2$. Of course, if he has passed through both special positions, he can move on all values less than or equal to $K1$ or greater than or equal to $K2$. Determine the minimum number of steps needed for Ojilă to reach the position $(N,N)$ in the matrix as if in a dream.

## Input data

The input file `vis.in` contains on its first line the natural numbers $N$, $K1$, $K2$, $L1$, $C1$, $L2$, $C2$ separated by spaces. The next $N$ lines contain $N$ natural numbers separated by spaces representing each row of the matrix.

## Output data

The output file `vis.out` will contain a single natural number representing the minimum length of the path from position $(1,1)$ to $(N,N)$.

## Constraints

$3 \leq N \leq 1000$

The elements of the array are natural numbers less than or equal to $30\ 000$.

The positions $(1,1)$, $(N,N)$, $(L1, C1)$ and $(L2,C2)$ will always be marked with $0$.

It is possible to pass through a position multiple times.

For all test cases, there will exist a path from $(1,1)$ to $(N,N)$.

## Example

`vis.in`
```
5 2 5 3 1 1 5 
0 3 0 0 0 
0 0 7 0 0 
0 5 2 0 0 
1 6 0 9 0
0 0 0 8 0
```

`vis.out`
```
13
```

## Explanation

$K1=2$, $K2=5$, $(L1, C1)=(3,1)$ and $(L2,C2)=(1,5)$. The path of length $13$ is $(1,1) (2,1) (3,1) (4,1) (5,1) (5,2) (5,3) (4,3) (3,3) (3,4) (3,5) (4,5) (5,5)$