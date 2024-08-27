##  Gravity

In this problem, you need to simulate the fall of some two-dimensional objects that follow rules similar (but not identical) to the rules of the game Tetris. More precisely, you are given a matrix of dimensions $N \times M$ with cells of type $.$ or $#$ . The rows are numbered increasingly, from $1$ to $N$, from top to bottom. We call an object each maximal $4$-connected component of $#$ cells. All objects fall at the same speed downwards (in the direction of row $N$). If a certain object would exit (even partially) from the matrix by continuing the movement, it stops entirely. If a certain object would intersect with another object (even partially) by continuing the movement, it also stops entirely. Note that objects maintain their original structure throughout the movement, ignoring concepts like "material resistance" or "equilibrium state". You can consult the examples for clarifications. You are required to display the final state of the matrix (i.e., the state of the matrix after all objects have stopped moving).

## Task

The input file `gravity.in` will contain on its first line the dimensions of the matrix, $N$ and $M$ . The next $N$ lines will contain a string of $M$ characters each of type $.$ or $#$, representing the initial state of the matrix. 

## Input data

The input file `gravity.in` will contain on its first line the dimensions of the matrix, $N$ and $M$. The next $N$ lines will contain a string of $M$ characters each of type $.$ or $#$, representing the initial state of the matrix.

## Output data

The output file `gravity.out` will contain $N$ lines, each containing a string of $M$ characters, representing the final state of the matrix.

## Constraints and clarifications

$1 \leq N$
$M \leq 1750$

Warning, the memory for the stack is $8\ MB$.

The term $4$-connected refers to the fact that two cells are considered neighbors only in the $4$ directions (north, south, east, west).

For tests grouped worth $32$ points, $1 \leq N$
$M \leq 400$.

For tests grouped worth $14$ points, all pieces are rectangles of height $1$.

For tests grouped worth $51$ points, the general constraints remain valid.

The last feedback test is worth $3$ points and is alone in the group $\dots$.

## Example

`gravity.in`
```
10 10
..........
..######..
..#....#..
..#.#..#..
..#..#.#..
..#....#..
..######..
..........
..#....#..
.......#..
```

`gravity.out`
```
..........
..######..
..#....#..
..#....#..
..#....#..
..#.##.#..
..######..
.......#..
..#....#..
..........
```

`gravity.in`
```
10 10
...#......
...#.###..
..........
.#####....
.....#.##.
.....#.##.
..#.......
..#..##...
..#...#.#.
..........
```

`gravity.out`
```
..........
...#......
...#.###..
.#####....
.....#....
..#..#.##.
..#..####.
..#...#.#.
..........
```