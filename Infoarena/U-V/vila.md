# Villa

An important person in the country has a villa, represented by a matrix containing only characters $1$ and $-$, where $1$ represents a wall and $-$ represents free space. A room is formed from a set of free cells with the property that one can reach any cell of the room from any other cell of the same room by moving only in one of the directions $\{ N, S, E, W \}$, and passing only through free spaces. For example, the villa encoded by the matrix below has $3$ rooms:
```
1111111111111
1-------1----
----111111111
1-------1---1
1111111111111
```

## Task

Determine the following:
a) how many rooms the villa has;
b) which room has the largest area;
c) which wall needs to be removed (by wall we mean a single $1$ character) so that the resulting room has the largest area, compared to all other rooms that can be obtained by removing one wall.

## Input data

The input file `villa.in` has the following format:
The first line contains two natural numbers $M$ and $N$, separated by a space, which represent the number of rows and columns, respectively, of the matrix representing the villa, and on the next $M$ lines there are $N$ characters from the set $\{1, -\}$, describing the matrix.

## Output data

The output file `villa.out` contains the answers in the following format:
The first line contains the number of rooms,
The second line contains the area of the largest room,
And the third line contains the coordinates of the removed wall and the area of the resulting largest room.

## Constraints and clarifications

$1 \leq N, M < 128$
If there are multiple solutions for point $c$, the one with the smallest first coordinate will be displayed.
If there are still multiple solutions, the one where the sum of the coordinates is the smallest will be displayed.
No partial scores are awarded.

## Example

`villa.in`
```
5 13
1111111111111
1-------1----
----111111111
1-------1---1
1111111111111
```

`villa.out`
```
3
18
2 9 23
```