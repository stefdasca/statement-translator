
Consider three positive natural numbers: `n`, `k`, and `x`. We call a *kx-decomposition* of the number `n` a way to write the number `n` as the sum of `k` positive natural numbers such that the difference between any two terms of the sum is at least `x`.

# Task
Given three natural numbers `n`, `k`, and `x`, determine how many distinct *kx-decompositions* exist. Two *kx-decompositions* are distinct if they differ by at least one term.

# Input data
The file `desc.in` contains on the first line three positive natural numbers representing the numbers `n`, `k`, and `x`.
    
# Output data
The file `desc.out` will contain one single value representing the remainder of the division of the number of distinct *kx-decompositions* by the number `10007`.

# Constraints and clarifications
* For `20%` of the tests `0 < n \leq 200`; for the remaining `80%` of the tests, `200 < n \leq 10000`;
* `1 \leq x, k \leq n`

# Example
`desc.in`
```
20 2 3
```
`desc.out`
```
8
```

Explanations 
---

The number of *kx-decompositions* in this case is `8`. These are formed from the numbers `1` and `19`; `2` and `18`; `3` and `17`; `4` and `16`; `5` and `15`; `6` and `14`; `7` and `13`; `8` and `12`

`desc.in`
```
2000 19 7
```

`desc.out`
```
3184    
```
