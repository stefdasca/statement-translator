# The Game of *betasah*

The game of **betasah** is played using only pieces similar to the queens from classic chess, also called *queens*. The playing surface has a triangular shape and consists of $N \cdot (N+1) / 2$ identical squares arranged on $N$ rows and $N$ columns. The rows are numbered from top to bottom, from $1$ to $N$. The columns are numbered from left to right, from $1$ to $N$. The first row contains a single square, the second row contains two adjacent squares, $\dots$, the $N$-th row contains $N$ adjacent squares, as in the playing surfaces with $N=6$ in the figures below. Out of the $N \cdot (N+1) / 2$ squares, $K$ are gray, and the rest are white. The position of each square on the playing surface is given by the row and column in which it is located.

~[betasah.png]

On the playing surface, there are $D$ queens placed in $D$ distinct white squares, occupying them. A square **can be occupied by only one queen**, and a gray square **cannot be occupied by any queen**. The position of a queen on the playing surface is given by the position of the white square in which the queen is placed.
Queens can access any unoccupied white square located in the directions: vertical, horizontal, or diagonal, numbered from $1$ to $8$ in **figure $b$)**. Access in a direction is made by moving from white square to white square (only unoccupied white squares) until encountering a gray square or a white square occupied by another queen, or until the end of the playing surface.
We call **accessible square** any unoccupied white square (on the playing surface) that could be accessed by at least one of the $D$ queens.
For example, for the playing surface in **figure $c$)** the number of accessible squares (marked with $X$) on the surface is $11$; for the playing surface with $N=6, D=3$ and $K=4$ in **figure $d$)**, the number of accessible squares on the surface is $13$. In figure $e$) the accessible squares for each queen on the playing surface of figure $d$) are marked with $X$.

~[betasah2.png]

# Task

Write a program that reads the natural numbers $N \ D \ K$, the positions of the queens and gray squares on the playing surface and determines:

* the maximum number $M$ of white squares contained in a row of the playing surface;
* the number $P$ of accessible squares on the playing surface.

# Input data

The input file `betasah.in` contains:

* the first line contains the three natural numbers $N \ D \ K$, separated by a space, with the specified meaning;
* on line $i+1$, two non-zero natural numbers $x_i \ y_i$, separated by a space, representing the position of queen $i$ on the playing surface (row $x_i$ and column $y_i$), for $i = 1,2,3,\dots,D$;
* on line $D+1+j$, two non-zero natural numbers $z_j \ t_j$, separated by a single space, representing the position of gray square $j$ on the playing surface (row $z_j$ and column $t_j$), for $j = 1, 2, 3, \dots, K$.

# Output data

The output file `betasah.out` will contain on the first line the natural number $M$ and on the second line the natural number $P$, with the specified meaning. To obtain partial scores, this format must be respected.

# Constraints and clarifications

* $2 \leq N \leq 1\ 000$;
* $1 \leq D \leq 100$;
* $1 \leq K \leq 50$;
* $D + K \leq N \cdot (N+1) / 2$;
* $1 \leq y_i \leq x_i \leq N$;
* $1 \leq t_j \leq z_j \leq N$;
* for the correct solution of requirement $1$), $20\%$ of the score is awarded, while for the correct solution of requirement $2$), $80\%$ of the score is awarded.

# Example

`betasah.in`
```
6 3 4
3 2
5 2
5 4
3 1
4 3
6 4
1 1
```

`betasah.out`
```
5
13
```

## Explanation

~[betasah3.png|align=right]

$N=6, D=3, K=4$.  
Rows $5$ and $6$ contain the maximum number $M=5$ of white squares.  
The number of accessible squares on the playing surface is $P=13$.  
In the adjacent drawing corresponding to the given surface, the $13$ accessible squares are marked with $X$.  
Thus, on the first line of the `betasah.out` file, the number $5$ will be written, and on the second line of the file, the number $13$ will be written.