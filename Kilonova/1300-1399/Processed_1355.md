### Between Two Poles

Between two vertical poles on the banks of a river (one on each side) are two tightly stretched cables, parallel to the ground, with a distance between them of $d$ centimeters.

The cables are used to cross the river in case of floods. The poles are labeled $A$ and $B$, and the cables are labeled $1$ and $2$ as shown in the figure below. On the cables, there are $n$ colored points drawn in various colors, the colors being coded by the numbers $1, 2, 3, \ldots, k$. The position of the points on each cable is given by their distance from pole $A$ for each point. The points on each cable are numbered from $1, 2, 3, \ldots, n$. On each cable, there is at least one colored point in each color. To facilitate movement on the cable, the mayor decides to tie pairs of points of the same color, one from the first cable, and the other from the second cable, so that:

~[Poza3.png|align=right]

* For each color, there is only one pair of points connected.
* The total length of wire used is minimized.

# Task

Write a program that determines the minimum length of wire needed to solve the problem and a set of pairs of points that will be connected to achieve this minimum.

# Input data

The input file `stalpi.in` will contain:

* The first line contains the natural non-zero numbers $n, d$ separated by a space.
* The second line contains $n$ pairs of numbers, consisting of the distance from pole $A$ to each point and the color associated with the point, separated by a space, located on cable $1$.
* The third line contains $n$ pairs of numbers, consisting of the distance from pole $A$ to each point and the color associated with the point, separated by a space, located on cable $2$.

# Output data

The output file `stalpi.out` will contain the minimum value required on the first line, and the next $k$ lines will contain the order numbers of the points that will be connected with wire, separated by a space, first those on cable $1$, followed by those on cable $2$, in ascending order of colors.

# Constraints and clarifications

* $1 \leq n \leq 10\ 000$
* $1 \leq k \leq 100$
* $1 \leq d \leq 1\ 000$
* The distance between the two poles $A$ and $B$ is $30\ 000$
* The distances from pole $A$ to the points are natural numbers
* The minimum distance will be truncated to the first $3$ decimal places
* All points on a cable are distinct
* $40$% of the points are awarded for correctly determining the minimum in the task

# Example

`stalpi.in`
```
3 100
50 1 200 2 100 1
250 2 100 1 300 2
```

`stalpi.out`
```
211.803
3 2
2 1
```

# Explanation

There are $n=3$ pairs of points, $k=2$ colors, coded $1$ and $2$. The minimum amount of wire needed is $211.803$. Point $P3$ is connected to point $Q2$ (both are color $1$). Point $P2$ is connected to point $Q1$ (both are color $2$).