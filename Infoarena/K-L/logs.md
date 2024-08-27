## Task

Given a binary matrix of dimensions $N \times M$, determine the area of the largest rectangle that contains only the value 1, knowing that you can permute the matrix columns.

## Input data

The first line of the input file `logs.in` contains two integers separated by a space: $N$ and $M$. The next $N$ lines contain $M$ characters of 0 or 1 each, describing the matrix.

## Output data

The single line of the input file `logs.out` will contain the area of the largest rectangle.

## Constraints and clarifications

$1 \leq N \leq 15000$

$1 \leq M \leq 1500$

30% of the tests will have $N, M \leq 1024$.

It is recommended to parse the input file using the $\text{fgets}$ function for C/C++ and $\text{readln()}$ and $\text{settextbuf}$ for Pascal.

## Example

`logs.in`

```
10 6
001010
111110
011110
111110
011110
111111
110111
110111
000101
010101
```

`logs.out`

```
21
```

## Explanation

By permuting the columns such that columns 2, 4, and 5 become adjacent, a rectangle with area 21 is obtained (lines 2-8 and columns 2, 4, 5).