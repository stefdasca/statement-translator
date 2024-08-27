# Museum

## Task

A museum is square-shaped and has $N \times N$ rooms that can be visited. Some rooms are open and contain artworks, others are closed (used for other purposes). In some of the free rooms, there are guards. The museum director is afraid of a possible break-in and therefore wants to evaluate how well the guards are positioned in the free rooms. More precisely, he wants to know, for each free room, the minimum distance to the nearest guard (the minimum number of rooms a guard has to cross to reach that room). Guards can only move to free rooms in the North, East, South, or West directions (provided they do not leave the museum).

## Input data

The file `muzeu.in` contains on the first line the integer $N$ , representing the number of rows (and columns) of the museum (the museum having $N \times N$ rooms). The next $N$ lines contain $N$ characters each:
- `.` for a free room that does not contain a guard
- `P` for a free room that contains a guard
- `#` for a closed room (which neither guards nor thieves can enter)

## Output data

In the file `muzeu.out` print $N$ lines, each containing $N$ integers (separated by spaces). Each number corresponds to the room in the corresponding row and column from the input file. For each free room, print the minimum distance to the nearest guard (or $-1$ if no guard can reach this room). For closed rooms, print $-2$.

## Constraints and clarifications

$1 \leq N \leq 250$

## Example

`muzeu.in`
```
8
...#....
#..#..#.
.##.P..#
..#.#.#.
........
........
###...##
..P.....
```

`muzeu.out`
```
-1 -1 -1 -2  2  3  4  5
-2 -1 -1 -2  1  2 -2  6
 8 -2 -2  1  0  1  2 -2
 7  6 -2  2 -2  2 -2  6
 6  5  4  3  4  3  4  5
 6  5  4  3  4  4  5  6
-2 -2 -2  2  3  4 -2 -2
 2  1  0  1  2  3  4  5
```