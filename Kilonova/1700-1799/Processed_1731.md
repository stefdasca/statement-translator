Pixy lives in a colorful Country. The map of the Country can be represented as a rectangle divided into cells, organized in $M$ rows and $N$ columns. The rows are numbered from $1$ to $M$, starting from the top row, and the columns are numbered from $1$ to $N$, starting from the left column. Each cell has a certain color. The colors are coded with the letters `A`, `B`, `C`, `D`, `E`, `F` (there are only 6 colors).

Pixy's house is located in the cell with coordinates $(1, 1)$, and his friend, Pixela, lives in the cell with coordinates $(M, N)$. Pixy wants to reach the love of his life, but he can only step on cells of the same color. We know that Pixy can move only horizontally or vertically by one cell at a time.

To be able to reach Pixela, Pixy will proceed as follows: choose a color and recolor the cell where his house is with the chosen color. Thus, he will obtain an area of adjacent cells all having the same color. Two cells are considered adjacent if they are neighboring horizontally or vertically. For example, for the map in figure $1$, if he chooses the color coded $D$, he will obtain the area marked in figure $2$, all cells in this area having the color $D$.

~[pixy1.png]

Next, Pixy will proceed similarly: choose a new color, and recolor the entire area obtained in the previous step with the new color, thus the area he can step on will expand. For example, if in the situation from figure $2$, Pixy now chooses the color coded $C$, he will obtain the situation in figure $3$. The process continues until the cell corresponding to Pixela’s house also becomes part of the area obtained by Pixy following successive recolorings. The choice of colors at each step must be made carefully so that the number of recolorings is minimized. Now Pixy only has the task of finding the shortest path he will travel to reach Pixela, stepping only on the cells in the area obtained after the successive recolorings, that is, the cells along the path will all have the same color.

# Task

Determine:
1. the minimum number of recolorings
2. the length of the shortest path from Pixy to Pixela, traversed on the area obtained after the recolorings from Task $1$.

# Input data

The input file `pixy.in` contains the first line which contains two natural numbers $M$ and $N$, separated by a space, representing the dimensions of the map. The next $M$ lines contain $N$ capital letters of the English alphabet representing the colors of the cells on the map.

# Output data

The first line of the output file `pixy.out` will contain an integer representing the minimum number of recolorings. The second line of the file contains a single integer value, representing the length of the path traveled by Pixy.

# Constraints and clarifications

* $2 \leq M, N \leq 500$
* For a correct answer to the first task, $40\%$ of the score is awarded, and for a correct answer to the second task, $60\%$ of the score is awarded.
* The cells neighboring Pixy's house initially have colors different from the color of the house.

# Example

`pixy.in`
```
5 6
ADDBCD
DCDCBE
ACBAED
CBDADE
ABDCEE
```

`pixy.out`
```
5
9
```

## Explanation

The following recolorings are made:

* Step $1$: the color $D$ is chosen:

```
DDDBCD
DCDCBE
ACBAED
CBDADE
ABDCEE
```

* Step $2$: the color $C$ is chosen:

```
CCCBCD
CCCCBE
ACBAED
CBDADE
ABDCEE
```

* Step $3$: the color $A$ is chosen:

```
AAABCD
AAAABE
AABAED
CBDADE
ABDCEE     
```

* Step $4$: the color $D$ is chosen:

```
DDDBCD
DDDDBE
DDBDED
CBDDDE
ABDCEE
```

* Step $5$: the color $E$ is chosen:

```
EEEBCD
EEEEBE
EEBEED
CBEEEE
ABECEE 
```

There were $5$ recolorings made. The path that Pixy can take is the following: $(1, 1) \rightarrow (1, 2) \rightarrow (1, 3) \rightarrow (2, 3) \rightarrow (2, 4) \rightarrow (3, 4) \rightarrow (4, 4) \rightarrow (4, 5) \rightarrow (5, 5) \rightarrow (5, 6)$ and has a length of $9$.