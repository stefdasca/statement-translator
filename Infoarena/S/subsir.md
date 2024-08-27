### Subsequence

Zaharel is trying to teach his friend Eugenia computer science. Today he taught her dynamic programming, specifically the longest common subsequence problem: given two strings, determine their longest common subsequence. A subsequence of a string is made up of characters (not necessarily consecutive) of that string, in the order they appear in the string. Eugenia understood the solution to the problem but asked Zaharel the following question: how many distinct maximum length common subsequences exist for the two strings? Two subsequences are distinct if there is at least one character in one that differs from the character in the other subsequence at the same position. 

## Task

Help Zaharel determine the remainder of the division of the number of distinct maximum length common subsequences for two given strings by the number $666013$. 

## Input data

The input file contains the first string on the first line, and the second string on the second line.

## Output data

The output file should contain the required number on the first line.

## Constraints and clarifications

- Each string has a length less than or equal to $500$
- The strings contain only lowercase letters of the English alphabet

## Example

`subsir.in`
```
banana
oana
```

`subsir.out`
```
1
```

## Explanation

The only maximum length common subsequence that can be formed is `$ana$.