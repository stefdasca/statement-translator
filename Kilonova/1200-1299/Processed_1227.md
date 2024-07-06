```markdown
Mr. Gigi bought his son a construction game. The game consists of a square board $N \cdot N$ ($N$ rows and $N$ columns) and a number of $C$ colored cubes. The cube's side length is equal to the side length of one board square. Gigi junior places each cube on the board, in a given order, perfectly overlapping one face of the cube on the desired square. If there are already cubes at a certain position, the cube is placed on top of the existing ones. The game ends when all the cubes are placed on the board.
Mr. Gigi sees the game in its final form and looks at the board from three positions. The resultant image can be **top view, left view**, or **front view**.
Example: for $N=3, C=7$ and a placement of the cubes as in figure `a`), the three views are drawn in figures: `b` (top view), `c` (left view), and `d` (front view).

~[image.png|align=left]

# Input data

The input file `cuburi.in` contains:

The first line contains three natural numbers $N, C, D$, with the following meaning: $N$ - the size of the board, $C$ - the number of cubes, $D$ - the direction from which we view the board ($1$ - top view, $2$ - left view, $3$ - front view).

The next $C$ lines contain three natural numbers each. Thus, on line $i+1$, the numbers $\\text{Row, Col, Color}$, separated by space, represent the row, column, and the color of the $i$-th cube placed on the board.

# Output data

The output file `cuburi.out` will contain a two-dimensional array with $NL$ rows and $N$ columns representing the board's view, according to the direction read from the input file.

The first line of the file should contain the two dimensions $NL$ and $N$ separated by space, and on the next $NL$ lines, $N$ numbers representing the color codes of the visible cubes, respectively $0$ (zero) for areas without cubes.

# Constraints and clarifications

* $1 \\leq N \\leq 50$
* $1 \\leq C \\leq 50\ 000$
* Not more than $20$ cubes are stacked
* The color of a cube is coded by a number between $1$ and $15$
* It is always possible to place all the given cubes on the board
* Each line of the input and output files ends with a newline character

# Example

`cuburi.in`
```
3 7 2 
1 1 3 
1 1 1 
3 2 2 
1 3 1 
1 3 2 
1 3 1
1 3 3
```

`cuburi.out`
```
4 3 
3 0 0 
1 0 0 
1 0 0 
3 0 2
```

## Explanation

The tallest tower of cubes is located at position $(1,3)$ and has a height of $4$. Looking from the left side of the board, only the last two cubes of this tower are visible, the rest being hidden from view by the two-cube tower at position $(1,1)$.
On column $2$ there are no cubes, so we will fill it with $0$. 
On column $3$, only the cube from position $(3,2)$ is visible, the rest are filled with $0$ up to the maximum height.
```