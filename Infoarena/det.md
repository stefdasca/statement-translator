## Task

Given a matrix $A$ of size $N \times N$, calculate: $D = |I_N + A + A^2 + \dots + A^K|$, where $|M|$ is the determinant of the matrix $M$, and $I_N$ is the identity matrix of size $N$. To simplify display and calculations, you will need to compute the number $D$ modulo $9901$.

## Input data

The input file `det.in` contains the numbers $N$ and $K$ on the first line, followed by $N$ lines with $N$ elements on each line, representing the elements of the matrix $A$. All numbers on the same line will be separated by a space.

## Output data

The output file `det.out` will contain a single number, the value of the determinant of the sum modulo $9901$.

## Constraints

$1 \leq N \leq 50$  
$1 \leq K \leq 1\ 000\ 000\ 000$  
$1 \leq A[i,j] \leq 10\ 000$  

## Example

`det.in`
```
3 9
1 2 3
4 5 6
7 8 9
```

`det.out`
```
2222
```