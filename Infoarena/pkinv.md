## Task

Determine the number of permutations with $N$ elements that contain exactly $K$ inversions, modulo $41143$ (i.e., the remainder of the number of permutations with $N$ elements and $K$ inversions when divided by $41143$).

## Input data

The first (and only) line of the input file `pkinv.in` contains two integers separated by a space: $N$ and $K$.

## Output data

The first (and only) line of the output file `pkinv.out` will contain the number $X$, representing the number of permutations with $N$ elements and exactly $K$ inversions, modulo $41143$.

## Constraints and clarifications

$1 \leq N \leq 1\ 000\ 000\ 000$  
$0 \leq K \leq \min{100, \frac{N*(N-1)}{2}}$

## Example

`pkinv.in`  
`8 6`  

`pkinv.out`  
`602`