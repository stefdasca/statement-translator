# Parallelepiped

Robert Acrisor has $N$ parallelepipeds in a three-dimensional system, with all sides parallel to the $OX$, $OY$, or $OZ$ axes and that can overlap. He wants to know the total volume occupied by the union of the $N$ parallelepipeds but has no idea how to do this, so he is asking for your help. For each of the $N$ parallelepipeds, two corners are given: the bottom-left-back corner and the top-right-front corner.

## Task

## Input data

The input file `parallelepiped.in` contains on the first line a natural number $T$, representing the number of tests. For each of the $T$ tests, the first line of the test contains a natural number $N$ representing the number of parallelepipeds, and the following $N$ lines contain 6 integers $X_i$, $Y_i$, $Z_i$, $X_f$, $Y_f$, $Z_f$ representing the two corners of the parallelepiped.

## Output data

The output file `parallelepiped.out` will contain the answer for the $T$ tests, one per line, representing the volume of the union of the $N$ parallelepipeds.

## Constraints and clarifications

$T = 75$

$1 \leq N \leq 75$

$-10^4 \leq X_i$, $Y_i$, $Z_i$, $X_f$, $Y_f$, $Z_f \leq 10^4$

The sides of the parallelepipeds are parallel to the $OX$, $OY$, or $OZ$ axes, and for each parallelepiped, $X_i \leq X_f$, $Y_i \leq Y_f$, and $Z_i \leq Z_f$

The $x$ coordinate increases from left to right, the $y$ coordinate increases from bottom to top, and the $z$ coordinate increases from back to front.

## Example

`parallelepiped.in`

```
3
1
0 0 0 1 1 1
2
0 0 0 1 1 1
0 0 0 1 1 2
3
0 0 0 1 1 1
0 0 0 1 1 2
3 3 3 4 4 4
```

`parallelepiped.out`

```
1
2
3
```

## Explanation

In the first test, we have a single parallelepiped with a volume of $1$. In the second test, the second parallelepiped entirely contains the first, so we have a total volume of $2$.