```markdown
# Task

If you get injured, don't use Sprite to treat the wound. It's best to run to the nearest first aid station. Fortunately, you have a map from which you can find the Cartesian coordinates of the first aid stations. Unfortunately, due to the pain, you can't run directly to a station, but only in north-south and east-west directions. To know whether it makes sense for you to run to a station or to enjoy your last moments of life, it'd be best to evaluate the distance to the nearest first aid station.

The nearest first aid station is the one for which the Manhattan distance is minimal.

This time you were lucky enough because the time required to reach the station was sufficient; however, you wonder: if the accident had happened in another location, would you still have survived?

Consider $N$ points in the plane representing the first aid stations and other $M$ points representing possible accident locations. It is required to find, for each of the $M$ points, the Manhattan distance to the nearest station.

# Input data

The file `ajutor.in` contains on the first line the integers $N$ and $M$, in this order, separated by a space. Contained on the next $N$ lines are two integers, separated by a space, representing the coordinates of each first aid station. Contained on the following $M$ lines are two integers, separated by a space, representing the coordinates of the accident points. The coordinates are given in the order (abscissa, ordinate).

# Output data

The file `ajutor.out` will contain $M$ lines, each containing a single number representing the minimum distance to the nearest first aid station.

# Constraints and clarifications

* $0 < N < 401$
* $0 < M < 500 \ 001$
* Any coordinate is an integer within the range $[0,32 \ 000]$
* If you are already at a first aid station (coordinates are identical), the distance is $0$.
* The Manhattan distance is the shortest path between two points, moving only in directions parallel to the coordinate axes, i.e., $|x_1-x_2|+|y_1-y_2|$, where $(x_1,y_1)$, $(x_2,y_2)$ are the coordinates of the two points.
* There may be points with identical coordinates in the input file.
* Points are awarded for each test only if all values in the output file are correct.
* All Sprite does is quench your thirst.

# Example

`ajutor.in`
```
4 4
1 1
5 5
1 5
5 1
0 0
1 1
3 3
4 1
```

`ajutor.out`
```
2
0
4
1
```
```

Feel free to double-check the grammar and syntax for any potential errors.
