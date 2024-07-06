By concatenating two natural numbers $A$ and $B$, the natural numbers $AB$ and $BA$ can be obtained. For example, if $A = 8$ and $B = 8$, the number $88$ can be obtained by concatenation, and if $A = 7$ and $B = 17$, the numbers $717$ and $177$ can be obtained by concatenation.

# Task

Write a program that solves the following two requirements:

1. For a given non-zero natural number $A$, calculate $P1$, the number of distinct natural numbers $X$, where $1 \leq X \leq 10 * A$, such that $X$ concatenated with $A$ or $A$ concatenated with $X$ is a palindrome.
2. Given the natural number $N$ and a sequence of $N$ natural numbers $v[1], v[2], \dots, v[N]$, calculate $P2$, the number of distinct palindromic numbers that can be obtained by concatenating the numbers in the pairs $(v[i], v[j])$, where $1 \leq i \leq N$ and $1 \leq j \leq N$.

# Input data

The input file `cat2pal.in` contains on the first line the natural number $C$, representing the task that needs to be solved ($1$ or $2$). If $C = 1$, then the second line contains the natural number $A$. If $C = 2$, then the second line contains the natural number $N$ and the third line contains $N$ natural numbers separated by spaces, representing the sequence $v$.

# Output data

The output file `cat2pal.out` will contain a single line on which a single natural number will be written, representing the result for the task $C$ from the input file.

# Constraints and clarifications

* $1 \leq A \lt 100 \ 000 \ 000$
* $1 \leq N \leq 10 \ 000$
* $0 \leq v[i] \lt 100 \ 000$; for any $i = 1 \dots N$
* For the case $C = 2$, pairs $(v[i], v[i])$ should also be considered, i.e., the concatenation of an element with itself.
* For tests worth $20$ points: $C = 1$ and $A < 100 \ 000$
* For other tests worth $30$ points: $C = 1$ and there are no additional constraints.
* For tests worth $15$ points: $C = 2$ and $N \leq 1 \ 000$
* For tests worth $35$ points: $C = 2$ and there are no additional constraints.

# Example 1

`cat2pal.in`
```
1 
2
```

`cat2pal.out`
```
3
```

## Explanation

$C = 1$, $A = 2$, the numbers $X$ which, when concatenated with $A$, produce palindromic numbers are $2$, $12$, and $20$, so $P1 = 3$.

# Example 2

`cat2pal.in`
```
2
3
2 12 21
```

`cat2pal.out`
```
4
```

## Explanation

$C = 2$, $N = 3$, $v = {2, 12, 21}$, the distinct palindromic numbers that can be obtained are $22$, $212$, $1221$, $2112$, so $P2 = 4$.