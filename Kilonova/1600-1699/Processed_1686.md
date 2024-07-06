Ion and Ana have fun building words made up of uppercase English letters: `A`, `B`, $\dots$, `Z`. They imagine a new language that allows words containing subarrays made of the same letter. However, they imposed a restriction: no word must start with the letter `Z`. For example, consider the word: `AAZCCCCADDDBBBBEEC`. The word does not start with `Z`. It can be decomposed into subarrays made of identical letters: `AA Z CCCC A DDD BBBB EE` and `C`. Among these, `CCCC` and `BBBB` have a length of $4$. We call maximally repeatable subarrays the longest subarrays made of identical letters. Thus, in the example above, `CCCC` and `BBBB` are maximally repeatable subarrays.

The question Ion and Ana are now asking is: what is the number (modulo $30 \ 011$) of words made up of **at most** $n$ uppercase English letters, containing at least one maximally repeatable subarray of length $k$. Note that the words will not be able to contain repeatable subarrays strictly longer than $k$.

# Task

Given $n$ and $k$, the maximum length of a word and the length of a maximally repeatable subarray, determine the number of words that can be formed, modulo $30 \ 011$.

# Input data

The input file `nuz.in` contains on the first line the numbers $n$ and $k$ with the meaning from the statement.

# Output data

The output file `nuz.out` will contain on a single line a natural number that represents the number of words that can be formed according to the task.

# Constraints and clarifications

* $2 \leq K \leq N \leq 100 \ 000$
* for $50\%$ of the tests $N \leq 1 \ 000$

# Example 1

`nuz.in`
```
2 2
```

`nuz.out`
```
25
```

## Explanation

There are $25$ sequences: `AA`, `BB`, `CC`, $\dots$, `YY`

# Example 2

`nuz.in`
```
3 2
```

`nuz.out`
```
1275
```
