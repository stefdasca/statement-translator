## Task

Given a binary matrix $A$ with $N$ rows and $M$ columns. A "right-down" path is defined as any sequence of cells $(x_0, y_0), (x_1, y_1) \dots (x_{k - 1}, y_{k - 1})$ with the property that for any $1 \leq i \leq k - 1$, $x(i) = x(i - 1) + 1$ and $y(i) = y(i - 1)$ or $x(i) = x(i - 1)$ and $y(i) = y(i - 1) + 1$. How many "right-down" paths exist that start in the top-left corner, end in the bottom-right corner, and contain only cells of type $1$? Just kidding. This problem is too well known. So well-known that throughout history, the Committees have developed remarkable precision in composing such types of tests. Specifically, given a natural number $C$, the Committee can produce a reasonably sized matrix for which the answer to the above question is exactly $C$. Spoiler alert, that's what you have to do as well!

## Input data

The input file `nop.in` will contain the number of tests $T$. It will be followed by $T$ lines, each containing a natural number $C$, the number of required paths for the respective test.

## Output data

The output file `nop.out` will contain the solution matrices for each of the $T$ tests. For each test, the number of rows $N$ and the number of columns $M$ of the matrix will be printed. $N$ lines of $M$ characters each, without spaces, will follow. Each character will be either $0$ or $1$.

## Restrictions and clarifications

The number of cells $(N \times M)$ of each matrix you display must be at most $1600$.  
$1 \leq T \leq 500$  
$1 \leq C_i \leq 66\ 666\ 666$  
For tests worth 10 points, $C_i \leq 800$  
For tests worth 30 points, $C_i \leq 50\ 000$  
For tests worth 50 points, $C_i \leq 1\ 000\ 000$  

## Example

`nop.in`  
$2$  
$1$  
$2$  

`nop.out`  
$1$ $1$  
$1$  
$3$ $3$  
$111$  
$101$  
$111$