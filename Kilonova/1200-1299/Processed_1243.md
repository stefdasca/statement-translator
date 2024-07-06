```markdown
A grid in the form of a square with $n \times n$ cells is considered. We have at most $n \times n$ robots that can be placed in any of the grid cells, at most one robot in each cell. We will identify the robots placed on the grid by capital letters indicating their initial movement directions, as follows: a robot of type $U$ (up) will move from bottom to top (from the cell where it is located, to the cell situated on the line above and the same column), a robot of type $D$ (down) will move from top to bottom (from the cell where it is located, to the cell situated on the next line and the same column), a robot of type $L$ (left) will move from right to left (from the cell where it is located, to the cell situated on the same line and the left column), and a robot of type $R$ (right) will move from left to right (from the cell where it is located, to the cell situated on the same line and the right column).
The movement takes place for a known number of steps $k$. The initial configuration is considered step $0$. At each step $i$, each robot will move into a cell adjacent to the one occupied at the previous step $i - 1$, according to its movement direction. For example, a robot of type $U$ will advance into the cell placed above it, just as a robot of type $L$ will advance into the cell immediately to the left of the current one. It is possible for the robots' paths to intersect or overlap. If at a certain step, two or more robots advance into the same cell, then a small implosion occurs, and these robots disintegrate and disappear from the grid.
~[roboti1.png|align=right]
In $\text{Figure} \ 1$, such a situation is exemplified: the robots of type $D$ and $R$, present on the grid at step $i - 1$, disappear at the next step $i$, because they both advance into the cell in the middle of the grid, while the robot of type $U$ doesn't have such problems and continues its movement.
Let's comment now on $\text{Figure} \ 2$. The situation of the robots of type $D$ and $U$ from step $i - 1$ may seem conflictual, but they will advance into different cells at the next step $i$, hence they don't disintegrate; practically, they swap places and continue their movements.
~[roboti2.png|align=center]
In the same $\text{Figure} \ 2$, steps $i$ and $i + 1$ involve a special analysis that imposes new rules regarding robot movement. It is about the robots of type $L$ and $D$ who have reached the edges of the grid and can no longer execute movements to the left or down, according to their types. In such cases, the movement directions are simply reversed, and with that, the robots' types are changed. As seen in the figure, the robot of type $L$, at step $i$, can no longer move to the left, which is why it transforms into a robot of type $R$ and moves one cell to the right at step $i + 1$, following the movement rules corresponding to its new type. Similarly, the robot of type $D$ at step $i$ transforms into a robot of type $U$ at step $i + 1$ and moves up one position on the grid. Evidently, this rule also applies to the robots of the other two types, $R$ and $U$, which, if they reach the grid edges, become robots of type $L$ and respectively $D$, practically reversing their movement directions. This should also be the case for the robot of type $U$ located in the upper right corner of the grid at step $i + 1$. It should transform into a robot of type $D$ and occupy a position lower on the grid at step $i + 2$. However, this position is "claimed" also by the robot of type $R$. According to the previous discussions, if two or more robots advance into the same cell, they disintegrate and disappear from the grid, as illustrated in the figure. The robot of type $D$ from the step $i - 1$ is the only one that "survived" until step $i + 2$, even though it transformed during the process into one of type $U$; remaining alone on the grid, its movement continues indefinitely, considering the corresponding changes of direction and type, whenever necessary.

# Task

Given the initial configuration of the grid and a specified number of steps $k$, display the number of robots that will remain on the grid and the configuration obtained after $k$ steps.

# Input data

The input file `roboti.in` contains:
- The first line contains the natural number $n$ (the size of the grid).
- The second line contains the natural number $k$ (the number of steps).
- The next $n$ lines contain $n$ characters from the set $\\{$`U`, `D`, `L`, `R`, `.`$\\}$ (capital letters). If the cell does not contain any robot, then the `.` character (dot) is assigned, otherwise, the cell contains a robot, and one of the characters `U`, `D`, `L`, or `R` is assigned according to the initial type of the robot placed in the cell.

# Output data

The output file `roboti.out` will contain:
- The first line contains the number of robots that remain on the grid after $k$ steps.
- The next $n$ lines will print the $n \times n$ values representing the grid configuration after $k$ steps, in the form of $n$ lines, each line containing $n$ characters which can be: `U`, `D`, `L`, `R` or `.` (dot character).

# Constraints and clarifications

* $2 \leq n \leq 20$
* $1 \leq k \leq 100$
* The input/output files do not contain spaces.

# Example

`roboti.in`
```
3
4
...
.RD
..U
```

`roboti.out`
```
1
...
..D
...
```
```