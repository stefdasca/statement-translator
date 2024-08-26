## Task

Determine how many unlabeled rooted trees exist that satisfy the following properties: they have $N$ nodes, and the degree of each internal node is equal to $K$ modulo $M$. Two trees $T_1$ and $T_2$ are considered equal if there is a bijection between their nodes such that the root of $T_1$ corresponds to the root of $T_2$, and there is an edge between a pair of nodes in $T_1$ if and only if there is an edge between the corresponding pair of nodes in $T_2$.

## Input data

The input file `arbori.in` contains on the first line the numbers $N$, $M$, $K$ separated by spaces.

## Output data

The output file `arbori.out` will contain the required number.

## Constraints and clarifications

$1 \leq N \leq 90$  
$2 \leq M \leq 10$  
$0 \leq K < M$  
For 60% of the tests $N \leq 40$  
It is guaranteed that the result fits into a 64-bit signed integer  
In a rooted tree, any node that has at least one child is an internal node

## Example

`arbori.in`
`
5 2 0
`

`arbori.out`
`
3
`

## Explanation

The 3 trees are:

~[trees.png]