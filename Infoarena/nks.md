## Task

Construct a binary matrix (with elements $0$ and $1$) having $M$ rows and $N$ columns, such that every submatrix of $P$ rows and $Q$ columns contains exactly $S$ elements equal to $1$ (the rest being $0$).

## Input data

The input file `nks.in` contains on the first line $5$ integers, separated by a space: $M, N, P, Q,$ and $S$.

## Output data

In the output file `nks.out` you will print $M$ rows, each of them containing $N$ characters from the set $\{0,1\}$, representing the constructed matrix (from the first to the last row). The characters on the same row will not be separated by spaces.

## Constraints and clarifications

$1 \leq M \leq 1000$  
$1 \leq N \leq 1000$  
$1 \leq P \leq M$  
$1 \leq Q \leq N$  
$0 \leq S \leq P \times Q$  

This problem has tests divided into $2$ groups, worth $30$ and $70$ points, respectively.

## Example

`nks.in`  
`7 5 2 2 2`

`nks.out`  
`10101`  
`01010`  
`10101`  
`01010`  
`10101`  
`01010`  
`10101`