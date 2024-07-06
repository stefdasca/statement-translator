In a cybernetic laboratory, experiments are being conducted with robots. On a work strip, there are $N$ yellow and blue cubes placed next to each other, numbered in order from $1$ to $N$. For each cube, the side length in centimeters and the color, coded by the symbol $g$ (for yellow) or $a$ (for blue), are known.

~[turnuri-1.png|align=right|width=30%]

An intelligent robot is programmed to construct towers by stacking the cubes on top of each other. It stands in front of the work strip, analyzes each cube in order from first to last, and proceeds as follows:
* if it is the first cube, it leaves it in place on the strip;
* it places the cube numbered $K$ on top of the cube numbered $K-1$ only if it has a different color and a smaller side length than cube $K-1$. This operation is performed if cube $K-1$ is already in a previously constructed tower or if it has remained in its initial position. If cube $K$ cannot be placed on top of cube $K-1$, it remains in its place.

# Task

Knowing that a tower can be formed of at least one cube, write a program that determines:
1. the final number $T$ of towers on the strip and $H$, the height of the tallest tower that can be formed, expressed in centimeters;
2. the largest number of cubes $N_{max}$ that can form a tower if the $N$ cubes could be initially rearranged on the strip, next to each other.

# Input data

The input file `turnuri.in` contains:
* the first line contains a natural number $C$ which represents the task number and can be $1$ or $2$.
* the second line contains a natural number $N$ which represents the number of cubes on the strip;
* each of the next $N$ lines contains a natural number representing the side length of a cube, followed by a space and the symbol $g$ or $a$ for the color code of the cube.

# Output data

In the output file `turnuri.out`, for task $1$, the first line will contain two values separated by a space representing $T$ and $H$. For task $2$, the file will contain the number $N_{max}$ on the first line.

# Constraints and clarifications

* $1 \leq N \leq 10 \ 000$ and $1 \leq$ side length of a cube $\leq 500 \ 000$;
* there are no two cubes with equal side lengths;
* $10$ points are awarded by default. For correct resolution of the first task, $30$ points are awarded, and for the correct resolution of the second task, $60$ points are awarded.

# Example 1

`turnuri.in`
```
1
6
18 a
13 g
15 a
10 a
8 g
2 a
```

`turnuri.out`
```
3 31
```

## Explanation

Task $1$ will be resolved. The second cube is placed on top of the first one and forms a tower with a height of $31$ centimeters. The third cube forms a tower by itself with a height of $15$ centimeters. The last three cubes form a tower with a height of $20$ centimeters. The number of towers is $3$. The height of the tallest tower is $31$ centimeters.

# Example 2

`turnuri.in`
```
2
6
18 a
13 g
15 a
10 a
8 g
2 a
```

`turnuri.out`
```
5
```

## Explanation

Task $2$ will be resolved. A possible rearrangement of the cubes would be as follows:

~[turnuri-2.png]

The first $5$ cubes form a tower.