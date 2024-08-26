## Task

You are given an $N \times M$ matrix with values ranging between $0$ and $10^9$. Determine how many chessboard squares exist. A chessboard square is a square submatrix of the given matrix that has the property that diagonally adjacent elements are equal while horizontally or vertically adjacent elements are different.

## Input data

The input file `sah3.in` will contain on the first line 2 natural numbers $N$ and $M$. The next $N$ lines will each contain $M$ numbers separated by a space. This is the given matrix.

## Output data

The output file `sah3.out` will contain a single natural number representing the answer.

## Constraints

$1 \leq N$  
$M \leq 1000$ 

## Example

`sah3.in`
```
4 5
0 1 0 1 0
1 0 1 0 1
0 1 0 1 0
1 1 1 0 1
```

`sah3.out`
```
34
```

