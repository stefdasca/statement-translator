## Task

Given two natural numbers $N$ and $K$. Print the number of permutations of the set $1, 2, \dots, N$ which have $K$ inversions. In a given permutation $P$, the number of inversions is the number of pairs $(i,j)$ such that $i<j$ and $P[i]>P[j]$. For example, for the permutation with $5$ elements: $P=5 \ 2 \ 3 \ 1 \ 4$, the pairs $(i,j)$ in disorder are:
$(1,2) :\ 1<2$ but $5>2$
$(1,3) :\ 1<3$ but $5>3$
$(1,4) :\ 1<4$ but $5>1$
$(1,5) :\ 1<5$ but $5>4$
$(2,4) :\ 2<4$ but $2>1$
$(3,4) :\ 3<4$ but $3>1$
Therefore, this permutation has $6$ inversions. The minimum number of inversions of a permutation of $N$ elements is $0$ (for the permutation $1 \ 2 \ 3 \ \dots \ N-1 \ N$), and the maximum number of inversions is $\frac{N*(N-1)}{2}$ (for the permutation $N \ N-1 \ \dots \ 3 \ 2 \ 1$).

## Input data

The file `perm6.in` contains a single line that contains the values of $N$ and $K$, separated by a space.

## Output data

The file `perm6.out` will contain the number of permutations with $K$ inversions.

## Constraints and clarifications

$1 \leq N \leq 45$\
$0 \leq K \leq \frac{N*(N-1)}{2}$

## Example

`perm6.in`\
`perm6.out`\
$3 \ 0$\
$1$

`perm6.in`\
`perm6.out`\
$4 \ 2$\
$5$