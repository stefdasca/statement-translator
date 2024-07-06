In a rectangular area with $p$ rows and $q$ columns, there are $n$ robots. The top-left cell is located at row $1$ and column $1$. For each robot, its row and column, as well as its orientation, are known. A robot can be oriented in one of four directions: north, south, east, or west, encoded by the characters `N`, `S`, `E`, and `V`, respectively. Each robot executes $m$ commands. A command is encoded by a character `L`, `R`, or `F`. When executing a command of type `L`, the robot turns $90$ degrees to the left, counterclockwise. When executing a command of type `R`, the robot turns $90$ degrees to the right, clockwise. When executing a command of type `F`, the robot moves one position in the direction it is oriented.

The robots simultaneously execute their first command in their command sequence, then the second command, and so on. If at any moment, two or more robots reach the same position, they will disappear, and the cell they disappeared from is considered traversed by all those who disappeared. If a robot moves outside the surface upon executing a command, the robot disappears. Passing through a cell is considered when visiting it as a result of executing a command of type `F`. If a robot passes through a cell multiple times, each pass is counted. The cell where each robot starts is considered a pass for that robot.

# Task

Write a program to determine:
1. The number of robots remaining after executing the $m$ commands
2. The position of the cell in the area that was passed through the most (if there are multiple cells, then the one with the smallest row index is specified, and if there are multiple with this index, the one with the smallest column index) and the number of passes through this cell.

# Input data

The input file `roboti.in` contains:
* The first line contains $p$ and $q$, values separated by a space and representing the number of rows and columns of the area
* The second line contains the value $n$, representing the number of robots
* The next $n$ lines contain three values separated by spaces, representing the row, column, and orientation of each robot
* The next line contains the value $m$ representing the number of commands to be executed by each robot
* The next $n$ lines contain $m$ characters representing the commands for each robot (first the $m$ commands for the first robot, then the $m$ commands for the second robot, and so on). There are no spaces between the characters of a command

# Output data

The output file `roboti.out` will contain:
* The first line contains the number of robots remaining in the end
* The second line contains the position of the cell (row and column) that was passed through the most (if there are multiple cells, then the one with the smallest row index is specified, and if there are multiple with this index, the one with the smallest column index) and the number of passes through this cell, three values separated by a space

# Constraints and clarifications

* $1 \leq p, q, m \leq 50$
* $2 \leq n \leq 50$
* The characters used to encode the orientations can only be `N`, `S`, `E`, `V`, and those for commands can only be `L`, `R`, or `F` (uppercase).
* Initially, no two or more robots are in the same cell.
* $50\%$ of the score is awarded for solving requirement $1$ and $50\%$ for requirement $2$.

# Example

`roboti.in`
```
4 4
3
1 1 E
1 3 V
4 4 S
2
FL
FF
FF
```

`roboti.out`
```
0
1 2 2
```

## Explanation

After the first command, robots $1$ and $2$ will reach the same cell, so they disappear. The third robot will leave the area after the first move, so it disappears. In the end, there are $0$ robots. Two robots reached the cell at row $1$ and column $2$, after which they disappeared. The other cells were passed through at most once.