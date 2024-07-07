# Task

Mark has built a rectangular parking lot, divided into square parking spots using markings, organized into $n$ rows (numbered from $1$ to $n$) and � columns (numbered from $1$ to $m$). Thus, a parking spot can be identified by its row number and column number. Any car can be parked within a parking space, parallel to the horizontal lines of the marking or parallel to the vertical lines, without exceeding the contour of the corresponding square. Mark has built a surrounding wall for the parking lot, interrupted at certain parking spots, to allow cars to exit the parking lot. We consider that the wall is placed on line $0$ (north), column $0$ (west), line $n + 1$ (south), and column $m + 1$ (east).

~[img0.png|align=right|width=50%]

A car parked parallel to the horizontal markings can move along the row, to the left or to the right, and can exit the parking lot if it reaches a wall interruption to the west or east, and only if there is no other car parked in its moving direction towards the exit. A car parked parallel to the vertical markings can move up or down along the column, and can exit the parking lot if it reaches a wall interruption to the north or south and only if there is no other car parked in its moving direction towards the exit. Cars can move forward or in reverse. For example, the car parked at position $(2,2)$ parallel to the horizontal markings cannot exit the parking lot because if it moves west it reaches the wall, and if it moves east, it cannot reach the corresponding wall interruption on that row due to other cars parked along the way, but the car at position $(2,6)$ can exit by moving east. Exiting the parking lot is done in consecutive series, with the cars in a series starting to move simultaneously (after all the cars from the previous series have exited); the current series includes all cars which at that moment have a clear path to at least one wall interruption (no need for the movement of any other remaining cars in the parking lot, including those in the current series), even if their path to the exit intersects with the path of other cars from the same series, in movement. In the first series, all cars that can leave the parking lot immediately, without being conditioned by the movement or exit of other cars, exit.

# Task

Write a program that, given the dimensions of the parking lot, the positions of the wall interruptions, the number of cars, and for each car, the row and column number corresponding to the parking spot and its parking mode, solves the following two tasks:

1. Determine the number of cars that can exit the parking lot without being conditioned by the movement or the exit of other cars (the number of cars that can exit in the first series);
2. Determine the total number of cars that can exit the parking lot, as well as the number of series in which the exit of all these cars is realized.

# Input data

The input file `parking.in` contains on the first line the natural numbers $c$, $n$, $m$, $k$, and $q$ representing, in order, the task number, the number of rows and the number of columns of the parking lot, the number of wall interruptions, respectively, the number of parked cars. The next $k$ lines contain two natural numbers $i$ and $j$ representing the positions (row, respectively column) of the wall interruptions. The next $q$ lines contain three natural numbers $x$, $y$, and $p$ representing, in order, the row and column number corresponding to the parking spot of a car and its parking mode ($p$ = 0 for parallel parking with the horizontal markings, and $p$ = 1 for parallel parking with the vertical markings). The values written on the same line are separated by a space.

# Output data

The output file `parking.out` will contain a single line:

* The number of cars that exited the parking lot in the first series, if $c = 1$;
* The total number of cars that exited the parking lot and the number of series in which the exit of the cars took place, separated by a space, if $c = 2$.

# Constraints and clarifications

* $2 \le n, m \le 1 \ 000$
* $2 \le k \le 2 \cdot n + 2 \cdot m$
* $2 \le q \le min(n \cdot m, 100 \ 000)$
* $1 \le i \le n$, for $j = 0$ or $j = m + 1$, and $1 \le j \le m$, for $i = 0$ or $i = n + 1$
* $1 \le x \le n$, $1 \le y \le m$, $0 \le p \le 1$
* It is guaranteed for the test data that the number of series obtained will be at most $10 \ 000$, if $c = 2$.
* While parking to exit the parking lot, the cars will move such that they do not collide.

| # | Points | Constraints|
| - | - | ------------|
|1|12|$C = 1 \ \ n, m, q \le 150$|
|2|16|$C = 1$ and no additional constraints|
|3|12|$C = 2 \ \ n, m, q \le 150$|
|4|60|$C = 2$ and no additional constraints|

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

Six cars can exit the parking lot without waiting for other cars to move or leave from the parking spots at positions: $(2, 6)$ – east, $(3, 1)$ – north, $(4, 2)$ – west, $(4, 7)$ – south, $(6, 1)$ – west, $(6, 3)$ – south.

~[img1.png|align=center|width=37%]

**Second example.** Series 1: the six cars mentioned in the previous example exit the parking lot.

Series 2: the three cars from the parking spots at positions: $(3, 6)$ – north, $(4, 3)$ – south, $(6, 6)$ – west exit the parking lot. The configuration appears in the first image below.

Series 3: one car from the parking spot at position: $(4,5)$ – west. A total of $6 + 3 + 1 = 10$ cars can leave in $3$ series. The configuration appears in the second image below.

~[img2.png|align=center|width=37%]