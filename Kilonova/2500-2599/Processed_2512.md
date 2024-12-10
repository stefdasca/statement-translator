Mark has built a rectangular parking lot, which he divided, using markings, into square parking spots, organized in $n$ rows (numbered from $1$ to $n$) and $\mathbf{m}$ columns (numbered from $1$ to $m$). Thus, a parking spot can be identified by the row number and the column number it occupies. Any car can be parked within a parking spot, parallel to the horizontal marking lines or parallel to the vertical lines, without exceeding the outline of the corresponding square. Mark built a surrounding wall for the parking lot, interrupted at some parking spots to allow cars to exit the parking lot. We consider that the wall is placed along line $0$ (north), column $0$ (west), line $n + 1$ (south) and column $m + 1$ (east).

~[img0.png|align=right|width=50%]

A car parked parallel to the horizontal markings can move along the row, to the left or to the right, and can exit the parking lot if it reaches an interruption of the wall on the west or east, and only if there is no other car parked in its direction of movement toward the exit. A car parked parallel to the vertical markings can move along the column up or down, and can exit the parking lot if it reaches an interruption of the wall on the north or south and only if there is no other car parked in its direction of movement toward the exit. Cars can move forward or in reverse. For example, a car parked at location $(2,2)$ parallel to the horizontal markings cannot exit the parking lot, because if it moves west it reaches the wall, and if it moves east, it cannot reach the interruption in the wall corresponding to that line due to other cars parked on its path, but the car from location $(2,6)$ can exit moving east. The exit from the parking lot is done in consecutive series, cars in a series starting their movement simultaneously (after all cars from the previous series have exited); the current series includes all cars that, exactly at that moment, have a clear path to at least one interruption in the wall (movement of any other cars remaining in the parking lot, including those in the current series, is not required), even if their path to exit intersects with the path of other cars from the same series, currently in motion. In the first series, all cars that can leave the parking lot immediately, without being conditioned by the movement or departure of other cars, exit.

# Task

Write a program that, knowing the dimensions of the parking lot, the positions of wall interruptions, the number of cars, and for each car the row number and column number corresponding to the place where it is parked and its parking mode, solves the following two tasks:

1. Determine the number of cars that can exit the parking lot without requiring the movement or departure of other cars (the number of cars that can exit in the first series); 
2. Determine the total number of cars that can exit the parking lot, as well as the number of series in which the exit of all these cars is accomplished.

# Input data

The input file `parking.in` contains on the first line the natural numbers $c$, $n$, $m$, $k$, and $q$ representing, in this order, the requirement number, the number of rows and the number of columns of the parking lot, the number of wall interruptions, respectively, the number of parked cars. The next $k$ lines contain two natural numbers $i$ and $j$ representing the positions (line, and column respectively) of the interruptions in the parking lot wall. The next $q$ lines contain three natural numbers $x$, $y$, and $p$ representing, in this order, the row number and the column number corresponding to the place where a car is parked and its parking mode ($p = 0$ for parallel parking with horizontal markings, $p = 1$ for parallel parking with vertical markings). The values written on the same line are separated by a space.

# Output data

The output file `parking.out` will contain a single line containing

* the number of cars that have exited the parking lot in the first series, if $c = 1$;
* the total number of cars that have exited the parking lot and the number of series during which the exit of the cars took place, separated by a space, if $c = 2$.

# Constraints and clarifications

* $2 \le n, m \le 1 \ 000$
* $2 \le k \le 2 \cdot n + 2 \cdot m$
* $2 \le q \le \min(n \cdot m, 100 \ 000)$
* $1 \le i \le n$, for $j = 0$ or $j = m + 1$ and $1 \le j \le m$, for $i = 0$ or $i = n + 1$
* $1 \le x \le n$, $1 \le y \le m$, $0 \le p \le 1$
* It is guaranteed for test data that the number of series obtained will be at most $10 \ 000$, if $c = 2$.
* Throughout the movement to exit the parking lot, the cars will circulate in such a way that they will not collide.

| # | Score | Constraints |
| - | - | ------------ |
| 1 | 12 | $C = 1 \ \ n, m, q \le 150$ |
| 2 | 16 | $C = 1$ and there are no additional constraints |
| 3 | 12 | $C = 2 \ \ n, m, q \le 150$ |
| 4 | 60 | $C = 2$ and there are no additional constraints |

# Examples

`parking.in`
```
1 6 7 11 16
0 1
0 4
0 6
7 2
7 3
7 5
7 7
1 0
4 0
6 0
2 8
1 2 1
1 4 0
2 2 0
2 4 1
2 6 0
3 1 1
3 4 0
3 6 1
4 2 0
4 3 1
4 5 0
4 7 1
5 6 0
6 1 0
6 3 1
6 6 0
```
`parking.out`
```
6
```

`parking.in`
```
2 6 7 11 16
0 1
0 4
0 6
7 2
7 3
7 5
7 7
1 0
4 0
6 0
2 8
1 2 1
1 4 0
2 2 0
2 4 1
2 6 0
3 1 1
3 4 0
3 6 1
4 2 0
4 3 1
4 5 0
4 7 1
5 6 0
6 1 0
6 3 1
6 6 0
```
`parking.out`
```
10 3
```

## Explanations

**First example.** The data corresponds to the image in the statement.

The $6$ cars parked in locations: $(2, 6)$ – towards east, $(3, 1)$ – towards north, $(4, 2)$ – towards west, $(4, 7)$ – towards south, $(6, 1)$ – towards west, $(6, 3)$ – towards south, can exit the parking lot without waiting for the movement or departure of other cars.

~[img1.png|align=center|width=37%]

**Second example.** Series $1$: the $6$ cars specified in the previous example exit the parking lot.

Series $2$: the $3$ cars parked in locations: $(3, 6)$ – towards north, $(4, 3)$ – towards south, $(6, 6)$ – towards west can exit the parking lot. The configuration appears in the first image below.

Series $3$: a single car parked in location $(4,5)$ – towards west can exit the parking lot. In total, $6 + 3 + 1 = 10$ cars can leave the parking lot in $3$ series. The configuration appears in the second image below.

~[img2.png|align=center|width=37%]