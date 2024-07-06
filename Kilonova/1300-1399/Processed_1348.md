Certainly! Here is the translated problem statement:

---

A matrix with elements $0$ or $1$, with $L$ rows (numbered from $1$ to $L$) and $C$ columns (numbered from $1$ to $C$) is given.

We define a rectangular area as a submatrix that has only values of $1$ on its contour and with the property that there are no $1$ values located outside the contour and at the same time at a distance of $1$ from a point on the contour. Two points are at a distance of $1$ if and only if they are neighbors in one of the $8$ directions.

The interior of a rectangular area consists of the elements of the submatrix not located on the contour.

A rectangular area can be completely included within another. We define the *order* of a rectangular area as the value $d+1$, where $d$ is the number of areas within which it is included.

Any $1$ element in the matrix is located on the contour of a single rectangular area.

$Fig.1-4$ contain examples of rectangular areas. In $fig.5$ there is a matrix in which three rectangular areas are found, among which the areas inside have an order of $2$ while the other has an order of $1$.

|$1 \\ 1 \\ 1 \\ 1 \\ 1 \\\\ 1 \\ 0 \\ 0 \\ 0 \\ 1 \\\\ 1 \\ 1 \\ 1 \\ 1 \\ 1 $|$1 \\ 1 \\ 1$|$1$|$1 \\ 1 \\ 1 \\ 1 \\\\ 1 \\ 1 \\ 1 \\ 1$|$1 \\ 1 \\ 1 \\ 1 \\ 1 \\ 1 \\ 1 \\ 1 \\ 1 \\ 0 \\\\ 1 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 1 \\ 0 \\\\ 1 \\ 0 \\ \\textit{1} \\ \\textit{1} \\ \\textit{1} \\ 0 \\ \\textit{1} \\ 0 \\ 1 \\ 0 \\\\ 1 \\ 0 \\ \\textit{1} \\ 0 \\ \\textit{1} \\ 0 \\ \\textit{1} \\ 0 \\ 1 \\ 0 \\\\ 1 \\ 0 \\ \\textit{1} \\ \\textit{1} \\ \\textit{1} \\ 0 \\ \\textit{1} \\ 0 \\ 1 \\ 0 \\\\ 1 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 1 \\ 0 \\\\ 1 \\ 1 \\ 1 \\ 1 \\ 1 \\ 1 \\ 1 \\ 1 \\ 1 \\ 0$|
|:-:|:-:|:-:|:-:|:-:|
|$fig. 1$|$fig. 2$|$fig. 3$|$fig. 4$|$fig. 5$|

# Task

Determine the total number of rectangular zones in the matrix, the maximum order of a zone, and the number of zones that have this maximum order.

# Input data

The input file `rectangles.in` contains on the first line the natural numbers $L$ and $C$ separated by a space.

Each of the next $L$ lines of the file contains $C$ numbers from the set $\\{ 0,1 \\}$, separated by a space, representing the values in the matrix.

# Output data

The output file `rectangles.out` contains on the first line three natural numbers $D, O$ and $NR$, separated by a space, where $D$ is the total number of rectangular zones in the matrix, $O$ is the maximum order of such a zone, and $NR$ is the number of zones of maximum order.

# Constraints and clarifications

* $3 \\leq L, C \\leq 1 \\ 000$
* The input data is correct. There will be at least one rectangular zone in the matrix.
* For the correct determination of the number of zones, $20\\%$ of the score will be awarded for each test.

# Example

`rectangles.in`
```
9 12
0 1 1 1 1 1 1 1 1 1 1 1
0 1 0 0 0 0 0 0 0 0 0 1
0 1 0 1 1 1 1 1 0 0 0 1
0 1 0 1 0 0 0 1 0 1 0 1
0 1 0 1 0 1 0 1 0 1 0 1
0 1 0 1 0 0 0 1 0 1 0 1
0 1 0 1 1 1 1 1 0 1 0 1
0 1 0 0 0 0 0 0 0 0 0 1
0 1 1 1 1 1 1 1 1 1 1 1
```

`rectangles.out`
```
4 3 1
```

# Explanation

There are a total of $4$ rectangular zones, the maximum order of one of them is $3$ (the one formed by a single $1$) and there is only one such zone.

---