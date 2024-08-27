## Task

A binary matrix $A$ is given with $R$ rows and $C$ columns. If we randomly choose, with uniform probability, a subset (possibly empty) of cells labeled with $1$, what is the average area of the minimum submatrix that contains all the selected cells?

## Input data

The input file `boundingbox.in` will contain the number of test cases $T$ on its first line. Each test case will follow the format below:  
The first line contains the two numbers, $R$ and $C$, and the next $R$ lines contain $C$ characters each, forming the matrix $A$.

## Output data

The output file `boundingbox.out` will contain $T$ lines, each containing the answer for the corresponding test case.  
The answer will be in the format "$X/Y$", where $X$ and $Y$ are natural numbers that are coprime. In other words, the answer must be in the form of an irreducible fraction.

## Constraints and clarifications

$1 \leq T \leq 1000$

$1 \leq R \cdot C \leq 50$

For $20 \%$ of the tests, the number of cells of type $1$ in each matrix is at most $12$ 

For other $40 \%$ of the tests, the relation $T \leq 100$ holds

## Example

`boundingbox.in`
```
2
2 3
101
010
1 1
0
```

`boundingbox.out`
```
5/2
0/1
```