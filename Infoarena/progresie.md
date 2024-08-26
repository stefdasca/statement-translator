# Progression

We all know that Petrica did not do well at the National Dynamic Programming Olympiad, so he switched to mathematics, specifically the field of arithmetic progressions. An array $V$ with $N$ elements is an arithmetic progression if and only if there exists an $R$ such that $R = V[i + 1] - V[i]$ for any $1 \leq i \leq N - 1$. Now that Petrica has figured out how progressions work, he wants to play a game. So he takes the following infinite array: $1, 3, 4, 7, 8, 9, \dots$. This array is obtained by the following rule: keep one element: $1$, skip one element: $2$, keep two elements: $3, 4$, skip two elements: $5, 6$, keep three elements: $7, 8, 9$, skip three elements: $10, 11, 12$, $\dots$ Thus, Petrica wonders what is the smallest number $V$ in this infinite array such that there exists an arithmetic progression with the first term $V$, of length $N$ and with the ratio $R$, whose elements are all found in the infinite array. You need to help the two boys.

## Task

## Input data

The input file progresie.in contains on the first line a natural number $T$ representing the number of tests. The next $T$ lines contain two natural numbers $N$ and $R$, with the significance from the statement.

## Output data

The output file progresie.out will contain $T$ lines, each line containing the value $V$ determined for the $i$-th test. 

## Constraints and clarifications

$T = 11$

$1 \leq N \leq 30$

$1 \leq R \leq 10^{8}$

## Example

`progresie.in`
```
2
2 1
3 4
```

`progresie.out`
```
3
73
```

## Explanation

For the first test, we need to find a progression with $2$ elements and with the ratio $1$. The progression is $3, 4$. 

For the second test, we need to find a progression with $3$ elements and with the ratio $4$. The progression is $73, 77, 81$.