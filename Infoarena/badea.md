# Badea

Badea Gheorghe has a very large farm in the shape of a square consisting of $L \times L$ square cells with a side of $1 \text{ m}$. Being very old, he is thinking about leaving his entire farm as an inheritance to his $N$ grandchildren. Badea Gheorge wishes to give each grandchild a rectangular plot with integer width and length. Moreover, all $2 \times N$ sides must have different lengths. For example, he does not want to give one grandchild a $1 \times 2$ plot and another grandchild a $2 \times 3$ plot. Because he was never good at math, Badea Gheorghe will ask for help in dividing the farm.

## Input data

The input file `badea.in` contains on the first line $2$ integers $N$ and $L$. The tests that will be used for evaluation can be found in the following table. Test $0$ is an example and will not be scored.

Test \# 

0 1 2 3 4 5 6 7 8 9 10 

$N$

5 5 5 6 6 7 7 8 8 9 10 

$L$

12 14 20 16 35 35 40 21 29 25 30

## Output data

The output file `badea.out` will contain $L$ lines, and on each line $L$ integers separated by a space. The $x$-th number on the $y$ line represents to which grandchild the cell $(x, y)$ belongs. Each grandchild is associated with a unique integer between $1$ and $N$ (inclusive).

## Constraints and clarifications

For all tests in the table, there is a solution. The land area received by each grandchild must be strictly positive. Since you are given the input tests, it is recommended that your program displays the precomputed result.

## Example

`badea.in`

```
5 12
```

`badea.out`

```
1 1 1 1 1 5 5 5 5 5 5 5 
1 1 1 1 1 5 5 5 5 5 5 5 
1 1 1 1 1 5 5 5 5 5 5 5 
1 1 1 1 1 3 3 3 2 2 2 2 
1 1 1 1 1 3 3 3 2 2 2 2 
1 1 1 1 1 3 3 3 2 2 2 2 
1 1 1 1 1 3 3 3 2 2 2 2 
1 1 1 1 1 3 3 3 2 2 2 2 
1 1 1 1 1 3 3 3 2 2 2 2 
1 1 1 1 1 3 3 3 2 2 2 2 
1 1 1 1 1 3 3 3 2 2 2 2 
4 4 4 4 4 4 4 4 2 2 2 2
```

## Explanation

The first grandchild receives a plot of $11 \times 5$, the second grandchild receives a plot of $4 \times 10$, the third grandchild receives a plot of $3 \times 9$, the fourth grandchild receives a plot of $1 \times 8$, and the last grandchild receives a plot of $2 \times 7$. $1, 2, 3, 4, 5, 7, 8, 9, 10, 11$ are distinct numbers two by two.