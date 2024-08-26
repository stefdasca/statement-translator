## Task

Marcel acquired a painting, encoded in a matrix with $N$ rows and $M$ columns, where each cell contains a digit representing a color. Therefore, the painting $T$ has the color encoded by the digit $T[l][ c ]$ at row $l$ (numbered from top to bottom from $1$ to $N$) and column $c$ (numbered from left to right from $1$ to $M$). $K$ mischievous girls each make a copy of the painting and then paint a submatrix with a color $0 \leq cul[i] \leq 9$, meaning that all cells in row $l$ and column $c$ with $lin1[i] \leq l \leq lin2[i]$ and $col1[i] \leq c \leq col2[i]$ acquire the color $cul[i]$, while the other cells retain the color of the original painting, where $i$ represents the $i$ -th girl. The neomodernists ask themselves how valuable each of the new paintings is. They agreed to calculate the value of a painting as the sum of the mismatches between it and all the new paintings, including itself. The mismatch between painting $A$ and painting $B$ is defined as follows: For all positions $(a, b)$ in $A$ and all positions $(p, q)$ in $B$, the mismatch increases by $A[a][b] - B[p][q]$, that is, the difference (not absolute) between the digits representing the colors of the two chosen cells.

## Input data

The input file `tablou.in` contains, on the first line, the numbers $N$ for the rows, and $M$ for the columns of the painting, which will be described on the next $N$ lines, by a sequence of $M$ digits without any spaces. The line $N + 2$ contains the number $K$ of girls. On each of the following $K$ lines, there are $5$ numbers $lin1[i]$ $col1[i]$ $lin2[i]$ $col2[i]$ $cul[i]$, describing the appearance of the painting obtained by the $i$ -th girl.

## Output data

The output file `tablou.out` will contain $K$ numbers on separate lines, representing the numerical value of each painting, in the order in which they were described in the input. Thus, the $i$ -th number in the output corresponds to the $i$ -th new painting from the input.

## Constraints and clarifications

$1 \leq N, M \leq 3000$

$1 \leq K \leq 100000$

$1 \leq lin1[i] \leq lin2[i] \leq N$

$1 \leq col1[i] \leq col2[i] \leq M$

For $10 \%$ of the tests, it is additionally known that $N, M, K \leq 11$

For another $20 \%$ of the tests, it is additionally known that $N, M, K \leq 200$

For another $30 \%$ of the tests, it is additionally known that $K \leq 1000$

You will only receive evaluation results for the example input file. These will not affect the problem's score, having an associated score of $0$. It is guaranteed that the response fits in signed 64-bit data types.

## Example

`tablou.in`:
```
4 5
01234
12345
23456
34567
11
1 1 3 3 2
1 2 4 5 8
2 3 2 3 5
3 5 4 5 6
2 1 3 5 3
3 2 4 3 0
3 3 4 4 9
4 3 4 5 5
3 4 4 4 1
1 1 1 1 0
3 4 4 5 7
```

`tablou.out`:
```
-1160
12920
-720
-1380
-2260
-4680
2360
-1820
-1820
-1160
-280
```