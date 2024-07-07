
# Task

You work at a company that produces microprocessors. To assemble the microprocessors, the company uses a robot consisting of a single arm. The arm is fixed at one end ("shoulder") at a point placed at the center of the working platform, and at the other end, it has a device of negligible length with which it can "pick up" the components from the working platform ("hand"). The arm can only move horizontally above the working platform.

The arm consists of a succession of $N$ rigid segments of lengths $L_1, L_2, \dots, L_N$, connected by joint points. More precisely, segment $1$ is connected by a joint point to the robot's shoulder, segment $2$ is connected by a joint point to segment $1$, $\dots$, segment $N$ is connected by a joint point to segment $N-1$ and has the "hand" at the other end. A joint point allows free rotation (at any angle) of the segment connected at that joint point.

To assemble a microprocessor, the robot must successively pick up its components from the working platform. Each component has a well-determined position on the working platform, by its coordinates relative to a Cartesian coordinate system, with the center at the robot's shoulder.

Your role in the company is to program the robot's movements. For this purpose, for each component that the robot will pick up, you must specify the "configuration" of the robot arm that allows reaching that component (the robot's hand must be placed above the position where the component is).

The configuration of the robot arm is defined by the angles between the segments of the rigid arm.

Write a program that, for a given position, determines a configuration for the robot's arm that allows it to pick up the component from that position, if possible.

~[robot.png]

# Input data

The input file `robot.in` contains a natural number $N$ on the first line, representing the number of segments that form the robot arm.
Each of the following $N$ lines contains a natural number. The number on line $i+1$ is the length of the $i$-th segment of the robot arm.
The last line contains two integers $x$ and $y$, separated by a space, representing the coordinates of the position where the robot's "hand" needs to reach.

# Output data

The output file `robot.out` contains a single line containing the value $0$ if it is not possible for the robot's hand to reach the position $x, y$. If the problem has a solution, the output file contains $N$ lines. On line $i$ is the real value $u_i$ which represents the angle between segment $i$ and segment $i-1$ (for any $i$ from 2 to $N$), and the value of $u_1$ represents the angle that segment $1$ forms in the robot's shoulder with the OX axis.

# Constraints and clarifications

* $2 \leq N \leq 10\ 000$
* $1 \leq L_i \leq 200$
* $0 \leq u_i < 360$
* $-100\ 000 \leq x, y \leq 100\ 000$
* Angles are measured counterclockwise and are expressed in degrees.
* The evaluation program will check if the point where the robot's hand is placed for the configuration given by you $(x_p, y_p)$ matches the point of coordinates $(x, y)$ with an allowable error.
* Each line ends with a line-end mark (Enter).

# Example 1

`robot.in`
```
3
10
5
25
15 20
```

`robot.out`
```
125.6725
0
252.5424
```

# Example 2

`robot.in`
```
3
10
5
25
2 4
```

`robot.out`
```
0
```
```

