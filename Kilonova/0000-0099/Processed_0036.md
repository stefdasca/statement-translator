
Let `n` be a natural number and $M=\{S_1,S_2,\dots,S_n\}$ a set of non-empty strings. Let $S_k$ be a string from `M`. Then, any character of $S_k$ belongs to the set `{ 'a', 'b' }`. We denote by $|S_k|$ the number of characters in the string $S_k$ or, equivalently, its length. A subarray $S_k[i:j]$ of $S_k$ is formed by the characters located at consecutive positions `i, i+1, ..., j`. Thus, if $S_k = abbbaababa$, then $S_k[3:6] = bbaa$ or the highlighted subarray: ab**bbaa**baba.

# Task
Given a set `M`, determine the maximum length of a subarray that is found in all the strings from `M`.

# Input data
The input file `subsecvente.in` contains:
* The first line contains a natural number `n` equal to the cardinality of the set `M`.
* Each of the following `n` lines contains a string from the set `M`.

# Output data
The output file `subsecvente.out` will contain a single natural number equal to the length of the found subarray.

# Constraints and clarifications
* `1 < n < 5`
* If $|S| = |S_1| + |S_2| + \dots + |S_n|$, then `|S| < 50\ 001`
* It is guaranteed that there will always be a solution
* It is guaranteed that the result will not exceed `60`
* For `30%` of tests: `|S| < 101`
* For `55%` of tests: `|S| < 3\ 501`
* For `80%` of tests: `|S| < 10\ 001`

# Example

`subsecvente.in`
```
4
abbabaaaaabb
aaaababab
bbbbaaaab
aaaaaaabaaab
```

`subsecvente.out`
```
5
```

Explanation
---
The length of a common subarray of maximum length is `5`.

In the example, the common subarray of length `5` is `aaaab`:
abbaba**aaaab**b, **aaaab**abab, bbbb**aaaab**, aaa**aaaab**aaab.
