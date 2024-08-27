# Walls

## Task

We are given $N$ rectangular walls in a plane, placed one after the other from left to right, all having a common base, and with $1$ cell of empty space between any two consecutive walls (the arrangement is exactly like in the game Walls). Each wall $i$ has a height of $H_i$ and a width of $W_i$, consisting of $W * H$ square cells of size $1 \times 1$. The bottom-left corner of the first wall is at the cell with coordinates $(1,1)$. The enemy wants to destroy as many walls as possible using a cannon that shoots cannonballs. This cannon has an adjustable position, allowing it to shoot a cannonball from any point where there is no wall cell. The cannon fires a cannonball that moves horizontally from right to left until it hits a wall cell, which it destroys. The cannonball is also destroyed in this collision. If the cannon destroys all the cells of a wall at a certain level, then that level and all levels above it are destroyed and disappear. Only the cells below the destroyed level will remain from the wall. Knowing that the enemy shoots the cannon $M$ times, calculate for each shot which cell is hit (if it hits one) and if the destruction of the cell causes the upper levels of the wall to fall.

## Input data

The input file `walls.in` will contain on the first line the number $N$, followed by $N$ lines with the pairs $W_i$ and $H_i$. The next line contains the number $M$, followed by $M$ lines with the coordinates of the cannon for each shot.

## Output data

The output file `walls.out` will contain one line for each cannonball. If the cannonball did not hit anything, the line contains only the string `MISS`. If the cannonball hit a cell, the line has the form: `HIT $x$_cell wall $fallen$` where:
- $x$_cell = the coordinate of the cell hit
- $wall$ = the wall hit by the cannonball
- $fallen$ = `YES` if the upper part of the wall has fallen or `NO` if not; `YES` is also displayed if the destroyed cell is on the highest level of the wall

## Constraints

1 $\leq N, M \leq 100\ 000$

1 $\leq W, H \leq 2\ 000\ 000\ 000$

## Example

`walls.in`

```
4
2 4
2 6
2 4
2 2
7
10 3
11 3
3 3
4 3
12 9
13 4
14 4
```

`walls.out`

```
HIT 8 3 NO
HIT 7 3 YES
HIT 2 1 NO
HIT 1 1 YES
MISS
HIT 5 2 NO
HIT 4 2 YES
```

## Explanation

The wall $3$ is hit at the cell $(8,3)$

The wall $3$ is hit at $(7,3)$, and levels $3$ and $4$ fall

The wall $1$ is hit at the cell $(2,4)$

The wall $1$ is hit at $(1,4)$, and level $4$ falls

There is no wall at height $9$

The wall $2$ is hit at the cell $(5,4)$

The wall $2$ is hit at $(4,4)$, and levels $4$, $5$, $6$ fall