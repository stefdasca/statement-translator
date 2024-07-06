~[patrat.jpg|align=right]

The largest astronomical observatory in Romania and Eastern Europe, situated in Galați, captured an image of the celestial sphere, displaying all visible stars at that moment. The image is in digital format, encoded as a two-dimensional array with $N$ rows and $M$ columns. Each element of the array contains a natural number representing the brightness intensity of a star.

We define a **brilliant star** as a star that has a brightness intensity greater than all the stars directly adjacent to it, whether horizontally, vertically, or diagonally. We define a **square constellation** as four brilliant stars placed at the corners of a square, with sides parallel to the edges of the array. The side length of a square constellation is equal to the number of stars forming one side. A brilliant star can be part of multiple square constellations.

# Task

Write a program to determine:
1. The number of brilliant stars;
2. The number of square constellations;
3. The side length of the square representing the largest square constellation.

# Input data

The file `patrat.in` contains on the first line two natural numbers $N$ and $M$, separated by a space, representing the dimensions of the two-dimensional array, followed by the next $N$ lines, each containing $M$ natural numbers separated by a space, representing the brightness intensity of the stars.

# Output data

The file `patrat.out` will contain:
- On the first line, a natural number representing the answer to task $1$.
- On the second line, a natural number representing the answer to task $2$.
- On the third line, a natural number containing the answer to task $3$.

# Constraints and clarifications

* $1 < N \leq 200$;
* $1 < M \leq 200$;
* $1 \leq$ brightness intensity of a star $\leq 1\ 000$;
* For correctly solving task $1$, $40\%$ of the points for each test will be awarded. For correctly solving task $2$, $40\%$ of the points for each test will be awarded. For correctly solving task $3$, $20\%$ of the points for each test will be awarded.
* Respect the output file format! To obtain the points awarded for a task, the answer in the file must be correct and written exactly on the specified line in the statement.

# Example 1

`patrat.in`
```
6 8
1 8 5 7 1 6 3 4
1 2 3 1 1 5 2 1
1 7 1 9 1 1 8 1
6 3 5 1 6 4 3 1
1 9 5 7 1 8 2 1
1 5 6 5 3 1 3 6
```

`patrat.out`
```
11
3
5
```

## Explanation

In the two-dimensional array with $6$ rows and $8$ columns, there are $11$ brilliant stars. The array contains $3$ square constellations, and the largest has a side length of $5$.

# Example 2

`patrat.in`
```
2 3
1 1 1
1 1 1
```

`patrat.out`
```
0
0
0
```

## Explanation

In the two-dimensional array with $2$ rows and $3$ columns, there are no brilliant stars. The array contains $0$ square constellations, and the largest has a side length of $0$.