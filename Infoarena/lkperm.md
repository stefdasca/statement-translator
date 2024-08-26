## Task

Aphrodite has decided that the only beautiful permutations are $LK$-permutations. An $LK$-permutation is a permutation that meets the following condition: for any subarray of $L$ consecutive elements, the maximum element of this subarray is within the first $K$ elements of the subarray. Specifically, for a permutation $P$ with $N$ elements, any subarray $P_i, P_{i+1}, \dots, P_{i+L-1}$ $($ $i+L-1 \leq N$ $)$ with $P_k = \max(P_i, P_{i+1}, \dots, P_{i+L-1})$ must satisfy $i \leq k \leq i + K - 1$. Whoever helps Aphrodite find out how many $LK$-permutations with $N$ elements exist will be rewarded with boundless beauty.

## Input data

The input file `lkperm.in` will contain on the first line three natural numbers $N$, $L$, and $K$ separated by a space, as described in the statement.

## Output data

In the output file `lkperm.out`, you will print a single number representing the number of $LK$-permutations with $N$ elements modulo $100 \ 019$.

## Constraints and clarifications

$1 \leq N \leq 100 \ 000$

$1 \leq K \leq L \leq N$

For $40\%$ of the tests, $N \leq 1 \ 000$

For $60\%$ of the tests, $N \leq 10 \ 000$ and $K \leq 1 \ 000$

## Example

`lkperm.in`

`4 3 2`

`lkperm.out`

`10`

## Explanation

All $32$-permutations with $4$ elements are:

`1 4 2 3`, `1 4 3 2`, `2 4 1 3`, `2 4 3 1`, `3 4 1 2`, `3 4 2 1`, `4 1 3 2`, `4 2 3 1`, `4 3 1 2`, `4 3 2 1`.