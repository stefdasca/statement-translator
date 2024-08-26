# Numbers 2

Danut learned about prime numbers in his math class at school. Now he wants to develop an efficient algorithm to check for primality. Given a natural number $P$, he knows that $P$ is not prime if there exist natural numbers $A$ and $B$ such that $A$ raised to the power of $B$ equals $P$ and $B$ is greater than $1$. Danut would like to know the smallest $A$ for which there exists a number $B$ such that ${A}^{B} = P$.

## Task

Given the number $P$, find $A$ and $B$ such that ${A}^{B} = P$.

## Input Data

In the file `numere2.in`, the first line contains the number $P$ without any spaces between the digits.

## Output Data

The output file `numere2.out` will contain the number $A$ on the first line, and the number $B$ on the second line. The numbers will be printed without any spaces between the digits.

## Constraints and Clarifications

$0 < P < 10^{100}$ 
(that is, $P$ has at most 100 digits)

for 50% of the tests

$0 < P < 10^{9}$ 

$A$ must be minimal

$B$ can be equal to $1$

$A$, $B$, $P$ are positive integers

## Examples

`numere2.in`
`numere2.out`
81
3
4

`numere2.in`
`numere2.out`
17
17
1

`numere2.in`
`numere2.out`
9904578032905937
17
13