Ionuț goes hiking in a square-shaped area with a side length of $N$ meters. A map of the area is divided into a grid, splitting the region into $N \cdot N$ unit squares, each with a side length of $1$ meter. Thus, the map of the area looks like a square grid with $N$ rows and $N$ columns. Rows and columns are numbered from $1$ to $N$. The elements of the two-dimensional table correspond to unit squares. The area can be traversed by crossing any side of the unit squares **at most once**.

~[55bdc2f5c84ca3f4b5a80867350d0328.png]

Ionuț starts from the point located at the bottom-right corner of the unit square in row $X$, column $Y$ and moves by making **one step** (crossing a unit square's side) in one of the directions $North$, $East$, $South$, $West$. To easily remember the path, he uses the following encoding for the $4$ directions: $1$ for moving North, $2$ for moving East, $3$ for moving South, and $4$ for moving West. Upon reaching another point (corner of a unit square), Ionuț continues to move without crossing the same side of a unit square more than once.

Ionuț stops when he reaches a point he has passed before. The path traversed between the two passes through the same point delineates an area of land formed by unit squares.

# Task

Given the row $X$ and column $Y$ corresponding to Ionuț's starting position, the area's dimension $N$, the path's length $L$, and the path, determine:

$a)$ The number of steps taken between the first and second pass through the stopping point.  
$b)$ The number of unit squares inside the area bounded by the path traversed between the two passes through the same point.

# Input data

The file `zona.in` contains:

The first line contains the values $X$, $Y$, $N$, and $L$, separated by a space, representing the coordinates of the starting point, the dimension of the area, and the path's length. 
The next line contains $L$ values from the set $\{1, 2, 3, 4\}$, separated by a space, representing the encoding of the entire path.

# Output data

The file `zona.out` will contain **two** lines: 

The first line contains a natural number representing the answer to Task $a)$, and the second line contains a natural number representing the answer to Task $b)$. **To receive partial scores, each line must contain a number!**

# Constraints and clarifications

* $0 < N < 51$
* $0 < X, Y < N$
* $0 < L < 2501$
* It is guaranteed that the path passes through the same point twice and does not cross the same side twice.
* For the correct determination of the number in Task $a)$, $20\%$ of the score is awarded.
* For the correct determination of the number in Task $b)$, $80\%$ of the score is awarded.

# Example

`zona.in`
```
2 3 7 18
2 3 3 3 4 3 4 1 1 1 1 1 2 2 2 3 3 4
```

`zona.out`
```
16
11
```

## Explanation

~[da212936caa305a5b6caf61a2265304a.png]

After $18$ steps from the start, he reaches the point located at the bottom-right corner of the unit square with coordinates $(3,4)$. 
The last $16$ steps traverse $11$ unit squares.