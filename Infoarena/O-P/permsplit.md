## Permsplit

## Task

A permutation of the set $\{1 \dots N\}$ is given. A subarray is called compact if all the numbers in the subarray form a contiguous interval of natural numbers (example: $2 \ 4 \ 3 \ 5$ is a compact subarray, $1 \ 4 \ 3$ is not a compact subarray). Perform $N-1$ cuts on the initial permutation so that at each step the obtained subarrays are compact, or state if this is impossible.

## Input data

The input file `permsplit.in` contains on the first line the number $N$ and on the second line a permutation of $N$ elements.

## Output data

The output file `permsplit.out` will contain on the first line $N-1$ numbers, the $i$-th number representing the position of the element in the permutation after which the cut is made. If there is no solution, print $-1$.

## Constraints and clarifications

$2 \leq N \leq 1\ 000\ 000$

## Example

`permsplit.in`

```
5
1 5 3 4 2
```

`permsplit.out`

```
1 2 4 3
```

## Explanation

( $1 \ 5 \ 3 \ 4 \ 2$ )  
( $1$ ) ( $5 \ 3 \ 4 \ 2$ )  
( $1$ ) ( $5$ ) ( $3 \ 4 \ 2$ )  
( $1$ ) ( $5$ ) ( $3 \ 4$ ) ( $2$ )  
( $1$ ) ( $5$ ) ( $3$ ) ( $4$ ) ( $2$ )