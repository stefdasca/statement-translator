Consider a Cartesian coordinate system and two distinct lines $d_1$ and $d_2$, parallel to the Ox axis. The distance between the two lines is $d$. On each of these lines, a number of points are fixed.

# Task

Determine:

1) how many parallelograms can be formed with the given points;
2) how many of these are rectangles;
3) the parallelogram with the largest perimeter.

A parallelogram is a convex quadrilateral with opposite sides parallel. Rectangles, squares, and rhombuses are special cases of parallelograms; therefore, they are also considered parallelograms.

# Input data

The input file `paralel.in` contains the following data:

- The first line contains a natural number $d$, representing the distance between the two lines;
- The second line contains a natural number $m$, representing the number of points fixed on the line $d_1$;
- The next $m$ lines contain $m$ distinct integers $a_1$, $a_2$, $\\dots$, $a_m$, representing the abscissas of the $m$ points fixed on the line $d_1$;
- The next line contains $n$, which represents the number of points fixed on the line $d_2$;
- The next $n$ lines contain $n$ distinct integers $b_1$, $b_2$, $\\dots$, $b_n$, corresponding to the abscissas of the points fixed on the line $d_2$.

# Output data

The output file `paralel.out` will contain three lines **mandatory**:

- The first line contains the number of parallelograms;
- The second line contains the number of rectangles that can be formed;
- The third line contains four integers separated by a space. These will represent the abscissas of the points that determine the parallelogram with the maximum perimeter. The first two values will represent the points on $d_1$ and will be written in ascending order; the next two values will represent the points on $d_2$ and will also be written in ascending order.

# Constraints and clarifications

* $0 < d \\leq 6 \\ 000$
* $0 < m,n \\leq 1 \\ 000$
* $-3 \\ 000 \\leq a_i \\leq 3 \\ 000$ for any natural number $i$ with the property $1 \\leq i \\leq m$
* $-3 \\ 000 \\leq b_i \\leq 3 \\ 000$ for any natural number $i$ with the property $1 \\leq i \\leq n$
* It is guaranteed that the requested number does not exceed $1 \\ 000 \\ 000 \\ 000$
* If no parallelogram exists, print `0 0 0 0` for task 3.
* If there are multiple parallelograms with the maximum perimeter, the output file will contain the corresponding values for the vertices of one of them.
* The score is awarded for the correct data on the three mandatory lines in the output file as follows:
  * the first line in the file correct: $40\\%$ of the score;
  * the second line in the file correct: $30\\%$ of the score;
  * the third line in the file correct: $30\\%$ of the score.

# Example

`paralel.in`
```
5
6
1
-2
7
8
15
10
3
-3000
1
-2
```

`paralel.out`
```
2
1
7 10 -2 1
```

## Explanation

The first parallelogram has vertices at the abscissas $1$ and $-2$ on the first line and respectively $1$ and $-2$ on the second line (the parallelogram is a rectangle).

The second parallelogram has vertices on the first line with abscissas $7$ and $10$ and vertices on the second line with abscissas $1$ and $-2$.

The parallelogram with vertices at points $7$, $10$ on $d_1$ and $-2$, $1$ on $d_2$ has the maximum perimeter.