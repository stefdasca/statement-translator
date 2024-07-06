At a robotics contest, during the presentation, a cylindrical robot with a diameter of one unit goes out of control and moves into a rectangular-shaped ring. The ring is divided into $N \times M$ identical squares, with a side length of one unit, arranged in $N$ rows and $M$ columns.

~[Poza111.png|align=right|width=26em]

The robot can leave the ring only through the corners, which are numbered from $1$ to $4$, with corner number $1$ being the bottom left, and the rest being numbered counterclockwise. The surface of the ring is delimited by four separating walls: two "vertical" walls (from corner $1$ to corner $4$, and from corner $2$ to corner $3$) and two "horizontal" walls (from corner $1$ to corner $2$, and from corner $3$ to corner $4$), without blocking the exits, as shown in the adjacent drawing.

The robot enters the ring through corner number $1$ at a $45$ degree angle and with a speed of one unit per second. Collisions with the walls are considered perfectly elastic (the robot does not lose speed), and the angle of incidence is equal to the angle of reflection.

# Task

Determine the following:

1. After how many seconds and through which corner of the ring the robot will exit.
2. How many times the robot collides with the horizontal and vertical walls, resulting in a change of direction, until it exits the ring.

# Input data

The input file `reflex.in` contains on the first line two natural numbers $N$ and $M$, separated by a single space.

# Output data

The output file `reflex.out` will contain on the first line two natural numbers $S$ and $C$, separated by a single space, $S$ representing the number of seconds after which the robot will exit the ring, and $C$ representing the corner through which it will exit. On the second line, the output file will contain two natural numbers $H$ and $V$, separated by a space, $H$ representing the number of collisions with the horizontal walls of the ring, and $V$ the number of collisions with the vertical walls.

# Constraints and clarifications

* $3 \leq N, M \leq 2\ 000\ 000\ 000$
* For correctly solving a single task, $50\%$ of the points are awarded, and for correctly solving both tasks, $100\%$ of the points are awarded.

# Example 1

`reflex.in`
```
3 6
```

`reflex.out`
```
11 4
4 1
```

## Explanation

Until the exit, the robot traverses $11$ squares, and the exit occurs at corner $4$. There are $4$ collisions with the horizontal walls and $1$ collision with the vertical walls.

~[Poza222.png|width=30em]

# Example 2

`reflex.in`
```
5 7
```

`reflex.out`
```
13 4
2 1
```

## Explanation

The robot traverses $13$ squares, exits at corner $4$, and there are $2$ collisions with the horizontal walls at points $a$ and $c$, respectively, and $1$ collision with the vertical walls at point $b$.

~[Poza333.png|width=30em]
