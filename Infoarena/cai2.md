## Task

Tired of drawing on paper, Lunasorab started playing with knights on a chessboard of size $N$ by $M$. This board is special in the sense that there are certain cells colored red. Now, he wonders in how many ways he can place knights (that follow the movement rules of knights in chess) on this board so that each red-colored cell is attacked by an even number of knights. Because this number can be very large, he asks you to display it modulo $666013$.

## Input data

The input file `cai2.in` will contain the first line with $T$, the number of tests. Each test will contain $N$ and $M$ on the first line, followed by $N$ lines, each containing $M$ numbers. The $j$-th number in the $i$-th row (in the group of $N$ rows) will be $1$ if the cell $(i, j)$ in the matrix is colored red, and $0$ otherwise.

## Output data

The output file `cai2.out` will contain $T$ lines, with the $i$-th line containing the number of ways to place knights on the board from test $i$ so that the conditions from the statement are met, modulo $666013$.

## Constraints and clarifications

$1 \leq T \leq 100$  
$1 \leq N \leq 20$  
$1 \leq M \leq 20$  
For each test, both $N$ and $M$ will be chosen uniformly between the given limits  
A knight does not attack its own cell

`cai2.in`

```
2
2 3
1 0 1
1 0 1
5 16
0 1 1 1 1 1 0 1 1 1 0 1 0 1 1 1
1 1 1 1 0 1 0 1 1 1 0 1 1 1 1 1
1 1 1 0 1 0 1 1 1 0 1 1 1 1 0 1
0 1 1 1 0 1 0 1 1 1 0 0 1 0 0 1
1 1 1 0 1 0 1 1 1 0 1 1 1 0 1 1
```

`cai2.out`

```
4
198226
```