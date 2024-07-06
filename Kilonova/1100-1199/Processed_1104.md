On a table, there are $N$ cubes placed next to each other, numbered in order from $1$ to $N$, with side lengths expressed in centimeters, as a nonzero natural number. An intelligent robot is programmed to build towers by stacking cubes on top of each other. It stands in front of the workbench, analyses each cube in order from the first to the last, and proceeds as follows:

* if it is at the first cube, it leaves it in its place on the table;
* it places the cube numbered $K$ on top of the cube numbered $K-1$ only if it has a strictly smaller side length than cube $K-1$. This operation is performed if cube $K-1$ is already part of a previously constructed tower or if it remained on the table. If cube $K$ cannot be placed on top of cube $K-1$, it remains in its place on the table.

# Task

Knowing that a tower can be made up of at least one cube, write a program that determines:
1. the largest number of adjacent cubes that have even side lengths expressed in centimeters;
2. the height (expressed in centimeters) of the tallest tower constructed by the robot.

# Input data

The input contains two natural numbers $C$ and $N$, in that order. $C$ represents the task number and can have two values $1$ or $2$ while $N$ represents the number of cubes on the workbench. Then $N$ natural numbers representing the side lengths of the cubes are read, in the order of their numbering.

# Output data

The output will contain a single natural number corresponding to the result obtained for solving each task.

# Constraints and clarifications

* $1 \leq N \leq 10\ 000$
* the side length of a cube can be from $1$ to $500\ 000$
* there is at least one cube that has an even side length expressed in centimeters
* $30$ points are awarded for the correct solution of the first task, and $70$ points for the correct solution of the second task.

# Example 1

`stdin`
```
1
7
18
12
10
17
8
2
7
```

`stdout`
```
3
```

## Explanation

Task $1$ will be solved. There are $7$ cubes, arranged as shown in the drawing. The largest number of adjacent cubes with even side lengths is $3$.

~[image.png|align=left]

# Example 2

`stdin`
```
2
7
18
12
10
17
8
2
7
```

`stdout`
```
40
```

## Explanation

Task $2$ will be solved. $3$ towers can be constructed, as shown in the image. The first tower has a height of $40$ cm, the second $27$ cm, and the third $7$ cm.

~[image2.png|align=left]