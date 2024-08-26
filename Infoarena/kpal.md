## Task

Consider $K$ natural numbers: $b_1, b_2, \dots, b_K$. We say that a number $X$ in base $10$ is a $K$-palindrome if there is at least one index $i$, $1 \leq i \leq K$, such that the number $X$ written in base $b_i$ is a palindrome. A number is a palindrome if it reads the same from left to right and from right to left. The task is to answer $Q$ questions of the type: $L \ U :$ how many numbers within the interval $[L, U]$ are $K$-palindromes?

## Input data

The first line of the input file `kpal.in` contains $K$. The second line contains $K$ natural numbers $b_1, b_2, \dots, b_K$ separated by spaces. The third line contains the number $Q$. The following $Q$ lines contain two natural numbers $L$ and $U$ separated by a space, representing the $Q$ questions.

## Output data

The output file `kpal.out` will contain $Q$ lines. On line $i$ will contain the answer to question $i$.

## Constraints and clarifications

$1 \leq K \leq 13$ 

$2 \leq b_i \leq 100\ 000$, for any $i$, $1 \leq i \leq K$ 

$1 \leq Q \leq 100\ 000$ 

$0 \leq L \leq U \leq 100\ 000\ 000$ 

Numbers $L$ and $U$ are considered in base $10$.

Considered palindromes can have any parity 

## Example

`kpal.in`
```
2
2 3
2
0 10
11 15
```

`kpal.out`
```
10
2
```