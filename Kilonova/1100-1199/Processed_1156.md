
A rectangle of size $m \times n$ is divided into $m \cdot n$ squares with side $1$. Some of these squares have a NW-SE diagonal drawn (noted with $1$ in the matrix), others have a NE-SW diagonal (noted with $2$ in the matrix), and others have no diagonal (noted with $0$ in the matrix).

# Task

Write a program that determines how many squares are formed by these diagonals.

# Input data

The input file `patrate.in` contains on the first line the natural numbers $m$ and $n$, and on the next $m$ lines the description of the rectangle: each line contains $n$ numbers, separated by spaces, having the value $0$, $1$ or $2$.

# Output data

The output file `patrate.out` will contain on the first line the total number of squares formed by diagonals, and on the following lines the number of squares with side $ \sqrt{2}$, $2 \sqrt{2}$, $3 \sqrt{2}$, etc. until all squares are exhausted. If there are no squares of a certain size, write `0` on the respective line.

# Constraints and clarifications

* $2 \leq m, n \leq 100$

# Example 1

`patrate.in`
```
4 5
0 2 1 2 1
2 1 2 1 2
1 2 0 2 0
0 1 2 0 0
```

`patrate.out`
```
4
3
1
```

## Explanation
~[1.png|width=20em]

# Example 2

`patrate.in`
```
6 6
0 0 2 1 0 0
0 2 0 0 1 0
2 1 0 0 2 1
1 0 1 2 0 2
0 1 0 0 2 0
0 0 1 2 0 0
```

`patrate.out`
```
2
0
1
1
```

## Explanation
~[2.png|width=20em]
