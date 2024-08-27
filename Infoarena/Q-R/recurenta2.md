# Recurenta2

Given the sequence $X$ defined by the recurrence $X_i = A \cdot X_{i-1} + B \cdot X_{i-2} + C$, you are asked to calculate the sum $X_1 \cdot 1 + X_2 \cdot 2 + X_3 \cdot 3 + \dots + X_N \cdot N$. 

## Input data

The input file `recurenta2.in` will contain a single line with 6 integers $A$, $B$, $C$, $X_1$, $X_2$, and $N$, having the meanings as described in the statement. 

## Output data

The output file `recurenta2.out` will contain a single integer representing the value of the sum calculated modulo $666013$. 

## Constraints and clarifications

$1 \leq A, B, C \leq 10^6$  
$0 \leq X_1, X_2 < 666\ 012$  
$2 \leq N \leq 10^9$  

## Example

`recurenta2.in`  
`3 2 4 5 6 10`  

`recurenta2.out`  
`434185`