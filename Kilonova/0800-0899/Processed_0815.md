
The Advanced National Robotics Institute conducts a series of tests on the latest generation of intelligent robots designed by its specialists. The testing system is based on a network of sensors consisting of $n$ equal segments arranged horizontally and $n$ equal segments arranged vertically. The distance between two adjacent horizontal and vertical segments is $1$ meter. Each horizontal segment is in contact with each vertical segment. We call a point where a horizontal segment and a vertical segment come into contact a *node*. The segments are numbered: the horizontal ones from top to bottom starting with $1$, and the vertical ones from left to right starting with $1$.

A node will be identified by two numbers: the first represents the number of the horizontal segment and the second the number of the vertical segment that come into contact at that node.

In one of the network nodes, there is a target. In two other nodes, there are sources that emit a laser beam. Such a source emits the beam in only one direction. The laser beam has negligible thickness. The two sources are oriented so that the beam emitted by each "hits" the target. The two nodes in which the sources are placed are chosen so that the two beams only intersect at the node where the target is located.

In two other nodes of the network, there are robots. Each robot can move from one node to neighboring ones (those above, below, left, and right) without leaving the network. Robots move at $1$ meter/second.

~[bef10545696d117968b7bfe6325c2865.png]

Experiments are conducted in which the robots are programmed to move through the network to protect the target from the two laser beams. A robot can protect the target either by occupying the node where the source is or by occupying a node through which the laser beam passes on its way from the source to the target (the laser beams do not "avoid" the robots). The size of the robots is so small that, in this second case, they protect the target from the laser beam only when the nodes where the source, the target, and the robot are collinear, and the robot is between the source and the target. When a robot reaches a node where it protects the target from one of the beams, it can either stop or continue its movement. If it continues moving such that the new position occupied by that robot and the positions of the target and the source are no longer collinear, then that robot no longer protects the target. Due to the way the positions of the nodes for the target and laser sources are chosen, there is no position where a robot can simultaneously protect the target from both beams.

Each robot is equipped with a neural network and can learn from previous experiments where to move. To increase the adaptability of the robots, obstacles are placed in $k$ nodes of the network, making it impossible for robots to pass through those nodes. Since the obstacles used are transparent, the laser beams can pass through them without their intensity or direction being affected. Two or more obstacles placed on the same segment, in adjacent nodes, form a wall. The length of a wall is equal to the number of obstacles it is made of.

# Task

$1)$ Determine the maximum length of a wall.
$2)$ Determine the minimum number of seconds in which the two robots can protect the target from the two laser beams.

# Input data

The file `ai.in` contains:
- the first line contains a natural value $n$, representing the number of segments that make up the network;
- the second line contains five pairs of natural values separated by a space $T_1 \\ T_2 \\ S_1 \\ S_2 \\ S_3 \\ S_4 \\ R_1 \\ R_2 \\ R_3 \\ R_4$ with the following meaning: $T_1 \\ T_2$ represents the coordinates of the node where the target is, $S_1 \\ S_2$ the coordinates of the node where the first source is placed, $S_3 \\ S_4$ the coordinates of the node where the second source is placed, $R_1 \\ R_2$ the coordinates of the initial position of the first robot, respectively $R_3 \\ R_4$ the coordinates of the initial position of the second robot;
- the third line contains a natural value $k$, representing the number of obstacles in the network;
- the next $k$ lines contain a pair of natural values separated by a space. Each pair represents the coordinates of a node where an obstacle is placed.

# Output data

The file `ai.out` will contain:
- the first line contains a natural number representing the answer to task $1)$ and the second line contains a natural number representing the answer to task $2)$.

# Constraints and clarifications

* $n \leq 1 \ 000$
* $k \leq 150 \ 000$
- at the beginning of the experiment, the positions of the target, laser sources, robots, and obstacles are different.
- robots cannot occupy or pass through the node where the target is,
- robots can occupy a node at the same time.
- a robot can only protect the target from a beam when placed exactly in a node, not when it is between two nodes.
- an obstacle can belong at the same time to both a horizontal wall and a vertical wall.
- if the output file contains only one value, it is considered that it represents the answer to the first task
- in all tested cases, there is at least one possibility that the target is protected by one of the beams by one of the robots, and by the other beam by the other robot.
- solving the first task earns $20\%$ of the points; solving both tasks earns $100\%$ of the points.

# Example

`ai.in`
```
6
4 4 1 1 6 5 1 3 3 4
8
1 2 
2 3 
2 5 
4 2 
6 2 
2 2 
2 4 
5 2
```

`ai.out`
```
4
8
```

## Explanation

The longest wall has a length of $4$ (it is the one placed on the horizontal segment number $2$); the obstacles on the vertical segment $2$ form two walls with lengths $2$ and $3$.

The first robot reaches the position $6 \\ 5$ in $4$ seconds, thereby protecting the target from the beam emitted by the source at position $6 \\ 5$, and the second robot reaches the position $3 \\ 3$ in $8$ seconds, thereby protecting the target from the beam emitted by the source at position $1 \\ 1$. After $8$ seconds, the target is protected from both laser beams.
