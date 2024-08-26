# Pal2

Given a string $S$ of $N$ lowercase Latin letters. Let $P$ be the set of all palindromes. The task is to calculate: where $F(x)$ is the number of occurrences of the string $x$ in the string $S$, and $L(x)$ is the length of the string $x$.

## Input data

The input file `pal2.in` contains the string $S$.

## Output data

The output file `pal2.out` will contain on the first line the required sum.

## Constraints

$1 \leq N \leq 100\ 000$

## Example

`pal2.in`
`aaba`

`pal2.out`
`15`

## Explanation

$F("a") 2 \times L("a") + F("b") 2 \times L("b") + F("aa") 2 \times L("aa") + F("aba") 2 \times L("aba") = 3 2 \times 1 + 1 2 \times 1 + 1 2 \times 2 + 1 2 \times 3 = 15$.