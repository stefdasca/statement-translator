We are in the paint shop of the *Toyota Motor* plant where Japanese engineers are showcasing the latest type of industrial painting robot. In their desire to highlight the quality and speed of execution of the robots, they use a board of size $n \times n$, divided into squares with side lengths equal to $1$, represented as a two-dimensional array with $n$ rows and $n$ columns.
A robot used for painting has two telescopic arms that move along an axis. Each arm can paint one square in a unit of time. At time $t=0$, the robot receives a command to position itself in a square specified by coordinates $(x, y)$. Depending on the movement trajectory, the robots used are of two types. At time $t$, a type $1$ robot paints the squares at coordinates: $(x-t, y+t)$ and $(x+t, y-t)$, while a type $2$ robot paints the squares at coordinates: $(x+t, y+t)$ and $(x-t, y-t)$. Painting a square consumes $1$ liter of paint. There are $m$ robots placed on the board.

# Task
Given the initial coordinates $(x_{i}, y_{i})$ for the $m$ robots, $i=1, 2, \ldots, m$, determine:
1. The total amount of paint used by the robots after $t$ units of time.
2. The minimum number of time units required to form the first rectangle with a non-zero area. A correctly formed rectangle is the result of the intersection of two parallel trajectories of two type $1$ robots with two parallel trajectories of two type $2$ robots, and the corners of the rectangle are $4$ squares that have been painted by two robots of different types.

# Input data
The input file `robotics.in` contains on the first line three non-zero natural values $n$, $m$, and $t$, with the meanings from the statement, separated by a single space. Each of the next $m$ lines contains three non-zero natural values $x_{i}$, $y_{i}$, and $z_{i}$, separated by a single space, where: $x_{i}$, $y_{i}$ represent the initial coordinates where robot $i$ is positioned, and $z_{i}$ represents the type of robot.

# Output data
The output file `robotics.out` will have two lines.
The first line contains a non-zero natural number $C$ representing the total amount of paint used by the robots after $t$ units of time.
The second line contains a non-zero natural number $Tmin$ representing the minimum number of time units required to form the first rectangle with a non-zero area.

# Constraints and clarifications

* $1 \leq t < n \leq 1\ 000$
* $1 \leq m \leq 2 \cdot n$
* $1 \leq x, \ y \leq n$
* The coordinates of the $m$ robots are distinct in pairs.
* Two robots cannot be on the same trajectory at the same time.
* At time $t=0$ the robot positions itself in the square specified by coordinates $(x, y)$ and paints this square once.
* Two robots of different types that reach the same square at the same time can paint the square simultaneously.
* If an arm of a robot leaves the rectangular board, the arm stops its activity.
* The correct solution for the first task is awarded $20$ points, and for the second task $80$ points.

# Example 1

`robotics.in`
```
13 3 6
3 5 1
7 5 2
7 9 1
```

`robotics.out`
```
29
0
```

## Explanation

~[image1.jpg|width=50%]
The amount of paint used by the robots after $t$ units of time is $29$. Rectangles cannot be formed.

# Example 2

`robotics.in`
```
19 9 4
4 5 1
4 14 2
2 11 1
14 7 2
5 10 2
14 13 1
7 4 2
7 10 1
12 13 2
```

`robotics.out`
```
75
3
```

## Explanation

~[image2.jpg|width=50%]
The amount of paint used by the robots after $t$ units of time is $75$.
The only correctly formed rectangles after $t=4$ have corners in squares with coordinates: ($2$, $7$), ($6$, $11$), ($10$, $7$), ($6$, $3$) and ($8$, $9$), ($13$, $14$), ($17$, $10$), ($12$, $5$).
We observe that the first rectangle is formed after $t=3$ (the minimum time).