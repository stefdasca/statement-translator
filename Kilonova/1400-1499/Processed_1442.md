Costel has a great passion for solving the Rubik's Cube, so great that he began conducting various research and calculations based on this game. His latest idea, inspired by the Rubik's Cube, uses a cube with a side length of $2$ units, composed of $8$ unit cubes (unit cube), with the outer faces colored. Each unit cube has $3$ outer faces, and each of these is colored with one of the $10$ available colors, coded by the digits from $0$ to $9$.

| Figure 1  | Figure 2  |
|-----------|-----------|
| ~[f1.jpg] | ~[f2.jpg] |

The identification of the unit cubes is done according to the specifications in **Figure 1**. The cube that is not visible in **Figure 1** has the coordinates $(1, 1, 2)$. Costel's cube allows the following types of moves, similar to those in the Rubik's Cube:
* **M1**: Parallelepiped $1$ contains the unit cubes with coordinates: $(1, 1, 1); (1, 2, 1); (2, 1, 1); (2, 2, 1)$. This is a horizontally placed disc and can be rotated $90$ degrees to the right, clockwise.
* **M2**: Parallelepiped $2$ contains the unit cubes with coordinates: $(1, 1, 2); (1, 2, 2); (2, 1, 2); (2, 2, 2)$. This is a horizontally placed disc and can be rotated $90$ degrees to the right, counterclockwise.
* **M3**: Parallelepiped $3$ contains the unit cubes with coordinates: $(1, 1, 1); (2, 1, 1); (1, 1, 2); (2, 1, 2)$. This is a vertically placed disc and can be rotated $90$ degrees toward the far plane, counterclockwise.
* **M4**: Parallelepiped $4$ contains the unit cubes with coordinates: $(1, 2, 1); (2, 2, 1); (1, 2, 2); (2, 2, 2)$. This is a vertically placed disc and can be rotated $90$ degrees toward the far plane, clockwise.

|     M1    |     M2    |     M3    |     M4    |
|-----------|-----------|-----------|-----------| 
| ~[m1.jpg] | ~[m2.jpg] | ~[m3.jpg] | ~[m4.jpg] | 

Configuration is understood as recording the color of each outer face of the $8$ unit cubes, thus the colors of the $24$ outer faces. By applying a valid sequence of moves, another configuration is obtained. For ease of remembering a configuration, Costel uses the flat unfold of the $6$ faces of his cube as shown in **Figure 2**, which illustrates how the faces are arranged in the unfold. Each face of the cube contains four outer faces of the unit cubes having, in order, the coordinates specified in the figure.

# Task

Given an initial configuration and a final configuration of the game, determine the minimum number of moves to get from the initial configuration to the final configuration and the corresponding sequence of moves to achieve the final configuration.

# Input data

The input file `joc.in` contains:

* $12$ lines corresponding to the initial configuration - two lines for each of the six faces; on each line, two digits are recorded, separated by exactly one space (the first two lines hold the elements of face $1$, the next two lines hold the elements of face $2$, ..., lines $11$ and $12$ hold the elements of face $6$).
* The next $12$ lines contain the elements of the final configuration - two lines for each of the six faces; on each line, two digits are recorded, separated by exactly one space.

# Output data

The output file `joc.out` will contain:
* The first line contains a natural number $MIN$, representing the minimum number of determined moves.
* The next $MIN$ lines contain the sequence of moves that transform the initial configuration into the final configuration, with each line containing a natural number between $1$ and $4$ representing the number associated with a move.

# Constraints and clarifications

* It is guaranteed that for all test data, there is a solution with at most $11$ moves.
* Any solution with a minimum number of moves that leads to obtaining the final configuration will get the maximum score.

# Example

`joc.in`
```
1 2
3 1
2 7
5 4
2 9
9 4
2 9
4 5
5 8
2 3
6 4
1 7
2 2
9 1
2 7
5 4
7 9
4 4
1 9
3 5
8 3
5 2
6 4
1 2
```

`joc.out`
```
1
3
```

## Explanation

The disc $3$ is moved toward the far plane, which is move $3$.

~[fin.jpg]