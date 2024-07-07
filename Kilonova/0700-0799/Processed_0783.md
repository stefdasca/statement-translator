
A rectangular area with height $N$ and width $M$ units needs to be perfectly covered (tiled) using rectangular tiles of dimensions $1 \times P$ or $P \times 1$, where $P$ is a non-zero natural number. The given surface can be viewed as a grid with $N \times M$ unit squares.

A correct tiling of the initial surface is stored in a text file using the following encoding conventions:
- The first line contains the dimensions $N$ and $M$ of the surface;
- A rectangular tile of width $P$ is encoded by the natural number $P$, and a tile of height $P$ is encoded by the integer $-P$;
- We assume that the tile with both dimensions equal to one is encoded with the value $1$;
- On each of the $N$ lines of the encoding, there is a sequence of integers representing the codes of the tiles placed starting from that line, from left to right;
- The code $P$ strictly greater than $1$ for a horizontal tile appears only once on the corresponding line where the tile is located, and the code $-P$ for a vertical tile appears only once, specifically on the first line from which the respective tile is placed downward on a certain column of the surface;
- If on a certain line of the surface there are no such tile codes, then that line in the file contains a single value of $0$.

Using the encoding of a tiling of the initial surface, the image of this tiling can be determined in the form of a two-dimensional array $A$, with $N$ lines and $M$ columns, where $A_{i,j}$ represents the absolute value of the tile code that overlaps the square at line $i$ and column $j$.

# Task
Given the encoding of a correct tiling of the given surface, obtain the image of this tiling (the matrix of values corresponding to the surface encoding).

# Input data
The input file `placare.in` contains the following structure:
- The first line contains the natural values $N$ and $M$, separated by a space, where $N$ is the height of the surface and $M$ is the width of the surface.
- Each of the following $N$ lines contain a sequence of integers, separated by spaces, representing the encoding of the respective line of the tiling.

# Output data
The output file `placare.out` will contain the two-dimensional array representing the image of the tiling, composed of $N$ lines, each containing $M$ natural values separated by spaces, with the meaning from the statement.

# Constraints and clarifications
- $1 \leq N,M \leq 300$
- For $80\%$ of the tests, $1 \leq N,M \leq 100$;
- The dimension $P$ or $-P$ of a tile is chosen such that the obtained coverage does not exceed the height $N$ or the width $M$ of the surface.
- The data in the input file are correct in the sense that they represent the encoding of a tiling of the rectangular area of dimensions $N$ and $M$.

# Example 1
`placare.in`
```
4 4
-4 1 1 1
1 2
2 1
3
```
`placare.out`
```
4 1 1 1
4 1 2 2
4 2 2 1
4 3 3 3
```
## Explanation
The value $-4$ encodes a tile with height $4$ and width $1$ placed starting from the square at coordinates $(1,1)$ until the square at coordinates $(4,1)$. The value $3$ on the last line of the encoding designates a tile with width $3$ and height $1$, placed horizontally, starting from the square at coordinates $(4,2)$.

# Example 2
`placare.in`
```
3 2
-3 -2
0
1
```
`placare.out`
```
3 2
3 2
3 1
```
```
