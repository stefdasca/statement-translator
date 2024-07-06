Below is the translated text while preserving the specified structure, format, and custom image format:
___

Two numbers `N` and `M` followed by a non-zero integer array `S` of odd length `N` indexed from `0` are given. This array will undergo exactly `M` swap operations. An operation involves randomly selecting two indices (not necessarily distinct) in the interval `[0, N - 1]` and swapping the elements at those positions.

An array is considered **alternating** if there are no adjacent elements having the same sign.

# Task
Determine the probability that at the end of the `M`-th operation, the array will be alternating. (It is guaranteed that there exists at least one arrangement of the array such that it is alternating). It can be shown that the required probability can be represented in the form `P / Q` where `P` and `Q` are coprime.

# Input data
The first line of the file `alternant.in` contains two natural numbers `N` and `M`.
The second line of the input file contains the array `S`.

# Output data
The output file `alternant.out` will contain the probability that at the end of the `M`-th operation the array will be alternating, represented in the form $P \times Q^{-1} (\text{modulo } 1\ 000\ 000\ 009)$, `P` and `Q` being defined above.

# Constraints and clarifications
* `1 \leq N \leq 100`
* `N` is odd
* `1 \leq M \leq 1 000 000 000`
* For `75%` of the tests, it is guaranteed that `N * M \leq 1 000 000`

# Example
`alternant.in`
```
3 2
1 2 -3
```
`alternant.out`
```
370370374
```
Explanation
---
The fraction corresponding to the example is `24/81`. Simplified, the fraction becomes `8/27`.
___

The translation has been thoroughly checked for potential grammar and syntax errors in accordance with English language rules.