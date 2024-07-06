In the coordinate system xOy, we consider N shelves fixed parallel to the Ox axis. The shelves are described by the triplet of non-zero natural numbers: $x_1$, $x_2$, $y$, where $x_1$, $x_2$ – represent the left and right ends of the shelf, and $y$ is the height at which the shelf is fixed. The shelves do not overlap (they do not have common points).

From a point with integer coordinates $(X, Y)$, above all the shelves, water flows from a tap. If the water reaches a shelf, it drips on the shelf towards the ends. Thus, if the water touches the shelf described by $(x_1, x_2, y)$, it moves in both directions towards the ends of the shelf, from where it will fall vertically in the directions $x_1$, respectively $x_2$, until it reaches either another shelf or the floor $(y = 0)$.

Shelves that are touched by water are considered wet. In other words, a shelf described by $(x_1, x_2, y)$ is considered touched by water if $x_1 \leq x_a$, $x_a \leq x_2$ and $y < y_a$, where $(x_a, y_a)$ represents the coordinates from where the water flows.

# Task

Determine:
* how many shelves are not touched by water (are not wet)
* the maximum number of shelves that have been wetted, located on the same vertical axis parallel to Oy.

# Input data

The input file `umede.in` contains on the first line the non-zero natural number $N$, with the significance from the statement. The next $N$ lines contain the description of the $N$ shelves. On the last line in the file, the coordinates $X$, $Y$ of the tap are found.

# Output data

The output file `umede.out` will contain, one per line, two natural numbers $n_1$ and $n_2$, where $n_1$ represents the number of shelves that are not touched by water, and $n_2$ the maximum number of shelves located on the same vertical that have been wetted.

# Constraints and clarifications

* $0 < N \leq 50 \ 000$
* $1 \leq y \leq 5 \ 000$, $y < Y \leq 5 \ 001$
* $1 \leq X \leq 1 \ 000 \ 000 \ 000$, $1 \leq x_1 < x_2 \leq 1 \ 000 \ 000 \ 000$
* The water stream has no thickness
* For tests worth $29$ points: $1 \leq N \leq 5 \ 000$, $1 \leq x_1 < x_2 \leq 5 \ 000$, for all shelves.
* For other tests worth $39$ points: $1 \leq x_1 < x_2 \leq 2 \ 000 \ 000$, for all shelves.
* For other tests worth $32$ points: the general restrictions are maintained.

# Example

`umede.in`
```
11
1 6 9
8 16 9
9 11 8
7 17 7
2 7 6
5 9 5
11 15 5
12 18 4
2 3 3
4 8 3
5 11 2
10 12
```

`umede.out`
```
3
5
```

## Explanation

~[umede.png]

There are $3$ shelves that are not touched by water. The maximum number of shelves on a vertical that have been wetted is $5$.