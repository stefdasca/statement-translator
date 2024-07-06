```markdown
Andrei is a master of the game of Tetris; he can play for days with his eyes closed and his hands tied behind his back. Therefore, he has decided to move to the next level and play the 3D version of the game. 

The pieces will fall on a flat horizontal surface in the shape of a square, with a side of $M$ cm, called the base. On the base, there is a grid that delimits $M \times M$ squares with a side of $1$ cm, each square being identified by its coordinates (the row and column it is on). 

After some pieces fall on the base, a certain game configuration is obtained, which will be represented as a matrix $B$ with $M$ rows and $M$ columns, $B_{i, j}$ being the height reached by the highest cube placed on the square on row $i$ and column $j$ of the matrix $(1 \leq i,j \leq M)$ - see figure $1$. 

A piece of the game is obtained by gluing cubes with a side of $1$ cm on a flat surface (the base of the piece) - see figure $2$. A piece will also be represented as a matrix $P$ with $N$ rows and $N$ columns, $P_{i, j}$ being the number of cubes placed on the square on row $i$ and column $j$ of the base of the piece $(1 \leq i,j \leq N)$. 

~[tetris.png]

The configuration of the base from figure $1$ will be described by the following matrix:
```
3 2 3 2 3 2
2 1 2 1 2 4
2 1 2 2 2 1
2 1 1 2 1 1
2 1 1 2 1 1
3 1 2 1 2 1
```

The piece from figure $2$ will be described by the following matrix:

```
1 2 1
2 3 2
2 2 2
```

Each square of the base of the piece or the base itself has at least one cube placed on it.
The pieces will fall with the base of the piece facing upwards and cannot be rotated. A piece is positioned on the base as follows: the square $(1,1)$ of the base of the piece aligns with a square $(L,C)$ of the matrix (without the piece exceeding the limits of the base), and the piece falls vertically until a cube of the piece touches a cube of the base. 

We say that a piece is positioned perfectly in a certain position $(L,C)$ if for each square of the base of the piece, the "lowest" cube touches the cube situated at the maximum height on the corresponding square of the base. 

# Task

Given the configuration of the base and a piece, determine the number of positions in which the piece can be positioned perfectly.

# Input data

The input file `tetris.in` contains on the first line the natural number $M$, representing the size of the base. The next $M$ lines contain $M$ natural numbers separated by spaces, representing the matrix that encodes the configuration of the base. On line $M+2$ is the natural number $N$, representing the size of the base of the piece. On the next $N$ lines are $N$ natural numbers separated by spaces, representing the matrix that encodes the piece. 

# Output data

The output file `tetris.out` will contain a single line that will contain the number of positions in which the given piece can be positioned perfectly.

# Constraints and clarifications

* $1 < M < 505$
* $0 < N < 101$
* $N < M$
* $1 \leq M_{i,j} \leq 10 \ 000 (1 \leq i,j \leq M)$
* $1 \leq P_{i,j} \leq 10 \ 000 (1 \leq i,j \leq N)$

# Example

`tetris.in`
```
6
3 2 3 2 3 2
2 1 2 1 2 4
2 1 2 2 2 1
2 1 1 2 1 1
2 1 1 2 1 1
3 1 2 1 2 1
3 
1 2 1
2 3 2
2 2 2
```

`tetris.out`
```
1
```

## Explanation

The piece can be positioned perfectly only at position $(1,3)$.
```