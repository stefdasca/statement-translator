## Task

Besides his passion for numbers, Zaharel is also very fond of permutations. Today, he decided to study only the permutations $P$ of length $N$ that have an interesting property: they contain $K$ distinct positions $1 < i_1, i_2, \dots, i_K \leq N$ for which $P[i_x] = P[i_x - 1] + 1$. Write a program that determines how many permutations Zaharel will study today.

## Input data

The first line of the input file `perm4.in` contains the two natural numbers $N$ and $K$, separated by a single space.

## Output data

The first line of the output file `perm4.out` will contain the number of permutations. Since the result can be very large, the output should be the remainder of the division of the result by the number $666013$.

## Constraints

$0 \leq K < N \leq 3000$

## Example

`perm4.in`  
`4 1`

`perm4.out`  
`9`

## Explanation

The $9$ permutations are: $1243$, $1342$, $1423$, $2134$, $2314$, $3421$, $3124$, $4231$, $4312$