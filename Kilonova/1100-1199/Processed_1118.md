A new game consists of $n$ identical cubes, numbered from $1$ to $n$. Each cube has all six faces adhesive (with "scratch"). The game consists of creating an object from all the $n$ cubes. The initial object is cube $1$. An object is obtained from the previous object by attaching a new cube to a cube already in the object, on one of its faces.

To attach a new cube, a note with the number of the cube to which it will be attached is drawn, and a die is rolled which will indicate where the new cube will be attached (top, bottom, left, right, front, or back, positions coded respectively with $1$, $2$, $3$, $4$, $5$, $6$ of the cube in the object).

# Task

* Given a sequence of cube attachments, check if it is valid
* If the sequence is valid, specify whether the resulting object has the shape of a full cuboid, specifying its dimensions.

# Input data

The file `cuburi.in` contains on the first line the value of $n$. The following $n - 1$ lines contain a sequence of cube placements, for each cube specifying: $numar_{cub}$, $biletel$, $zar$, values separated by a space.

# Output data

The output file `cuburi.out` will contain on two lines the results of points a and b as follows:

* If the sequence is valid, the first line will contain the value $0$. Otherwise, the first line will contain the number of the cube that cannot be attached, the number of the cube and the number of the face to which it cannot be attached, as well as the error code: $1$ for attachment to a non-existent cube; $2$ for attachment to an occupied face.
* If the object is not a full cuboid, or if the sequence is not valid, the second line of the file will contain the value $0$.
* If the object is a full cuboid, the second line of the file will contain its dimensions, measured in number of cubes, in the order: number of cubes on the top-bottom, left-right, front-back directions separated by a space.

# Constraints and clarifications

* $2 \leq n \leq 1 \ 000$;
* on one dimension at most $10$ cubes are attached.

# Example 1

`cuburi.in`
```
6
2 1 1
3 2 4
5 1 4
6 3 1
4 6 3
```

`cuburi.out`
```
0
3 2 1
```

# Example 2

`cuburi.in`
```
4
2 1 1
4 2 1
3 2 4
```

`cuburi.out`
```
0
0
```

# Example 3

`cuburi.in`
```
8
2 1 1
5 1 4
6 3 6
7 6 2
3 2 4
4 2 6
8 7 3
```

`cuburi.out`
```
6 3 6 1
0
```

# Example 4

`cuburi.in`
```
8
2 1 1
4 2 6
3 2 4
6 3 6
7 6 2
5 1 6
8 7 3
```

`cuburi.out`
```
8 7 3 2
0
```

