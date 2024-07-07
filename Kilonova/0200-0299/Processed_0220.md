# Task
Determine the number of distinct arrays of length `N` with all numbers from the set `{1..K}`, each array having exactly `X` distinct elements.

# Input data
The file `xnumere.in` will contain on the first line three natural numbers: `K X N`.

# Output data
The file `xnumere.out` will contain a single natural number representing the answer to a tourist's question. The result will be written modulo `666013`.

# Constraints and clarifications:
* $1 \leq X \leq \min(K, 10^5)$
* $1 \leq N, K \leq 10^{15}$
* For `10%` of tests it is guaranteed that `N, K, X \leq 7`.
* For `30%` of tests it is guaranteed that `N \leq 10000, K \leq 100`.
* For `60%` of tests it is guaranteed that `K \leq 100`.
* For `85%` of tests it is guaranteed that `K \leq 1000`.
* `2` arrays $A=(x_1, x_2, \ldots, x_n)$ and $B=(y_1, y_2, \ldots, y_n)$ are distinct if there exists at least one position `i` for which $x_i \neq y_i$.

# Example:
`xnumere.in`
```
2 2 4
```
`xnumere.out`
```
14
```
Explanation
---
The arrays are:

`(1,1,1,2),(1,1,2,1),(1,1,2,2),(1,2,1,1),(1,2,1,2),(1,2,2,1),(1,2,2,2),(2,1,1,1),(2,1,1,2),(2,1,2,1),(2,1,2,2),(2,2,1,1),(2,2,1,2),(2,2,2,1)`

`xnumere.in`

```
10 6 8 
```

`xnumere.out`

```
258420
