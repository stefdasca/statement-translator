When Andrei stays home with his grandfather, his grandfather brings him a box of plastic chips in various colors. Last time, his grandfather asked Andrei to arrange the chips in a row, one next to the other, by color, from the color with the most chips to the color with the fewest chips.
Because the row was too long and did not fit on the carpet, his grandfather asked Andrei to form a square with the maximum possible side, taking the chips in the given order and placing them one next to the other (in equal numbers) on the lines of the square. The square will be filled from top to bottom, in increasing order of the rows, and on each row from left to right, in the increasing order of the columns.

# Task

Knowing the colors of the chips in the box, write a program that determines the number of existing colors in the game, the maximum side of the square that Andrei can build, and the way to arrange the chips in the square.

# Input data

The input file `joc.in` contains on the first line the natural number $N$, representing the number of chips in the game. The next $N$ lines contain the colors of the $N$ chips in the game, one chip per line. The colors are identified by digits between $1$ and $9$.

# Output data

The output file `joc.out` will contain on the first line a natural number $C$, representing the number of colors used for the chips in the game. The second line will contain a natural number $\text{MAX}$ representing the maximum side of the formed square. The following $\text{MAX}$ lines will contain $\text{MAX}$ digits between $1$ and $9$, representing the colors of the chips placed in the square, according to the constraints from the statement.

# Constraints and clarifications

* $1 \leq N \leq 60\ 000$
* There are no two colors for which the chips are in equal numbers.
* $30\%$ of the points are awarded for correctly determining the number of colors. $50\%$ of the points are awarded for correctly determining the number of colors and the maximum dimension of the side of the formed square. Full points are awarded for solving all three requirements.

# Example

`joc.in`
```
13
8
5
8
8
8
5
8
8
5
9
8
4
9
```

`joc.out`
```
4
3
888
888
855
```

## Explanation

In the game, there are chips of $4$ colors (colors $4$, $5$, $8$, $9$).
In the specified order from the statement, the chips could be arranged in a line as follows: $8888888555994$
With these chips, a square with a maximum side of $3$ can be built, considering the chips in the specified order, as follows:
$888$
$888$
$855$
Note that $4$ chips remain unused (one chip of color $5$, two chips of color $9$, and one chip of color $4$).