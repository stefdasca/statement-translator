# Robot

Gigel has just bought a strategy game. The game's action takes place on a flat map. On the map, there is a small robot and several obstacles. The goal of the game is to move the robot to a certain location. Since he is not very good at computer games, Gigel is asking for your help. The robot and the obstacles are represented by convex polygons, with vertices at integer coordinate points. We say that the robot is in a valid position on the map if the polygon representing it does not intersect with the interior of any obstacle. If the robot is tangent to one or more obstacles, but does not intersect the interior of any of them, its position is considered valid. Throughout the game, the obstacles remain unmoved and unrotated. Also, the robot cannot rotate, but it can move in any direction. Throughout its movement, the robot must remain in a valid position. The position of the robot on the map is defined as the point $\( x,y \)$, with $ y $ equal to the minimum of the ordinates of the robot's vertices and $ x $ equal to the minimum of the abscissas of the robot's vertices. The curve drawn by the robot's position during its movement on the plane is called the robot's path.

## Task

Write a program that reads the initial configuration of the map and calculates the length of a minimum path traveled by the robot to reach a final position.

## Input data

The input file `robot.in` contains:
- The first line contains the number $N$ of vertices of the polygon representing the robot.
- The next $N$ lines contain the coordinates $x$ and $y$ of the robot's vertices, coordinates separated by a space.
- The next line contains the number $M$ of obstacles. 
- Then $M$ blocks follow, each representing an obstacle with the following structure: the first line of the block contains the number of vertices $P$ of the polygon representing the obstacle, and the next $P$ lines contain the coordinates $x$ and $y$ of the obstacle's vertices, coordinates separated by a space.
- The last line of the input file contains the coordinates $x$ and $y$ of the position where the robot must reach.

## Output data

The output file `robot.out` must contain on a single line, with two decimal places precision, the minimum distance traveled by the robot to the final position on a path that respects the above rules. If no such path exists, print $-1$.

## Constraints and clarifications

$N \leq 10$

$M \leq 25$

all coordinates are in the range $(-5000,5000)$

the number of vertices of all the obstacles' polygons does not exceed $250$

you can assume that the initial position of the robot is valid.

in the input file, for all polygons, the points are given in counterclockwise order.

your solution is considered correct if it differs from the jury's solution by at most $0.02$.

some say that the true champion is the one who solves $ivv$

the truth is, however, that the only one who can determine the true champion is the robot

## Example

`robot.in`
```
3
0 0
2 0
0 2
1
4
3 0
5 0
5 2
3 2
6 2
1
```

`robot.out`
```
7.24
```

## Explanation

The robot appears dotted and the obstacle is drawn with a thick line. The circle represents the robot's final position. A slightly thicker line also marks a minimum-length path.