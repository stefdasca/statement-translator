---

Given a string of length `N` consisting of uppercase English letters, and an integer `K`.

A possible operation on the string is to repeatedly choose a subarray of length at least `K` with all identical elements and remove it from the string. Evidently, the operation is first applied on the initial string and subsequently on the resulting string from the previous operation. The operation is applied until the string becomes empty (of length `0`) or the string no longer contains subarrays of length at least `K` with all identical elements.

# Task
Given `N, K` and the character string, determine what is the minimum length to which the string can be reduced after applying the operations in a convenient way.

# Input Data
The input file `zuma.in` contains on the first line the numbers `N` and `K` separated by a space, and the second line contains the character string composed of `N` uppercase letters.

# Output Data
The output file `zuma.out` must contain a single natural number representing the minimum length that the string can have after applying the operations in a convenient way.

# Constraints and clarifications
* $ 1 \leq K \leq N \leq 500 $
* For tests worth `10` points, $ 25 \leq K \leq N \leq 100 $
* For other tests worth `10` points, $ K = 2 $
* For other tests worth `10` points, the number of distinct characters in the string is `2`
* For other tests worth `15` points, $ 1 \leq N \leq 50 $
* For other tests worth `35` points, $ 1 \leq N \leq 200 $

# Example
`zuma.in`
```
10 3
AAABBBCCCA
```

`zuma.out`
```
0
```

Explanation
---

We have `N=10` and `K=3`. Any subarray with identical letters of length at least `3` can be removed.
Considering the string indexed from `1`, in the first operation we can remove the subarray `[4,6]=BBB` because it has length `3`. Now the string is `AAACCCA`, so we can remove the subarray `[4,6]=CCC`, obtaining the string `AAAA`.
This is composed of `4` identical characters, so we can delete it and obtain the empty string with length `0`.
If we had chosen in the previous step to remove the subarray `[1,3]=AAA` and then the subarray `CCC`, we would have obtained a final string of length `1`, consisting of the last `A`.

