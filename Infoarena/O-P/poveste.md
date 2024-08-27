# Story

The Faculty of Automation and Counting has decided to produce a robot named AutoMitică, which can pass the Turing Test. Since this test requires the robot to be capable of at least a minimal literary analysis, researchers have taught it today about circular narrative style. More precisely, AutoMitică is capable of reading "literature" in the form of a binary matrix of dimensions $A \times B$. Each of the $B$ columns represents a page for AutoMitică, and it reads them from left to right, in increasing order of column indices. Since AutoMitică is not very talented, it can recognize the circularity of a story only if the first page is literally identical to the last page of the story. The researchers at the faculty have a binary matrix of dimensions $N \times M$ and would like to cut out a submatrix with the largest possible area, which has the property of circularity (i.e., the first column is identical to the last).

## Input data

The input file `poveste.in` will contain on its first line the value $T$ signifying the number of tests in the file. $T$ tests will follow this format: the first line will contain the values $N$ $M$ representing the number of rows and the number of columns of the matrix, respectively. It continues with $N$ lines each containing $M$ characters 0 or 1, not separated by whitespace.

## Output data

The output file `poveste.out` will contain $T$ lines, each containing a single value representing the answer for the respective test.

## Constraints and clarifications

$1 \leq T \leq 5$

$1 \leq N, M \leq 1000$

Tests 1 and 2 respect $N, M \leq 60$

Tests 3 and 4 respect $N, M \leq 400$

Tests 5, 6, and 7 respect $N, M \leq 650$

## Example

`poveste.in`
```
1
3 4
1011
0001
1000
```

`poveste.out`
```
6
```

## Explanation

A $2 \times 3$ matrix can be cut with the top left corner at $(0, 0)$.