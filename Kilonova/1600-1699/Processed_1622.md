Here is the translated and processed text as specified:

```
Two natural numbers $P$ and $Q$ and a sequence $S$ = $S_1$, $S_2$, $\dots$, $S_N$ of integers are given. From the sequence $S$, a ($P, Q$) - subsequence $S_{i_1}$, $S_{i_2}$, $\dots$, $S_{i_k}$ must be chosen such that $k \geq 2$ and $P \leq i_j - i_{j-1} \leq Q$ for any $j = 2 \dots k$.

For example, for $P = 2$, $Q = 3$ and $S = (2, -3, -7, -8, 5, -1)$, the subsequence ($2, -3, -8$) is not a ($2, 3$) - subsequence, but the subsequences ($2, -7, 5$) and ($2, -7, -1$) are ($2, 3$)-subsequences.

For any ($P, Q$)-subsequence $X = (S_{i_1}, S_{i_2}, \dots, S_{i_r})$, we are interested in the value of the expression $e(X)$ = |$S_{i_1} - S_{i_2}$| + |$S_{i_2} - S_{i_3}$| + $\dots$ + |$S_{i_{r-1}} - S_{i_r}$|, where |$a$| denotes the absolute value of the integer $a$.

# Task

Calculate and display $E$ = max{$e(X)$, $X$ is a ($P, Q$) - subsequence of $S$}.

# Input data

In the input file `pqstr.in`, the first line contains the numbers $N$, $P$ and $Q$ separated by spaces. The next line contains $N$ integers separated by spaces.

# Output data

In the output file `pqstr.out`, the maximum determined value will be printed.

# Constraints and clarifications

* $1 \leq P \leq Q < N \leq 100\ 000$
* The numbers in the sequence $S$ will each have at most nine digits.

# Example 1

`pqstr.in`
```
7 2 4
7 -2 6 -1 8 6 2
```

`pqstr.out`
```
16
```

## Explanation

The maximum value is $16$ and is obtained for $e(-2, 8, 2) = 16$.

# Example 2

`pqstr.in`
```
6 2 3
2 -3 -7 -8 5 -1
```

`pqstr.out`
```
21
```

## Explanation

$e(2, -7, 5) = 21$
