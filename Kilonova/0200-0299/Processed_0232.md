A point-sized robot can move in the plane, in a straight line, in any direction. The robot starts at an initial position `S` and must reach a final position `F`, avoiding collisions with existing obstacles in the field. The obstacles are convex polygonal surfaces, with disjoint interiors and boundaries. We say the robot has collided with an obstacle if its position becomes interior to the obstacle. Therefore, if the robot moves along an obstacle, it does not collide with it. 

# Task

Write a program that determines the shortest path the robot can follow from its initial position `S` to its final position `F` without colliding with any obstacles.

The path will be specified by the sequence of critical points (the initial point, the points where the robot changes direction, and the final point). The length of the path is equal to the sum of the lengths of its segments.

# Input data

The input file `robot.in` contains:
1. The first line contains the coordinates of the robot's initial and final positions `xS yS xF yF`.
2. The second line contains `n` - the number of obstacles.
3. Then follow `n` groups of lines describing the obstacles. The first line of a group contains `k` - the number of vertices of the obstacle, followed by `k` lines each containing the coordinates of the obstacle's vertices `x y`.

# Output data

The output file `robot.out` contains the robot's path encoded as a sequence of points between which the robot moves in a straight line. The first line contains the number `nr` of points on the path. The following `nr` lines contain the coordinates of the points on the path, in order from the initial point to the final point.

# Constraints and clarifications

* `1 ≤ n ≤ 20`
* $k_1+k_2+...+k_n ≤ 100$
* $x_i, y_i$ are real numbers with two decimal places, $|x_i|, |y_i| ≤ 100\ 000$
* Points `S` and `F` are not inside any obstacle
* The coordinates will be displayed in the output file with two decimal significant figures.
* If there are multiple minimum-length paths, only one solution will be displayed.

# Example

`robot.in`

```
10 5 -10 -10
1
3
0 0
0 10
10.5 0
```

`robot.out`

```
3
10 5
10.5 0
-10 -10
```

# Explanation

The minimum distance is $\\sqrt{0.5^2 + 5^2} + \\sqrt{20.5^2 + 10^2} = 27.83..$