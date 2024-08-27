## Task

In the year $2006$, people constructed the first biomechanical robot with artificial intelligence. However, it is still unclear how advanced its intelligence is. Therefore, the robot will be subjected to a test. It will be placed in a rectangular area, divided into squares positioned on $5$ rows and an infinite number of columns. The columns are numbered from $-\infty$ to $+\infty$ and the robot is initially placed in the column numbered $0$. The rows of the rectangular area are numbered from $1$ to $5$ and the robot will initially be placed on row $3$ (the middle one).

The robot will be oriented in one of the $8$ possible directions: North, North-East, East, South-East, South, South-West, West, North-West.

The moves the robot can make are:
1. **Rotation by an angle multiple of $45$ degrees**

   From the direction it is facing, the robot can turn to any other direction. A rotation from an initial direction to a final direction consumes a certain amount of time. Due to the robot's internal structure, it may be that a rotation by a larger angle takes less time than a rotation by a smaller angle. Also, a rotation from direction $X$ to direction $Y$ may not take the same amount of time as a rotation from direction $Y$ to direction $X$.

2. **Move in the direction it is facing, from the current square to the next square (having a common edge or vertex with it)**

   For example, if the robot is on row $3$, column $X$, facing North-East, it could move to the square on row $2$, column $X+1$. After moving, the robot does not change the direction it is facing. It is also not allowed to move outside the rectangular area (thus, certain moves are forbidden from certain squares).

The amount of time required for a move depends both on the direction in which it moves (due to Earth's magnetic field) and the row on which the robot is currently located (since each of the $5$ rows has a different electromagnetic structure). However, the costs of the moves do not depend on the column the robot is in.

The robot will be subjected to a test, as follows: it will be given $TMAX$ units of time. Using them, it will have to move as far away as possible from the current position. The distance is not measured in terms of squares, but in terms of columns. If after $TMAX$ time units the robot is on column $X$, the distance is considered $|X|$ (the absolute value of $X$). The row it ends up on is not important. The robot will choose the direction in which it will initially be oriented and the amount of time will start decreasing after it makes this decision. Find out the maximum distance the robot can travel in $TMAX$ units of time.

## Input data

The first line of the input file `biomech.in` contains the amount of time $TMAX$. The following $8$ lines contain $8$ integers each. The $j$-th number from the $i$-th of these lines represents the time required to change from direction $i$ to direction $j$. The following $5$ lines contain $8$ integers each. The $j$-th number from the $i$-th of these lines represents the time required to move in direction $j$ from a square on row $i$. Values for forbidden moves are also provided. These should be ignored. The order of directions (from $1$ to $8$) is as follows: N, NE, E, SE, S, SW, W, NW.

## Output data

Print on the single line of the output file `biomech.out` the maximum distance the robot can travel without exceeding the duration of $TMAX$.

## Constraints and clarifications

$1 \leq TMAX \leq 10^{15}$

$TMAX$ is an integer

$1 \leq time required for any rotation or move \leq 1000$

## Examples

`biomech.in`
```
4
0 10 10 10 10 10 10 10
10 0 10 10 10 10 10 10
10 10 0 10 10 10 10 10
10 10 10 0 10 10 10 10
10 10 10 10 0 10 10 10
10 10 10 10 10 0 10 10
10 10 10 10 10 10 0 10
10 10 10 10 10 10 10 0
1000 1000 1000 1000 1000 1000 1000 1000
1000 1000 1000 1 1000 1000 1000 1000
1000 1000 1000 1000 1000 1000 1000 2
1000 1000 1000 1000 1000 1000 1000 7
1000 1000 1000 1000 1000 1000 1000 1000
```

`biomech.out`
```
0
```