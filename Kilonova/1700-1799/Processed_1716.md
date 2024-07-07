
Consider a natural number $K$ and a sequence of $N$ arrays $s_1$, $s_2$, $\dots$, $s_N$. Each array is made up of **distinct digits**. For two arrays $s_i$ and $s_j$, the subtraction operation (-) is defined such that: $s_i - s_j$ will contain only the digits that appear in $s_i$ but not in $s_j$. For example, if $s_i = (1, 3, 8)$ and $s_j = (2, 9, 3)$, then $s_i - s_j = (1, 8)$. This operation is not associative, $(s_i - s_j) - s_p$ is different from $s_i - (s_j - s_p)$.

Thus, if a sequence $s_{i_1}$, $s_{i_2}$, $\dots$, $s_{i_p}$ is selected from the sequence, it is agreed that $s_{i_1} - s_{i-2} - \dots - s_{i_p}$ will be executed from right to left.

Example: $(1, 2, 3) - (2, 3) - (1, 3) = (1, 2, 3) - (2) = (1, 3)$. Two distinct digits were obtained.

# Task

Determine the number of non-empty subsequences $s_{i_1}$, $s_{i_2}$, $\dots$, $s_{i_p}$ from the sequence $s_1$, $s_2$, $\dots$, $s_N$ for which when the subtraction operation is performed (i.e. $s_{i_1}$ - $s_{i_2}$ - $\dots$ - $s_{i_p}$), at least $K$ distinct digits are obtained. Since the number of such subsequences can be very large, it will be calculated modulo $123 \ 457$.

# Input data

The file `ksiruri.in` contains natural numbers $K$ and $N$ on the first line. The next $N$ lines contain one array $s_i$ each. Line $i+1$, for $i = 1 \dots N$, will contain the values $m \ c_1 \ c_2 \dots cm$, where $m$ is the number of terms in array $s_i$, and $c_1$, $c_2$, $\dots$, cm are the distinct digits of array $s_i$.

# Output data

The file `ksiruri.out` contains a single natural number representing the number of subsequences, modulo $123 \ 457$.

# Constraints and clarifications

* $1 \leq K \leq 8$
* $2 \leq N \leq 50 \ 000$
* $1 \leq i_1 < i_2 < \dots < i_p \leq N$

# Example

`ksiruri.in`
```
3 3
5 5 6 7 8 9
3 4 5 6
3 7 8 9 
```

`ksiruri.out`
```
6
```

## Explanation

$s_1$ = $5 \ 6 \ 7 \ 8 \ 9$
$s_2$ = $4 \ 5 \ 6$
$s_3$ = $7 \ 8 \ 9$

The six non-empty subsequences are: $s_1$, $s_1-s_2$, $s_1-s_2-s_3$, $s_2$, $s_2-s_3$, $s_3$
