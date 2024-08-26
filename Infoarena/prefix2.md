# Prefix2

You are given a string $S$ composed of uppercase and lowercase letters of the Latin alphabet. For each prefix of $S$, you must determine how many different subsequences of characters it contains.

## Example:
For the string

$aabab$, we can take the prefixes one by one:

`a -> a -> 1`  
`aa -> a, aa -> 2`  
`aab -> a, b, aa, ab, aab -> 5`  
`aaba -> a, b, aa, ab, ba, aab, aba, aaba -> 8`  
`aabab -> a, b, aa, ab, ba, aab, aba, bab, aaba, abab, aabab -> 11`

## Input data

The input file `prefix2.in` contains on the first line the string $S$.

## Output data

The output file `prefix2.out` must contain as many lines as there are characters in the string $S$. Thus, the $i$-th line must contain a single natural number representing the number of distinct subsequences of characters of the prefix composed of $i$ characters of the string $S$.

## Constraints and clarifications

$1 \leq$ length of $S$ $\leq 100\ 000$

## Example

`prefix2.in`
```
aabab
```

`prefix2.out`
```
1
2
5
8
11
```