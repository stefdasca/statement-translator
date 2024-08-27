## Task

Ligia has a matrix with $N$ rows and $M$ columns filled with values $0$ and $1$. She wonders what is the largest triangle that can be placed in the matrix only on elements equal to $0$. A triangle of height $L$ consists of $L$ rows, and the length of each row is $2$ more than the length of the previous row (except the first row which has a length of $1$). For example, a triangle of height $5$ looks like this:

```
.... 0 ....
... 000 ...
.. 00000 ..
. 0000000 .
000000000
```

Ligia wants to know the maximum area of a triangle that can be placed in the matrix such that it covers only elements equal to $0$. The area of a triangle is equal to the number of positions occupied by that triangle.

## Input data

The input file `trmax.in` will contain on the first line three numbers $N$, $M$, and $K$. The next $K$ lines will each contain two numbers $l_i$, $c_i$ representing that an element with value $1$ is located at row $l_i$ and column $c_i$. All other elements of the matrix will be equal to $0$.

## Output data

In the output file `trmax.out` you will print a single number representing the maximum area of a triangle that meets the conditions from the task.

## Constraints

$1 \leq N, M \leq 2000$

$1 \leq K \leq \min(N * M, 10^5)$

The triangle cannot be rotated

## Example

`trmax.in`

```
7 9 8
1 1
2 3
4 1
6 3
4 1
7 3
6 7
1 6
```

`trmax.out`

```
16
```

## Explanation

The matrix and the solution represented by the bold elements:

```
100000100
001000000
000010000
100000000
010000000
001000000
100001000
```