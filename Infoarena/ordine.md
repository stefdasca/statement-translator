## Task

You are given a string consisting of lowercase English letters (characters from $a$ to $z$). The task is to obtain the smallest lexicographical anagram of the string with the property that any two adjacent characters in the anagram are different. An anagram of the initial string is a string that contains exactly the same characters but possibly in a different order. Two characters are called adjacent if they are next to each other (the first character is adjacent to the second, the second to the third $\dots$). It is guaranteed that there is always a solution.

## Input data

The file `ordine.in` will contain the initial string of characters.

## Output data

The file `ordine.out` will contain the smallest lexicographical anagram of the initial string.

## Constraints and clarifications

$1 \leq$ length of the string $\leq$ $1\,000\,000$

A string $X$ is smaller lexicographically than a string $Y$ if there exists a $k$ such that $X_i = Y_i$ for any $i < k$ and $X_k < Y_k$

## Example

`ordine.in`

```
cbab
```

`ordine.out`

```
abcb
```
