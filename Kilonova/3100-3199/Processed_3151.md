
# Task

You are given a string $s$ that contains only lowercase letters of the English alphabet. Determine the minimum number of operations needed so that $s$ contains the string `roalgo` as a subsequence. The operation you can perform is to replace a letter in the string with another letter from the English alphabet.

# Input data

The first line contains the string $s$.

# Output data

The first line will contain a single integer, the number of operations required to obtain the subsequence `roalgo`. If this subsequence already exists, print $0$.

# Constraints and clarifications

* $6 \leq |s| \leq 100 \ 000$, where $|s|$ represents the length of the string $s$. 

# Example

`stdin`
```
qaorxqlgp
```

`stdout`
```
3
```

## Explanation

The minimum number of operations is $3$ (the string `rxqlgp` can be transformed into the string `roalgo` by replacing `x`, `q`, and `p` with the appropriate letters).
