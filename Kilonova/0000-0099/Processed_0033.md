The moles are small-sized animals that live on open land surfaces, with the fox being their main enemy. Near a forest, there is an agricultural area in the shape of a rectangle, divided into equal-sized squares. The agricultural area is represented by a two-dimensional array with `m` rows and `n` columns, with rows and columns numbered starting from `1`. In this agricultural area, there is a mole living and `k` foxes.

We know the coordinates (row and column) of the mole as well as those of the foxes, who lie in wait to attack the mole in moments of inattention.

On the surface of the ground, the mole can move from its current square to one of the `4` neighboring squares in the north, south, east, or west directions.

The foxes can attack instantly within a range of `0`, `1`, or `2` units both horizontally and vertically, including their current position, after which they instantly return to their initial positions. In the figure below, the squares where a fox positioned in the square marked with the number representing the attack range can attack are drawn.
\
~[cartite.png]
\
To minimize the risk of moving in the agricultural area, the mole digs a system of `g` tunnels in the ground that connect the squares in the agricultural area. These tunnels do not intersect underground, only at the surface, the transition from one tunnel to another, which intersects in the same square, being done through a system that does not endanger the mole's life. The tunnels are indicated by the coordinates of the squares they connect. They are dug so that we can traverse all of them starting from one end. There are no two tunnels that start from the same square and end in the same square (the tunnels are distinct).

The mole wants to walk through all the tunnels underground, passing through each only once, but to do this it must reach a square on the surface from which it can enter the tunnel system unharmed.

# Task
Determine:
a) the nearest square to the mole's initial position through which it can enter the tunnel to walk, as well as the length of the path traversed on the surface so that each square on the path is not attacked by any fox;
b) the walking path only through tunnels, specified by the coordinates of the squares that constitute their ends.

# Input data
The input file `cartite.in` contains the following data:
- The first line contains a natural number `p`. For all input tests, the number `p` can only have the value `1` or the value `2`.
- The second line contains `m, n` the dimensions of the agricultural area;
- The third line contains the coordinates of the mole;
- The fourth line contains the number of foxes `k` followed by `k` lines, each with three natural numbers representing the coordinates of the squares where the foxes are located and their range of action (`0, 1` or `2`);
- The next line contains the number of tunnels `g`;
- Each of the following `g` lines contains `4` natural numbers separated by a space, representing the coordinates of the ends of a tunnel.

# Output data
If the value of `p` is `1`, **only the result from point a) of the task will be displayed**. In this case, the output file `cartite.out` will list three natural numbers separated by a space, representing the coordinates of the square where the mole will enter the tunnels and the length of the path traversed on the surface.

If the value of `p` is `2`, **only the result from point b) of the task will be displayed**. In this case, the output file `cartite.out` will contain the coordinates of the squares of the walking path through the tunnels (the coordinates of one square per line, starting with the first line of the output file). The starting square must be the same as the one where the mole ends its walk and it is not necessary to be the same as the one where it enters the tunnels from the surface of the ground.

# Constraints and clarifications
* `1 \leq m, n \leq 200`
* `1 \leq g \leq 100`
* `0 \leq k \leq 50`
* The length of the path traversed on the surface is equal to the number of squares it passes through, except the one it starts from.
* Each of the requirements represents `50%` of the score.
* The mole cannot enter the tunnels through a square within the range of a fox.
* For all tests, there is a solution to requirement a), meaning there is a safe path from the mole to a tunnel entrance.
* The solution is not unique, however, any correct solution will obtain the maximum score on the test.
* Initially, the mole is in a position where it is not attacked by any fox.

# Examples

`cartite.in`
```
1
6 4
6 3
3
5 1 0
3 4 1
4 3 0
7
1 1 3 2
1 3 1 4
1 1 3 3
1 4 4 2
4 2 3 3
4 2 1 3
4 2 3 2
```

`cartite.out`
```
4 2 3
```

`cartite.in`
```
2
6 4
6 3
3
5 1 0
3 4 1
4 3 0
7
1 1 3 2
1 3 1 4
1 1 3 3
1 4 4 2
4 2 3 3
4 2 1 3
4 2 3 2
```

`cartite.out`
```
1 1
3 2
4 2
1 3
1 4
4 2
3 3
1 1
```

Explanations
---

For the first test:
`p = 1`
The mole's movement on the agricultural surface will be on the path with a length of `3` that passes through the squares `(6,3) (6,2) (5,2) (4,2)`. The coordinates of the square for entering the tunnels are `(4,2)`.
**Attention! Only the result of requirement a) is displayed for this test.**

For the second test:
`p = 2`
The walking path through the tunnels is as follows: `(1,1) (3,2) (4,2) (1,3) (1,4) (4,2) (3,3) (1,1)`, noting that another starting square could also have been chosen.
**Attention! Only the result of requirement b) is displayed for this test.**
It is observed that for this case all data in the file must be read.