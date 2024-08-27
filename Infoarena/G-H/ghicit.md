# Guessing

You and the Farmer are playing an uninteresting game. You have a large string of characters. The Farmer tells you another string of characters, and you need to answer quickly whether that string is a subsequence of your string. The Farmer asks many questions, and since you are a computer scientist, you thought it would be faster if you knew in advance all the strings he might ask about. Before doing all this work, you are interested in the total number of distinct subsequences of your string, to know if it makes sense to start this task.

## Task

Write a program that finds the number of distinct subsequences of a given string of characters.

## Input data

The input file `ghicit.in` contains a single line which contains the string of characters for which we must determine the number of distinct subsequences.

## Output data

The output file `ghicit.out` contains a single line which contains the number $N$, representing the number of determined distinct subsequences.

## Constraints and clarifications

$1 \leq$ length of the string $\leq 50\,211$ \\
$1 \leq N \leq 2\,000\,000\,000$ \\
A subsequence of string $s=s_0, s_1, s_2, \dots, s_k$ is composed of consecutive characters of the string $s_i, s_{i+1}, \dots, s_j$ with $0 \leq i \leq j \leq k$ \\
The string contains characters with ASCII codes between $0$ and $255$ and ends with the character `\n` (end of line) which should not be considered

## Example

`ghicit.in`
```
abab
```

`ghicit.out`
```
7
```

## Explanation

The subsequences are: a, b, ab, ba, aba, bab, abab.