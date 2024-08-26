# Decompositions

A decomposition of a natural number $N$ is defined as an increasing sequence (not necessarily strictly) of natural numbers whose product is $N$.

## Task

Given a natural number $N$ and a natural number $K$, calculate the number of decompositions of $N$ as well as the $K$-th decomposition in lexicographic order.

## Input data

The first line of the input file `desc.in` contains two integers $N$ and $K$ as described above.

## Output data

In the file `desc.out`, print on the first line $X$, the number of decompositions of $N$, and on the second line, print the sequence that represents the $K$-th decomposition, with the numbers separated by a space.

## Constraints and clarifications

$1 \leq N \leq 10^{12}$

$1 \leq K \leq 10^{9}$

A sequence $A_1, A_2, \dots, A_s$ is lexicographically smaller than another sequence $B_1, B_2, \dots, B_t$ if there exists $i \leq \min(s, t)$ such that $A_1 = B_1, A_2 = B_2, \dots, A_{i-1} = B_{i-1}$ and $A_i < B_i$.

For each test, 4 points are awarded for correctly finding the number of decompositions, and 6 points for finding the $K$-th decomposition.

## Example

`desc.in`

`36 5`

`desc.out` 

`9` 

`3 3 4` 

## Explanations

The 9 decompositions are (in lexicographic order):
$2\ 2\ 3\ 3$,
$2\ 2\ 9$,
$2\ 3\ 6$,
$2\ 18$,
$3\ 3\ 4$,
$3\ 12$,
$4\ 9$,
$6\ 6$,
$36$