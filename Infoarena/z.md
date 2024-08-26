# ZTraversal

Petrica has a square board with dimensions $2^N \times 2^N$. He wants to write natural numbers between $1$ and $2^N \times 2^N$ on the squares of the board according to a special traversal he calls Z-traversal. A Z-traversal recursively visits the four quadrants of the board in the order: top-left, top-right, bottom-left, bottom-right. For example, if $N=1$, the order of visiting the squares on the board is in the shape of a Z, as shown in the following figure:

$1 \quad 2$
$3 \quad 4$ 

If $N=2$, Petrica will traverse the squares in the order:
$1 \quad 2 \quad 5 \quad 6$
$3 \quad 4 \quad 7 \quad 8$
$9 \quad 10 \quad 13 \quad 14$
$11 \quad 12 \quad 15 \quad 16$

## Task

At some point, Petrica would like to know the order numbers he needs to write according to the Z-traversal on certain squares given by their coordinates $(x, y)$. Petrica always starts filling the board from the top-left corner.

## Input data

The first line of the input file `z.in` contains two natural numbers $N$ and $K$, where $N$ indicates that the board has dimensions $2^N \times 2^N$, and $K$ is the number of squares for which Petrica wants to know what number he needs to write on them. Each of the next $K$ lines contains two natural numbers $(x, y)$, which represent the row and column of a chosen square. The $i+1$-th line describes the $i$-th square $(i = 1, 2, \dots, k)$.

## Output data

Each of the $K$ lines of the output file `z.out` will contain one natural number, corresponding to the number Petrica will write on the chosen square. The $i$-th line describes the $i$-th square $(i = 1, 2, \dots, k)$.

## Constraints and clarifications

$1 \leq N \leq 15$

$1 \leq K \leq 1\,000$

$1 \leq x, y \leq 2^N$

## Example

`z.in`
```
2 2
3 3
4 3
```

`z.out`
```
13
15
```