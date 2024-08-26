# P-array

A sequence of natural numbers $a_1$, $a_2$, $\dots$, $a_k$ $(k \geq 2)$ is called a $p$-sequence if it meets the condition $(a_i - a_{i-1})*(a_i - a_{i-2}) < 0$ for $2 < i \leq k$. A $subsequence$ of a sequence that meets the $p$-sequence condition is called a $p$-$subsequence$. Given a sequence of $N$ natural numbers $P_1$, $P_2$, $\dots$, $P_N$, determine how many $p$-subsequences it contains.

## Task

## Input data

The input file `psir.in` will contain the natural number $N$ on the first line. The next line will contain $N$ natural numbers representing the elements $P_1$, $P_2$, $\dots$, $P_N$.

## Output data

The output file `psir.out` will contain the number of $p$-$subsequences$, $modulo \ 2^{32}$.

## Constraints

$1 \leq N \leq 2000$

$1 \leq P_i \leq 2\ 000\ 000\ 000$

## Example

`psir.in`
4
1 1 5 2

`psir.out`
8

## Explanation

The 8 $p$-$subsequences$ are: $$(P_1, P_2) = (1, 1)$$ $$(P_1, P_3) = (1, 5)$$ $$(P_1, P_4) = (1, 2)$$ $$(P_1, P_3, P_4) = (1, 5, 2)$$ $$(P_2, P_3) = (1, 5)$$ $$(P_2, P_4) = (1, 2)$$ $$(P_2, P_3, P_4) = (1, 5, 2)$$ $$(P_3, P_4) = (5, 2)$$