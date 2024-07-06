```markdown
$n$ and $t$ are given as two non-zero natural numbers, and $S$ is a binary array of $n$ elements indexed from $1$. A swap in this array consists of choosing two indices $i, j\\ (1 \\leq i, j \\leq n)$ and changing the values of $S[i]$ and $S[j]$. A subarray of length $t$ in the array $S$ represents $t$ elements in consecutive positions in $S$.

# Task

Determine the minimum number of swaps needed in array $S$ to obtain two disjoint subarrays of length $t$ consisting only of elements equal to $1$.

# Input data

The first line of the file `secvente.in` contains the numbers $n$ and $t$ separated by a space. The second line contains $n$ characters `0` and `1`.

# Output data

The first line of the output file `secvente.out` will contain the minimum number of swaps needed to obtain two disjoint subarrays of length $t$ consisting only of elements equal to $1$. If this is impossible, print `-1`.

# Constraints and clarifications

* $2 \\leq n \\leq 1\\ 000\\ 000$
* $2 \\cdot t \\leq n$

# Example 1

`secvente.in`
```
7 2
1010101
```

`secvente.out`
```
2
```

## Explanation

The element at position $1$ is swapped with the element at position $6$, and the element at position $3$ is swapped with the element at position $4$.

# Example 2

`secvente.in`
```
26 3
00010100100100010111001001
```

`secvente.out`
```
1
```

## Explanation

A convenient sequence is located between positions $4$ and $6$ and another between positions $18$ and $20$. A single swap is needed to place a $1$ element at position $5$.
```