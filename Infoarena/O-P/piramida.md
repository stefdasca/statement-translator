# The Pyramid

A pyramid of height $N$ has at its base (the base being considered level 1) $N$ non-zero natural numbers. At the next level of the pyramid (level 2), there are $N-1$ numbers, each number at level 2 being obtained using the formula $P_{2,i} = P_{1,i} + P_{1,i+1}$, for $i = 1, \dots, N-1$, and so on. Thus, at level $K$ there are $N-K+1$ numbers, each number at this level being obtained using the formula $P_{k,i} = P_{k-1,i} + P_{k-1,i+1}$ for $i = 1, \dots, N-K+1$. The pyramid is $S$-generating if the number at the last level is $S$.

## Task

For a given value $S$, determine how many maximum height $S$-generating pyramids exist. For example, for $S = 10$, there are 3 such pyramids: The pyramids below are 10-generating but do not have maximum height:

## Input data

The file `piramida.in` contains a single natural number representing the value of $S$.

## Output data

The output file `piramida.out` will contain a single line which will contain a single natural number representing the total number of maximum height $S$-generating pyramids modulo 10000.

## Constraints and clarifications

1 $ \leq S \leq 600\ 000$

## Example

`piramida.in` `piramida.out` 
`1` `1` 
`3` `2` 
`10` `3` 
`20` `7` 
`101` `714`