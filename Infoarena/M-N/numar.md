# Number

Consider a natural $number$ $n$.

## Task

Determine all the ways in which the given $number$ can be written as a $sum$ of (at least two) consecutive $integers$.

## Input data

The input file `numar.in` contains the natural $number$ $n$.

## Output data

The output file `numar.out` will contain as many $lines$ as there are ways of $decomposition$. On each $line$, two $integers$ $p$ and $nr$ will be written, where $p$ represents the first $term$ in the sum, and $nr$ represents the $number$ of $terms$.

## Constraints and clarifications

$3 \leq n \leq 1\ 000\ 000\ 000$

The $decompositions$ will be displayed in $descending$ $order$ by the first $number$ in the $sequence$.

## Example

`numar.in`

`25`

`numar.out`

`12 2`

`3 5`

`-2 10`

`-11 25`

`-24 50`

## Explanations

$12 + 13 = 25$

$3 + 4 + 5 + 6 + 7 = 25$

$-2 -1 + 0 + 1 + 2 + 3 + 4 + 5 + 6 + 7 = 25$

$-11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 + 0 + 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 = 25$

Similarly, in the last $case$, the $sum$ of $50$ consecutive $numbers$ starting with $-24$ is $25$.