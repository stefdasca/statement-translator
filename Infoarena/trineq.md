## Task

In this problem, you need to count the number of ways to label the edges of a complete graph with $N$ nodes with lengths from the set $\{0, 1, 2\}$ such that any triplet of nodes out of the $N$ nodes satisfies the triangle inequality: the sum of the lengths of the two shortest edges is greater than or equal to the length of the longest edge.

## Input data

The input file `trineq.in` will contain on the first line the number of tests $T$. The following $T$ lines will contain a number, $N$, as described above.

## Output data

The output file `trineq.out` will contain $T$ lines, each containing the answer to the problem's task modulo $1000000007$.

## Constraints

$1 \leq T \leq 2000$

$2 \leq N \leq 2000$

## Example

`trineq.in`

`1`

`3`

`trineq.out`

`15`