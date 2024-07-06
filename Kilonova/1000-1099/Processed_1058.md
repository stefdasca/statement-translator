A rectangular yard with length $N$ and width $M$ (we will denote $N$ rows and $M$ columns) is paved with square tiles of size $1$. The tiles have two colors, they are either white or black (we will encode the white tiles with $0$ and the black tiles with $1$). The black tiles are made of a material much more resistant than the white tiles, and Ionel would like to pitch a tent of maximum area under which there are only black tiles. He also knows that there are only rectangular and square tents of any size. For technical reasons, Ionel can only perform the following operations with the tiles in the yard:

* swap any number of tiles on the same row;
* swap any number of times an entire row with another entire row;

# Task

Write a program that solves the following two tasks:
1. Display the maximum number of black tiles that could be obtained on a column after reordering;
2. Display the maximum area of the tent that can be placed only on black tiles.

# Input data

The input file `cort.in` contains on the first line a natural number $C$ representing the task from the problem to be solved ($1$ or $2$). The second line of the file contains two natural numbers $N$ and $M$, representing the length and the width of the yard. On each of the next $N$ lines, there are $M$ values of $0$ or $1$, indicating the color of the tile at that position.

# Output data

If $C = 1$, the output file `cort.out` will contain a number representing the answer to task $1$.  
If $C = 2$, the output file `cort.out` will contain a number representing the answer to task $2$.

# Constraints and clarifications

* $1 \leq N \leq M \leq 1 \ 000$
* There is at least one black tile
* Correctly solving task $1$ awards $25$ points; correctly solving task $2$ awards $75$ points.

# Example 1

`cort.in`
```
1
6 5
1 0 1 0 1
1 1 1 1 0
1 0 0 0 0
0 0 0 0 0
0 1 1 1 0
0 0 0 0 0
```

`cort.out`
```
4
```

## Explanation

For the first example, the task is $1$. The tiles can be rearranged in the following way:

$ \begin{pmatrix} 1 & 1 & 1 & 0 & 0 \\ 1 & 1 & 1 & 1 & 0 \\ 1 & 0 & 0 & 0 & 0 \\ 1 & 1 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{pmatrix}$

On column $1$ there are $4$ black tiles.

# Example 2

`cort.in`
```
2
6 5
1 0 1 0 1
1 1 1 1 0
1 0 0 0 0
0 0 0 0 0
0 1 1 1 1
0 0 0 0 0
```

`cort.out`
```
9
```

## Explanation

For the second example, the task is $2$. The tiles can be rearranged in the following way:

$ \begin{pmatrix} 1 & 1 & 1 & 1 & 0 \\ 1 & 1 & 1 & 1 & 0 \\ 1 & 1 & 1 & 0 & 0 \\ 1 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{pmatrix}$

An area of $9$ square units is formed.