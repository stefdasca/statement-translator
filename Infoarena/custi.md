## Task 

The prison director has finished rebuilding the fence. Now he's working on the "Dog Cages" project and has assigned *James Blond* to the calculations. However, *James* is in a hurry and won't elaborate on the whole story with the dogs and how the cages should be, but he sent you an email with his problem simplified: given a square matrix of size $N \times N$ that contains only $0$ and $1$, you need to determine the number of all submatrices of size $M \times M$ $(M \leq N)$ that contain only $1$. Thus for a certain test, you need to print $N$ lines, as follows:

Line 1: how many submatrices of $1 \times 1$ with the stated property exist.
$\dots$ 
Line $i$: how many submatrices of $i \times i$ with the stated property exist.
$\dots$ 
Line $N$: how many submatrices of $N \times N$ with the stated property exist.

## Input data 

The file `custi.in` contains: 
- the first line contains the number $N$ 
- the following lines contain the matrix, with elements separated by a space (see example) 

## Output data 

The file `custi.out` has the structure stated above. 

## Constraints

- $1 \leq N \leq 1000$

## Clarifications:

- For $20 \% \text{-} 30 \%$ of the tests $N \leq 100$ 

## Examples:

`custi.in` 
```
5
1 1 1 0 0
1 1 0 1 1
1 1 1 1 1
1 1 1 0 0
1 1 1 0 0
```

`custi.out`
```
18
7
1
0
0
```

## Explanations

18 submatrices of $1 \times 1$ 

7 submatrices of $2 \times 2$ 

1 submatrix of $3 \times 3$ 

0 submatrices of $4 \times 4$ 

0 submatrices of $5 \times 5$ that contain only elements of $1$