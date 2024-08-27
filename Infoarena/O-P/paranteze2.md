# Paranteze2

A string $S$ of length $N$, containing characters $'('$ and $')'$, is given. Calculate and print how many of its subarrays represent valid parenthesizations. A valid parenthesization is named as follows: 

- A string $T$ of parentheses that can be formed as: $T = '()'$
- Or $T = '(' + t + ')'$, where $t$ is a valid parenthesization
- Or $T = t_1 + t_2 + \dots + t_n$, where $t_1, t_2, \dots, t_n$ are valid parenthesizations. 

## Input data

The input file `paranteze2.in` will contain on the first and only line the string $S$.

## Output data

The output file `paranteze2.out$ will contain the number of subarrays that constitute valid parenthesizations.

## Constraints and clarifications

$1 \leq N \leq 1\ 000\ 000$

An subarray of the string $S$ is understood as a compact interval of the form $[i..j]$ with $1 \leq i \leq j \leq N$.

## Example

`paranteze2.in`
`()(())`

`paranteze2.out`
`4`

## Explanation

The 4 subarrays are $1-2$, $3-6$, $4-5$, and $1-6$