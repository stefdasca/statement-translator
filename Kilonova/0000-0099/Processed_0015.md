```markdown
# Task

Felicia is interested in the maximum lexicographic subsequence of a string. Note that a string $a$ is considered smaller in lexicographic order than a string $b$ if $a$ is a prefix of $b$, or if there exists a position $i$ for which we have $a[1] = b[1]$, $...$, $a[i-1] = b[i-1]$, and $a[i] \lt b[i]$. Thus, the maximum lexicographic subsequence of a string of characters is the largest subsequence, in lexicographic order, of a string of characters (for example `zzxx` for `azbxazbxaax`). For a string $s$ of characters, we denote by $m(s)$ the maximum lexicographic subsequence of $s$, and with $v(s) = |m(s)|$ the length of this subsequence.

Felicia gives you a string $s$ consisting of lowercase English letters. Consider all continuous subarrays $s^{\prime}$ of $s$. Felicia wants you to calculate the sum of the values $v(s^{\prime})$ for all possible subarrays $s^{\prime}$ mentioned earlier.

# Input data

The single line read will contain the string $s$.

# Output data

You must print the required sum, modulo $10^9 + 7$.

# Constraints and clarifications

* $1 \leq N \leq 10^6$

## Subtask 1 (20 points)
* $N \leq 15$

## Subtask 2 (10 points)
* $N \leq 200$

## Subtask 3 (20 points)
* $N \leq 2 \ 000$

## Subtask 4 (20 points)
* $N \leq 5 \cdot 10^4$

## Subtask 5 (30 points)
* No additional constraints.

# Example 1
`stdin`
```
cab
```
`stdout`
```
8
```

## Explanation
We observe that $m(c) = c$, $m(a) = a$, $m(b) = b$, $m(ca) = ca$, $m(ab) = b$, $m(cab) = cb$. Thus, the answer is $1+1+1+2+1+2=8$

# Example 2
`stdin`
```
felicia
```

`stdout`
```
59
```
```