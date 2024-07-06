Given the natural numbers $N$ and $K$, as well as a sequence $a_1$, $a_2$, $\dots$, $a_N$ of non-zero natural numbers. From the sequence, a single subarray (possibly empty) $a_i$, $a_{i + 1}$, $\dots$, $a_j$ can be removed so that the remaining elements are $a_1$, $a_2$, $\dots$, $a_{i - 1}$, $a_{j + 1}$, $\dots$, $a_N$. For example, from the sequence $a$ = [$1$, $2$, $3$, $4$, $5$, $7$] the subarray $3$, $4$, $5$ can be removed and $1$, $2$, $7$ remain; or the empty subarray can be removed and the initial sequence $1$, $2$, $3$, $4$, $5$, $7$ remains; or $1$, $2$, $3$, $4$ can be removed and the sequence $5$, $7$ remains.

After removing the subarray, the remaining elements form an inno sequence if, by applying the & (bitwise AND) operation on them, the result is a number that has at least $K$ bits of $1$ in base $2$. For example, if $a$ = ($1$, $2$, $3$, $4$, $5$, $7$) and $K = 2$, then by removing the subarray $1$, $2$, $3$, $4$, the elements $5$, $7$ remain, and $5$ & $7$ = $5$, which has $2$ bits of $1$ in base $2$. But if the subarray $3$, $4$, $5$ is removed, then the elements $1$, $2$, $7$ remain, and $1$ & $2$ & $7$ = $0$, so it is not an inno sequence.

# Task

Determine in how many ways a subarray can be removed so that the remaining elements form an inno sequence.

# Input data

The input file `inno.in` contains on the first line the natural numbers $N$ and $K$. The second line contains $N$ natural numbers representing the elements of the sequence, separated by a space.

# Output data

The output file `inno.out` will contain on the first line a single natural number representing the number of ways to remove a subarray so that the remaining sequence is inno.

# Constraints and clarifications

* $3 \leq N \leq 200\ 000$
* $1 \leq K \leq 29$
* $0 \leq a_i \leq 2^{31} - 1$
* `&` is the bitwise AND operator. If $x$ and $y$ are binary values, then the expression $x$ & $y$ equals $1$ if and only if $x = 1$ and $y = 1$. Therefore, $1$ & $1$ = $1$, $0$ & $1$ = $0$, $1$ & $0$ = $0$, $0$ & $0$ = $0$. If $a$ and $b$ are natural numbers, then the expression $a$ & $b$ is performed at the level of binary representation. For example, if $a = 12$ and $b = 20$, then: $a$ & $b$ = $12$ & $20$ = $01100_{2}$ & $10100_{2}$ = $00100_{2}$ = $4_{10}$
* For tests worth $12$ points: $1 \leq K \leq 2$ and $3 \leq N \leq 25$
* For other tests worth $23$ points: $500 \leq N \leq 8\ 000$
* For other tests worth $65$ points: There are no additional restrictions.

# Example 1

`inno.in`
```
4 2
10 7 5 15
```

`inno.out`
```
5
```

## Explanation

For the first example, the ways are:

* Remove $10$ and the remaining sequence is $7$, $5$, $15$, and $7$ & $5$ & $15$ = $5$, which has $2$ bits of $1$
* Remove $10$, $7$ and the remaining sequence is $5$, $15$, and $5$ & $15$ = $5$, which has $2$ bits of $1$
* Remove $10$, $7$, $5$ and the remaining sequence is $15$, and $15$ has $4$ bits of $1$
* Remove $7$, $5$ and the remaining sequence is $10$, $15$, and $10$ & $15$ = $10$ which has $2$ bits of $1$
* Remove $7$, $5$, $15$ and the remaining sequence is $10$, and $10$ has $2$ bits of $1$

# Example 2

`inno.in`
```
5 4
7 7 6 1 62
```

`inno.out`
```
1
```

## Explanation

For the second example, the only possibility is to remove the subarray $7 \ 7 \ 6 \ 1$. Only the number $62$ remains, which has $5$ bits of $1$.
