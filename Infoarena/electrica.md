## Task 

Gabriela works at Electrica S.A., where she is in charge of billboards. She is currently working on a rather unusual billboard. The billboard consists of many bulbs arranged in an $N$ by $M$ matrix. Initially, all bulbs are off, and Gabriela has to turn on some of them. The problem is that the only allowed operation is to choose an $L$ by $L$ submatrix and change the state of all bulbs in that submatrix. Gabriela wants to know the minimum number of operations needed to bring the bulbs to the required final state.

## Input data

The input file `electrica.in` will contain on the first line the numbers $N$, $M$ and $L$. The following $N$ lines will each contain $M$ numbers 0 or 1 (not separated by spaces) representing the final state of the bulbs (0 for off and 1 for on).

## Output data

The output file `electrica.out` will contain a single line containing the minimum number of operations needed to bring the bulbs to the final state, or the number -1 if this is not possible.

## Constraints and clarifications

$1 \leq L \leq N$

$M \leq 1000$

For 40% of the tests

$1 \leq N, M \leq 100$

For 60% of the tests

$1 \leq N, M \leq 500$

Note: The submatrix represents the two-dimensional extension of the subarray and not the subsequence.

## Example

`electrica.in`
```
4 4 3
1110
1001
1001
0111
```

`electrica.out`
```
2
```

## Explanation

Gabriela chooses the submatrices with the top-left corner at points $1, 1$ and $2, 2$.