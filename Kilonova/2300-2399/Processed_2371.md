Prâslea cel Voinic found the garden with apple trees bearing golden apples, but he now has trouble guarding them. He stayed awake for years until he decided to build a fence around them so he could sleep peacefully.

The garden has the shape of a square with a side length of $N$ meters. Prâslea divided the garden into $N \times N$ squares of $1 m^{2}$, with the squares arranged in $N$ rows (numbered from $1$ to $N$) and $N$ columns (numbered from $1$ to $N$). Each apple is located in one of these squares.

To build the fence, Prâslea decided to select a series of squares in which the first and last square, as well as any $2$ consecutive squares in the series, share at least one common point. A square can be chosen in the series once or multiple times. In each square in the series, Prâslea will place a giant post. The fence formed by these posts will divide the garden into two zones (inside and outside). All apple trees must be inside. A square is considered inside if there is no path from a square on the edge of the garden (row $1$, column $1$, row $n$ or column $n$) to that square. A path is a series of squares such that any two consecutive squares in the path share a side, with the squares on the path being empty (squares that do not contain posts).

Placing a post in a certain square has a certain cost. If a square appears multiple times in Prâslea's chosen series, then the cost will be added as many times to the total cost.

# Task
Write a program to determine the total minimum cost of building the fence according to the conditions in the statement.

# Input data
The first line of the input file `gard.in` contains the natural number $N$ representing the size of the garden. The next $N$ lines contain $N$ numbers separated by a space. If the $j$-th number on the $i$-th line of the file is -$1$, then the square in the garden located on row $i-1$ and column $j$ contains an apple tree; otherwise, that number represents the cost of placing a post in the square on row $i-1$ and column $j$.

# Output data
The output file `gard.out` will contain a single line that contains a natural number representing the total minimum cost of placing the posts.

# Constraints and clarifications

* $2 < N < 36$
* Number of apple trees: $0 < apple\ count < 6$
* The cost of placing a post is a natural number greater than or equal to $0$ and less than $6\ 666$.
* There will be no apple trees on the edge of the garden (row $1$, column $1$, row $N$ or column $N$).
* Obviously, a post cannot be placed in a square that contains an apple tree.

# Example

`gard.in`
```
5
3 0 10 10 10
10 1 10 0 10
0 -1 4 -1 0
10 0 10 0 0
10 10 10 10 0
```

`gard.out`
```
9
```

## Explanation

The chosen series of squares for placing the posts is as follows: 
~[img1.png]
As you can see, the square with cost $4$ between the two apple trees was chosen twice.