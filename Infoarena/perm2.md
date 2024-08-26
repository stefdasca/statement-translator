Permutations II

Consider the set $A$ formed from the elements $1, 2, 3 \dots N (1 \leq N \leq 20\ 000)$. A permutation $P$ is a bijective function defined on the set $A$, with values in $A$. (i.e., it uniquely associates each element from $A$ with a unique element also from $A$). An example of such a permutation is illustrated in the table below:

$$i \ \ \ \ \ \ 1 \ \ 2 \ \ 3 \ \ 4$$
$$P(i) \ \ 2 \ \ 3 \ \ 4 \ \ 1$$

We define the permutation $P^k$ as follows:

$P^k(i) = P(i)$, when $k=1$

$P(P^{k-1} (i))$, for $k > 1$

The table below illustrates $P^1$ and $P^2$:

$$i \ \ \ 1 \ \ 2 \ \ 3 \ \ 4$$
$$P^1(i) \ \ 2 \ \ 3 \ \ 4 \ \ 1$$
$$P^2(i) \ \ 3 \ \ 4 \ \ 1 \ \ 2$$

## Task

Given $N$ and a permutation $P$. Find the smallest strictly positive natural number $K$ such that for any $1 \leq i \leq N$ we have $P^k(i) = i$ (in other words, $P^k$ should be the identity permutation).

## Input data

The file `perm2.in` will contain on the first line the integer $N$. The next line contains $N$ distinct natural numbers, each in the range $1 \dots N$.

## Output data

On the first line of the file `perm2.out` the number $K$ that meets the conditions will be written.

## Constraints and clarifications

For the provided tests:
$1 \leq K \leq 100\ 000$

## Examples

`perm2.in`  `perm2.out`
`6 1 2 3 4 5 6`  `1`
`4 2 3 4 1`  `4`
`8 1 5 2 3 4 8 6 7`  `12`