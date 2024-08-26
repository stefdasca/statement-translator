Fpwl

For a sequence of numbers $a_1, a_2, \dots, a_N$, we define its Polish sequence as the sequence $s_1, s_2, \dots, s_{N-1}$ of symbols $<$, $>$ or $=$. The symbol $s_i$ of the sequence represents the relationship between $a_i$ and $a_{i+1}$. For example, the Polish sequence of the sequence $2, 4, 3, 3, 5, 3$ is $<, >, =, <, >$. We say that the sequence $b_1, b_2, \dots, b_{N+1}$ with the Polish sequence $s_1, s_2, \dots, s_N$ achieves another Polish sequence $s'_1, s'_2, \dots, s'_K$ if for any $i$ from $1$ to $N$ $s_i = s'_{(i-1) \mod K + 1}$. In other words, the sequence $s_1, s_2, \dots, s_N$ can be obtained from the sequence $s'_1, s'_2, \dots, s'_K$ by repeating this sequence several times and then removing the corresponding suffix. For example, the sequence $2, 4, 3, 3, 5, 3$ achieves the following Polish sequences: $<, >, =$ $<, >, =, <, >$ $<, >, =, <, >, <, <, =$ $<, >, =, <, >, =, >, >$ and many others. You are given a sequence of numbers $a_1, a_2, \dots, a_N$ and a Polish sequence $s_1, s_2, \dots, s_K$. You need to find the longest subsequence of $a$ $a_{i1}, a_{i2}, \dots, a_{iM}$ $(1 \leq i1 \leq i2 \leq \dots \leq iM)$ that achieves the Polish sequence $s$.

## Input data

The first line of the file `fpwl.in` contains 2 integers $N$ and $K$ separated by a single space representing the length of the sequence $(a_i)$, respectively $(s_j)$. The second line contains $N$ integers $a_1, a_2, \dots, a_N$ separated by a space representing the sequence $a$. The third and final line contains $K$ symbols in the form $<, >$ or $=$ representing the Polish sequence $s$.

## Output data

The output file `fpwl.out` must contain 2 lines. The first line must contain $M$, the length of the longest subsequence of $a$ that achieves the Polish sequence $s$. The second and final line must contain the $M$ elements $a_{i1}, a_{i2}, \dots, a_{iM}$ representing such a subsequence.

## Constraints

$1 \leq N, K \leq 500.000$

$1 \leq a_i \leq 1.000.000$

## Example

`fpwl.in`
```
7 3
2 4 3 1 3 5 3
< > =
```
`fpwl.out`
```
6
2 4 3 3 5 3
```