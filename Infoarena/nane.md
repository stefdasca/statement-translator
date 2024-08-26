## Nane

Nane from Jiu, being a great algorithmician, challenges you to solve a problem that is too easy for him. Nane gives you $N$ positive numbers and a number $K$. Let $Sp$ be the OR sum (bitwise operation) of the numbers in a subsequence. We call a subsequence special if the $Sp$ of the subsequence has at most $K$ bits of 1 in its binary representation. Nane asks for the number of special subsequences. Two subsequences are different if at least one position in one is not found in the other. Prove to Nane that you are skilled in algorithms and calculate the requested number!

## Input data

The input file `nane.in` will contain the first line which will contain 2 numbers $N$ and $K$, and the second line will contain $N$ numbers.

## Output data

The output file `nane.out` will contain a single number $Nr$ on the first line, representing the number requested by Nane.

## Constraints and clarifications

$1 \leq N \leq 100\ 000$

$1 \leq K \leq 30$

For 20 points

$1 \leq N \leq 50$

For another 30 points

$1 \leq N \leq 1\ 000$

All $N$ numbers will be natural and can be represented in 30 bits

## Example

`nane.in`

`5 2`

`2 14 3 2 10`

`nane.out`

`6`

## Explanation

Example: the subsequence $2\ 6$ has the OR sum $6$; $6$ in binary is $110$ ($2$ bits of 1). This subsequence will be counted if $K \geq 2$.

In the first example, the subsequences are: $(1)$, $(3)$, $(3,4)$, $(4)$, $(4,5)$ and $(5)$.