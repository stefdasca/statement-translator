## Task

A sequence of numbers is an i-sequence of length $N$ if it has $N$ elements and all its elements $A_1, A_2, \dots, A_N$ are non-negative integers less than or equal to $2\,000\,000\,000$. Let's consider two i-sequences of length $N$: $A$ and $X$. The result of multiplying the two i-sequences is an integer $R = A_1 \cdot X_1 + A_2 \cdot X_2 + \dots + A_N \cdot X_N$. Given the i-sequence $A$ and the integers $P$ and $B$, solve the equation $A \cdot X = B \pmod{P}$.

## Input data

The first line of the input file `isecv.in` contains the integers $N$, $P$, and $B$, separated by a space. $N$ is the length of the i-sequence $A$. The second line contains the elements of the i-sequence $A$, separated by a space: $A_1~A_2~\dots~A_N$.

## Output data

The first line of the output file `isecv.out` will contain the string "DA", if there is at least one i-sequence $X$ that is a solution to the equation, or the string "NU", otherwise. If the answer is "DA", the second line will contain the elements of the i-sequence $X$, separated by a space: $X_1~X_2~\dots~X_N$.

## Constraints and clarifications

$1 \leq N \leq 1000$  
$1 \leq P \leq 10\,000$  
$0 \leq B \leq P-1$

## Examples

`isecv.in`  
`2 7 4`  
`7 3`

`isecv.out`  
`DA`  
`0 6`

`isecv.in`  
`3 10 1`  
`2 4 6`

`isecv.out`  
`NU`