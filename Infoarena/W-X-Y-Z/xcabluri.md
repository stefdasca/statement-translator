# Xcabluri

Since she ran out of hairspray, Ephie thought about using the current passing through the cables behind her computer to style her hair. However, she realized that even if she stretches the cables perfectly, some of them will intersect, and she will no longer be able to remove them easily. Therefore, she wants to find out for each cable how many other cables it intersects if they are perfectly stretched. Even though she has poor spatial orientation, she managed to create a map of the cables in the form of a two-dimensional matrix.

## Input data

The input file `xcabluri.in` contains on the first line $N$ and $M$ - the number of rows and the number of columns of the matrix created by Ephie. Each of the next $N$ lines contains $M$ numbers, representing the arrangement of the cables. Ephie has marked each of her $X$ cables with a distinct number, between 1 and $X$. Thus, in the matrix provided, there are positive natural numbers representing the path of each of her cables and $0$s representing empty spaces. In the matrix, any cable starts from column 1 and continues either to the upper-right, right, or lower-right. More precisely, if a portion of a cable is found at the coordinate $(i, j)$, then it can continue to one of the coordinates $(i - 1, j + 1)$, $(i, j + 1)$, or $(i + 1, j + 1)$. Of course, any cable ends at column $M$. When perfectly stretched, a cable coincides with the straight-line segment defined by the points where its ends are (from columns 1 and $M$).

## Output data

The output file `xcabluri.out` will contain $X$ natural numbers separated by spaces: $I_1$, $I_2$, $\dots$, $I_X$, where $I_i$ represents the number of cables that intersect with the cable marked with the number $i$ if all the cables are perfectly stretched.

## Constraints and clarifications

$1 \leq N, M \leq 100$  
$1 \leq X \leq N$

In the initial configuration, any two cables will not occupy the same coordinate.

## Example

`xcabluri.in`  
```
12 15
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
3 3 0 0 0 0 0 2 0 0 0 0 0 0 0
0 3 2 0 0 2 0 2 0 2 2 2 2 0 2
0 3 2 2 1 1 1 2 0 0 0 0 0 2 0
0 0 3 1 1 1 1 1 1 4 0 0 1 1 3
3 0 0 0 0 0 0 0 4 1 4 0 4 0 3
4 4 4 4 4 4 0 1 4 0 4 0 4 4 3
3 0 0 0 0 0 0 1 0 0 0 0 0 0 3
3 3 3 3 3 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
```

`xcabluri.out`  
`2 1 3 2` 

## Explanation

The pairs of cables that intersect after being perfectly stretched are: 1 and 3; 1 and 4; 2 and 3; 3 and 4.