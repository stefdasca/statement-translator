# Agent 007

Agent 007 has to destroy a terrorist camp. The terrorist camp consists of several objectives (ammunition depots, pavilions for terrorists, etc.), considered point-like in the plane. Agent 007 receives a map from the intelligence service with `n` objectives in the terrorist camp, given by Cartesian coordinates. Besides the map, agent 007 also receives a special weapon (built for this mission). The received weapon has two barrels and allows simultaneous firing in the same direction (linear), but in opposite directions, of two rockets at the same speed. After firing the weapon, once one target is hit, the other rocket also explodes (even if it has not hit its target).

# Task

Agent 007 wants to destroy the camp as quickly as possible and with as few rockets as possible. For this, he studies the possibility of positioning himself **in a point** in the camp (different from the objectives) that allows effective firing, that is, to destroy two objectives simultaneously with each shot. Determine if it is possible to find such a point.

# Input data

The file `a007.in` contains on the first line the number of tests `k`, followed by data for each test. For each test on one line there is `n`, and on the next `n` lines are the coordinates of the objectives in the terrorist camp (separated by a space in order of x-coordinates and y-coordinates).

# Output data

The file `a007.out` will contain `k` lines, on each line it will contain `1`, if there is a solution, and `0` if there is no solution. In case there is a solution, the coordinates of the required point will be written on the same line separated by a space (real numbers truncated to `4` decimals, in order of x-coordinates and y-coordinates).

# Constraints and clarifications

* `0 \leq n \leq 10000`
* `1 \leq k \leq 3`
* The coordinates of the points are integers from the interval `[-10000, 10000]`
* An objective is destroyed if the rocket explodes exactly at the point corresponding to it.

# Example

`a007.in`
```
2
4
10 0
10 10
0 10
0 0
6
0 0
10 0
2 10
12 0
5 0
7 0
```

`a007.out`
```
1 5.0000 5.0000
0
```