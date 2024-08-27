## Task

Due to security paranoia, Sam decided to choose a long password for his email account that contains only lowercase English letters. However, he realized that there is a high risk of forgetting his password, so he decided to encode it into two strings, which also contain only lowercase English letters. He wrote these strings $A$ and $B$ such that the password $S$ is an anagram of $B$ that appears as a subsequence in $A$ and is minimal lexicographically. A string is considered a subsequence of $A$ if and only if there exists a sequence of strictly increasing indices so that for $\dots$. We say that $A$ is lexicographically smaller than $B$ if and only if there exists an index $i$ so that for $\dots$ and $\dots$. As expected, Sam forgot his password after a week, and now he is struggling to recover it, which is why he is asking you for help. Write a program that finds the password for him.

## Input data

The input file `password1.in` contains exactly two strings $A$ and $B$ separated by a single whitespace.

## Output data

The output file `password1.out` must contain a line representing Sam's password. In case there is no solution, the word $\ll$impossible$\gg$ (without quotes) will be printed.

## Constraints

$n \leq 10^5$

$|A| \leq 10^5$

The existence of a solution is not guaranteed.

## Example

`password1.in` `password1.out`

```
abacaba bab  
abb
```

`password1.in` `password1.out`

```
abacaba cbc  
impossible
```

`password1.in` `password1.out`

```
abacaba caab  
aacb
```