Archaeologists have discovered the ruins of a medieval castle on a difficult-to-access mountainous plateau, which they photographed from a helicopter, obtaining its digitized map. The map is stored as a two-dimensional array $H$, composed of $N \cdot N$ squares with sides equal to one unit, having as elements natural numbers between $0$ and $15$, which encode the shape of the walls of each unit square. If we write the natural number $H[i][j]$ in base $2$, using exactly $4$ binary digits, each bit gives information about one of the walls possibly built on each side of the unit square at position $(i,j)$, as follows:

* if the bit at position $0$ is $1$, then there is a wall on the west side (left side)
* if the bit at position $1$ is $1$, then there is a wall on the south side (bottom side)
* if the bit at position $2$ is $1$, then there is a wall on the east side (right side)
* if the bit at position $3$ is $1$, then there is a wall on the north side (top side)
* a bit with a value of $0$ indicates the absence of the corresponding wall

For a number written in base $2$, the digit numbering starts with position $0$, from right to left. The castle is interesting because, for better defense, the rooms composing it are either constructed independently or one inside the other. Any room is built at a distance of at least one unit from the wall surrounding the castle or from the walls of other rooms.

Using the map, archaeologists want to find information about the number of rooms and the room with the maximum area. By the area of a room, we mean the number of unit squares included within its walls, without counting the areas of rooms built inside it.

# Task

Knowing the encoding of the castle map, determine:

1. the total number of rooms in the castle
2. the maximum area of a room
3. the coordinates of the top-left and bottom-right corners of the room with the maximum area. If there are several rooms with the same maximum area, then the coordinates of the room with the top-left corner $({lin}_1, {col}_1)$ with the smallest ${lin}_1$ should be displayed, and with equal lines, the one with the smallest ${col}_1$.

# Input data

The input data is read from the file ```castel.in```, which has the following structure:

* The first line contains the natural number $C$, which can be $1, 2$, or $3$, depending on the task to be solved
* On the next line contains the natural number $N$, representing the size of the map
* On the following $N$ lines there are $N$ natural numbers from the interval $[0,15]$, separated by a space, representing the map of the castle.

# Output data

The output data is written to the file ```castel.out```, as follows:

* If $C = 1$, the first line will contain the total number of rooms in the castle
* If $C = 2$, the first line will contain the maximum area of a room in the castle
* If $C = 3$, the first line will contain $4$ natural numbers ${lin}_1 \\ {col}_1 \\ {lin}_2 \\ {col}_2$, separated by a space, representing the coordinates of the top-left and bottom-right corners of the room with the maximum area.

# Constraints and clarifications

* $2 \leq N \leq 100$;
* It is guaranteed that there is at least one room in the castle.
* $10$ points are awarded by default.

| $C$ | Points |
| - | ------- |
| $1$ | 20      |
| $2$ | 50      |
| $3$ | 20      |

# Example 1

`castel.in`
```
1
9
0 2 0 0 0 0 0 0 0 
4 15 1 0 0 2 2 0 0 
0 10 2 0 4 11 14 1 0 
4 9 12 1 2 10 10 2 0 
4 3 6 5 9 8 10 12 1 
0 10 8 4 1 4 15 5 1 
4 13 1 4 3 2 10 6 1 
4 7 1 0 8 8 8 8 0 
0 8 0 0 0 0 0 0 0
```

`castel.out`
```
6
```

## Explanation

~[imagineex1.png]

The figure represents the castle map coded in the input file.
It contains $6$ rooms.

# Example 2

`castel.in`
```
2
9
0 2 0 0 0 0 0 0 0 
4 15 1 0 0 2 2 0 0 
0 10 2 0 4 11 14 1 0 
4 9 12 1 2 10 10 2 0 
4 3 6 5 9 8 10 12 1 
0 10 8 4 1 4 15 5 1 
4 13 1 4 3 2 10 6 1 
4 7 1 0 8 8 8 8 0 
0 8 0 0 0 0 0 0 0
```

`castel.out`
```
11
```

## Explanation

The maximum area of a room is $11$.

# Example 3

`castel.in`
```
3
9
0 2 0 0 0 0 0 0 0 
4 15 1 0 0 2 2 0 0 
0 10 2 0 4 11 14 1 0 
4 9 12 1 2 10 10 2 0 
4 3 6 5 9 8 10 12 1 
0 10 8 4 1 4 15 5 1 
4 13 1 4 3 2 10 6 1 
4 7 1 0 8 8 8 8 0 
0 8 0 0 0 0 0 0 0
```

`castel.out`
```
5 5 7 8 
```

## Explanation

The room with the maximum area has the coordinates $(5,5)$ – $(7,8)$.