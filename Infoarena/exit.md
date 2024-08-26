## Task

Two friends (Ionel and Gigel) are trapped inside a maze consisting of $X \times Y$ cells (the coordinates of the cells take values from $0$ to $X-1$, respectively from $0$ to $Y-1$). Among these cells, only $C$ cells are accessible, the others being blocked. From a cell $(x,y)$, movements can only be made to one of the $4$ neighboring cells: to the north, into cell $(x,y+1)$; to the east, into cell $(x+1,y)$; to the south, into cell $(x,y-1)$; to the west, into cell $(x-1,y)$. Movements can only be made if it does not go out of the maze and if the passage to the neighboring cell is not blocked. The cost of such a move is $1$ unit. The two friends know the coordinates of $N$ magical cells that they need to visit in order. The magical cells must be visited by at least one of the two friends, but not necessarily by both. Initially, Ionel and Gigel are in cell $(x_0,y_0)$. From here, one (or both) of them will go to the first magical cell. After Ionel or Gigel (or both) has (have) reached the $i$-th magical cell, one (or both) of them will move to the $(i+1)$-th magical cell. Between two magical cells (or between the initial cell and the first magical cell), they can pass through other magical cells, but the $i$-th magical cell is considered visited when one of the two friends arrives in it only if: $i=1$ or if the $(i-1)$-th magical cell has already been visited. After visiting the $N$-th magical cell, both friends need to reach this cell in order to finally exit the maze. Determine the minimum total cost of the movements made by the two friends to visit the $N$ magical cells and reach both in the $N$-th magical cell.

## Input Data

The first line of the input file `exit.in` contains $6$ integers, separated by a space: $N$, $X$, $Y$, $x_0$, $y_0$, $C$. The next $C$ lines contain $6$ integers each, separated by a space: $x_c$, $y_c$, north, east, south, west. $(x_c,y_c)$ represents the coordinates of a cell, and north, east, south, and west are numbers from the set $\{0,1\}$. If the number is $1$, then the passage to the neighboring cell in that direction is blocked (and if it is $0$, the passage is free). The blocked passages will be symmetrical (if a cell has the passage to the north blocked, then the cell to the north, if not a blocked cell, will have the passage blocked to the south). The next $N$ lines contain two integers each, separated by a space. The $i$-th of these lines contains the numbers $x_{m_i}$, $y_{m_i}$, representing the coordinates of the $i$-th magical cell.

## Output Data

In the output file `exit.out`, print the minimum total cost of the movements made by the two friends until they reach the last magical cell.

## Constraints and Clarifications

$1 \leq X, Y \leq 100$  
$1 \leq C \leq X \times Y$  
$1 \leq N \leq 1000$  
It is guaranteed that the two friends will be able to visit the $N$ magical cells.

## Example

`exit.in`  
```
2 3 2 0 1 6
0 0 1 1 1 1
0 1 1 0 1 1
1 0 1 1 1 0
1 1 1 0 1 0
2 0 1 1 0 0
2 1 0 1 1 0
2 1
0 1
``` 
`exit.out`
```
4
```