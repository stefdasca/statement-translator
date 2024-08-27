## Task

Flavia is interested in strings of $N$ $a$s and $b$s where there are no three consecutive identical characters. For example, $abaaba$ fits this definition, but $abaaa$ does not. Strings that satisfy this definition will be called interesting. Flavia cares about these strings from the perspective of lexicographical order. For two strings $A$ and $B$ of length $N$, we say that $A$ is smaller than $B$ in lexicographical order if and only if, for some index $i$ where $1 \leq i \leq N$, we have $A[1] = B[1], \dots, A[i−1] = B[i−1]$ and $A[i] < B[i]$. For example, $aba$ is greater than $aab$ in lexicographical order but smaller than $baa$ in lexicographical order. Flavia now wants to solve two tasks:
1. Given an interesting string $S$ of length $N$, find its lexicographical order among all interesting strings of length $N$, modulo $10^9 + 7$
2. Given a number $N$ and a number $K$, find the $K$-th interesting string of length $N$ in lexicographical order. Can you help her?

## Input data

The first line of the input file contains the number $P$, the index of the task in the test. The second line of the input will contain the number $N$. If $P=1$, the third line will contain the interesting string $S$. If $P=2$, the third line will contain the number $K$.

## Output data

If $P=1$, the output file will contain an integer, the lexicographical order of the interesting string $S$ of length $N$, modulo $10^9 + 7$. If $P=2$, the output file will contain the $K$-th interesting string of length $N$ in lexicographical order.

## Constraints and clarifications

For tests worth 20 points,
$P=1$ and $N \leq 20$

For other tests worth 30 points,
$P=1$ and $N \leq 1\ 000\ 000$

For other tests worth 20 points,
$P=2$, $N \leq 100$ and $K \leq 1\ 000\ 000$

For other tests worth 30 points,
$P=2$, $N \leq 1\ 000\ 000$ and $K \leq 1\ 000\ 000\ 000$

## Example

`cntlex.in`
```
1
3
aba
```

`cntlex.out`
```
2
```

`cntlex.in`
```
2
3
5
```

`cntlex.out`
```
bab
```

## Explanation

The interesting strings of length $3$ in lexicographical order are $aab, aba, abb, baa, bab, bba$. Thus $aba$ is the 2nd in lexicographical order, and the 5th is $bab$