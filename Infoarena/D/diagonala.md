## Task

Electra has a square matrix with $N$ rows and $N$ columns containing elements $0$ or $1$. The matrix follows a peculiar property: for any row $i$, all elements equal to $1$ are in the compact interval between columns $X_i$ and $Y_i$ ($X_i \leq Y_i$). Electra defines a diagonal in this matrix as a line with a slope of $45^\circ$ or $-45^\circ$. She wants to find the longest diagonal made up of only elements equal to 1 in the matrix. Electra is asking for your help, and to understand better, she provides some examples of diagonals:

## Example

### Example 1

### Example 2

```
0 0 0 0 1 1 0 0 0 0 1 1 1 0 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 1 1 0 0 1 1 1 1 1 1 0 0 0 0 1 1 1 1 1 0 1 1 1 1 0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0 1 1 1 0 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 1 1 0 0 1 1 1 1 1 1 0 0 0 0 1 1 1 1 1 0 1 1 1 1 0 0 0 1 1 1 0 0 0 0 0
```

## Input data

The input file `diagonala.in` will contain on the first line the natural number $N$. The next $N$ lines will each contain two numbers $X_i$ and $Y_i$, separated by a space, representing that in row $i$ of the matrix, elements equal to $1$ are between columns $X_i$ and $Y_i$.

## Output data

In the output file `diagonala.out` you will print a single number representing the length of a maximal diagonal that respects the conditions from the statement.

## Constraints and clarifications

$1 \leq N \leq 200\ 000$ 

$1 \leq X_i \leq Y_i \leq N$ 

Rows and columns are numbered from $1$ to $N$ 

For $20\%$ of tests $N \leq 100$ 

For $60\%$ of tests $N \leq 100\ 000$ 

## Example

`diagonala.in`
```
8 
5 6 
3 5 
4 7 
6 7 
2 7 
4 8 
2 5 
1 3 
```

`diagonala.out`
```
6
```

## Explanation

Refer to the examples above.