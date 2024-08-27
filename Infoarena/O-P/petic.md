## Task

You are given a binary matrix with rows from $0$ to $nrLin - 1$ and columns from $0$ to $nrCol - 1$, and $Q$ independent queries of the form $X_1 Y_1 X_2 Y_2$: "Suppose we change all bits of $1$ in the submatrix with the top-left corner at row $X_1$ and column $Y_1$ and the bottom-right corner at row $X_2$ and column $Y_2$ to $0$. What is the total number of rows and columns of the new matrix that still have at least one bit $1$?"

## Input data

The input file `petic.in` contains, on the first line, the numbers $nrLin$, $nrCol$, and $Q$. The next $nrLin$ lines contain one string of $nrCol$ bits each. The next $Q$ lines contain four numbers $X_1 Y_1 X_2 Y_2$ each.

## Output data

The output file `petic.out` contains the answers to the $Q$ queries, in order, one number per line.

## Constraints and clarifications

It is recommended to parse the input and output!

$0 \leq X_1 \leq X_2 < nrLin$  
$0 \leq Y_1 \leq Y_2 < nrCol$  
$nrLin \leq nrCol$  
$1 \leq Q$

Scoring

Subtask for $3$ points  
$nrCol \leq 100$  
$Q \leq 1\ 000$

Subtask for $11$ points  
$nrCol \leq 400$  
$Q \leq 100\ 000$

Subtask for $23$ points  
All submatrices in the queries are square $(X_2 - X_1 = Y_2 - Y_1)$  
$nrCol \leq 1\ 000$  
$Q \leq 1\ 000\ 000$

Subtask for $24$ points  
All submatrices in the queries are square $(X_2 - X_1 = Y_2 - Y_1)$  
$nrCol \leq 1\ 800$  
$Q \leq 1\ 500\ 000$

Subtask for $26$ points  
$Q$, $nrLin * nrCol \leq 400\ 000$

Subtask for $13$ points  
$nrLin * nrCol \leq 3\ 240\ 000$  
$Q \leq 1\ 500\ 000$

## Example

`petic.in` 
```
2 2 5 
1 1
0 1 
0 0 1 1
0 0 0 0 
1 0 1 0 
1 1 1 1 
0 3
4 4 3 2 
3 8
100 1 1 
```

`petic.out` 
```
0
1 
1 
1 
1 
```