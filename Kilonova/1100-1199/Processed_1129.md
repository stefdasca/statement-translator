
A farmer has a rectangular plot of land that is $M$ units long and $N$ units wide. Trees are planted sporadically on the land, and the farmer does not want to cut them down.

Desiring to oversee his crops, the farmer builds a small square-shaped robot with a side length of $3$ units that he can guide through the farm unit by unit over a specific area.

The robot can move vertically and horizontally, but it cannot move over trees, destroy them, nor can it rotate, and it requires a surface suitable for its dimensions to move.

# Task

Help the farmer determine the maximum area he can monitor using this system.

# Input data

The input file is `ferma.in`.

The first line contains two natural numbers $N$ and $M$ separated by space.
The next $N$ lines contain $M$ characters, not separated by spaces. These characters encode the farm and have the meanings:
* `.` — free land;
* `+` — the place where a tree is planted;
* `R` — the center of the robot.

# Output data

The output file is `ferma.out`.

The next $N$ lines contain $M$ characters, not separated by spaces. These characters encode the farm and have the meanings:
* `.` — land not covered by the robot;
* `*` — land that can be monitored by the robot;
* `+` — the place where a tree remains.

# Constraints and clarifications

* $1 \leq N, M \leq 50$

# Example

`ferma.in`
```
12 11
...........
...+.....+.
...........
...........
.+.........
...+.......
.+...R.....
.........+.
..+.......+
......+....
...........
......+....
```

`ferma.out`
```
....*****..
...+*****+.
..*********
..*********
.+*********
...+*******
.+.********
...******+.
..+******.+
******+....
******.....
******+....
```
