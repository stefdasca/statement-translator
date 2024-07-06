**Task**

Consider $A$ a two-dimensional array with $n$ rows, $n$ columns, and elements that are natural numbers. A triangular area of the array, represented by the triplet ($lin$, $col$, $k$), is an area in the shape of a right-angled triangle with legs of length equal to $|k|$, defined as follows:

For $k > 0$, the area is composed of $k$ rows:
* In the first row of the area, the elements are $A[lin][col], A[lin][col+1], \dots, A[lin][col+k-1]$;
* In the second row of the area, the elements are $A[lin+1][col], A[lin+1][col+1], \dots, A[lin+1][col+k-2]$;
* In the third row of the area, the elements are $A[lin+2][col], A[lin+2][col+1], \dots, A[lin+2][col+k-3]$;
* $\dots$;
* In the last row of the area, the element is $A[lin+k-1][col]$.

For $k < 0$, the area is composed of $|k|=-k$ rows:
* In the first row of the area, the element is $A[lin-|k|+1][col]$;
* In the second row of the area, the elements are $A[lin-|k|+2][col-1], A[lin-|k|+2][col]$;
* $\dots$;
* In the last row of the area, the elements are $A[lin][col-|k|+1], A[lin][col-|k|+2], \dots, A[lin][col]$.

The sum of the elements that compose a triangular area is called the area sum.

**Task**

Write a program that, given the array $A$ and $Q$ triangular areas, determines the largest among the area sums.

**Input data**

The input file `triunghi.in` contains on the first line the natural number $n$, with the significance given in the statement. On the next $n$ lines there are $n$ natural values each, representing the elements of the array $A$. The line $n + 2$ contains the natural number $Q$, representing the number of triangular areas. On the next $Q$ lines there are the triplets of values $lin \\ col \\ k$, which represent the $Q$ areas, in the form described in the statement. The values on the same line of the file are separated by a space.

**Output data**

The output file `triunghi.out` will contain a single line on which a natural number representing the required maximum sum is written.

**Constraints and clarifications**

* $3 \leq n \leq 1 \ 000$; $1 \leq Q \leq 100 \ 000$; $2 \leq |k| \leq n$;
* The values in the array are natural numbers from the interval [$1, 100$].
* The rows and columns of the array $A$ are numbered from $1$ to $n$ (rows from top to bottom, and columns from left to right).
* $|k|$ represents the absolute value of the number $k$ ($k$, for $k \geq 0$, respectively $-k$, for $k < 0$).
* It is guaranteed that any triangular area among the $Q$ is entirely included within the array $A$.

**Example**

`triunghi.in`
```
6
5 8 10 4 9 4
2 10 10 2 4 8
8 10 3 4 6 6
4 6 9 7 1 9
6 7 2 2 10 6
10 4 6 1 10 4
3
4 1 3
4 4 -4
6 5 -2
```

`triunghi.out`
```
59
```

**Explanation**

~[triunghi.png]

The triangular area with the maximum sum ($59$) is represented by the triplet ($4, 4, -4$) and contains the highlighted values: $59 = 4 + (10 + 2) + (10 + 3 + 4) + (4 + 6 + 9 + 7)$.