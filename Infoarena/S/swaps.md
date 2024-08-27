Swaps

We define the function $f(N, P, A, B)$ as the probability that the number $A$ will reach position $B$ after performing $P$ random swaps of two numbers on the identical permutation of length $N$. For example, $f(3, 1, 1, 2)$ is equal to $0.(2)$, because we have 9 possibilities to choose the swapped positions $(1, 1)$, $(1, 2)$, $(1, 3)$, $(2, 1)$, $(2, 2)$, $(2, 3)$, $(3, 1)$, $(3, 2)$, $(3, 3)$, of which only two produce the desired result ($(1, 2)$ and $(2, 1)$). Given $T$ tests of the form $N P A B$, we need to calculate $f(N, P, A, B)$ for each of them.

## Input data

The input file `swaps.in` will contain on the first line the natural number $T$. The next $T$ lines will be of the form $N P A B$, with the meaning described in the statement.

## Output data

The output file `swaps.out` will contain the answers to these $T$ queries, on separate lines.

## Constraints and clarifications

$1 \leq N \leq 1\ 000\ 000$

$1 \leq A, B \leq N$

$1 \leq P \leq 1\ 000\ 000$

$1 \leq T \leq 100\ 000$

The results will be displayed with a precision of $10^{-9}$.

$A$ and $B$ can also be equal. If the chosen positions for swapping are identical, the permutation will remain the same for the next step.

For 20% of the tests,

$T \leq 20$,

$N \leq 100$, and

$P \leq 100$.

For another 20% of the tests,

$T \leq 20$ and

$P \leq 100\ 000$.

## Example

`swaps.in`

```
3
6 3 1 4
6 4 1 1
3 2 3 3
```

`swaps.out`

```
0.117283951
0.331275720
0.320987654
```