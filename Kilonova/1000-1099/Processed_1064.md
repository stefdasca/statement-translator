
Given an alphabet consisting of $n$ distinct letters. With these letters, words of $n$ letters can be formed. Among these, we are interested in the words in which there is at least one letter that appears at least twice. We denote the number of these words by $nr$.

# Task

Write a program that, given $n$, determines $nr$.

# Input data

The input file `nrcuv.in` contains on the first line the natural number $n$.

# Output data

The output file `nrcuv.out` contains on the first line the number $nr$.

# Constraints and clarifications

* $1 \leq n \leq 100$;
* For $20\%$ of the tests $n < 11$.

# Example 1

`nrcuv.in`
```
2
```

`nrcuv.out`
```
2
```

## Explanation

If we denote the two distinct letters by `a` and `b`, the words we are interested in are `aa` and `bb`.

# Example 2

`nrcuv.in`
```
11
```

`nrcuv.out`
```
285\ 271\ 753\ 811
```

```
