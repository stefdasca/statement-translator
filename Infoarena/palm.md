## Task

Everybody knows the computer scientist Gigel. This year, he found a new passion: strings. While studying one of the old books he found in his father's library, he came across the following problem: "Given a string, determine its longest palindrome mountain subsequence." A string is called a palindrome if it reads the same backward as forward. A string is called a mountain if there is a position $p$ such that: all letters at positions less than or equal to $p$ are in alphabetical order and all letters at positions greater than or equal to $p$ are in reverse alphabetical order. After many days of thinking about how to solve this problem, he decided to ask for your help. As a reward for a correct solution, he will give you 100 points.

## Input data

The input file `palm.in` will contain on the first line the string $S$.

## Output data

The output file `palm.out` will print on the first line the length of the longest palindrome mountain subsequence of the string $S$.

## Constraints and clarifications

1 $\leq$ length of string $S$ $\leq$ 500

the string $S$ will consist of only lowercase letters of the English alphabet

the alphabetical / reverse alphabetical order is not necessarily strict

## Example

`palm.in`
```
zabcdcbazvb
```

`palm.out`
```
7
```