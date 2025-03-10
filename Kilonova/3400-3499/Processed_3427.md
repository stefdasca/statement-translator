Andrei is an adventurer searching for a treasure full of gold coins. When he reached the final clue, the one that would tell him where the treasure is located, he saw that the clue had two natural numbers $N$ and $K$ and, on the second line, a sequence of $N$ lowercase letters of the English alphabet. Andrei must take the current sequence and remove the first subarray of $K$ identical letters that appear in consecutive positions. He will repeat this process until there are no more consecutive subarrays of $K$ identical letters.

Andrei asks for your help in solving this problem as quickly as possible so he can reach the treasure first.

# Task

Given $N$ and $K$, natural numbers, and a sequence of $N$ lowercase letters of the English alphabet, you must always remove the first subarray of $K$ identical characters found in consecutive positions until no such subarray exists.

# Input data

The first line contains 2 natural numbers, $N$ and $K$, and the second line contains a sequence of $N$ lowercase letters of the English alphabet.

# Output data

The output will contain a sequence that represents the final sequence obtained after performing all possible eliminations.

# Constraints and clarifications

* $2 \leq K \leq N \leq 200 \ 000$
* All characters of the initial sequence are lowercase letters of the English alphabet.
* It is guaranteed that the final sequence will not be empty!

| # | Score | Constraints |
| ------- | ---- | ---------- |
| 1 | 35 | $N, K \leq 1 \ 000$ |
| 2 | 65 | No additional constraints |

# Example 1

`stdin`
```
5 2
abbac
```

`stdout`
```
c
```

## Explanation

Initial sequence: $\text{a\underline{bb}ac}$.

Sequence after the first elimination: $\text{\underline{aa}c}$.

Sequence after the second elimination: $\text{c}$.

# Example 2

`stdin`
```
12 3
aabbbaabbaac
```

`stdout`
```
abbaac
```

## Explanation

Initial sequence: $\text{aa\underline{bbb}aabbaac}$.

Sequence after the first elimination: $\text{\underline{aaa}abbaac}$.

Sequence after the second elimination: $\text{abbaac}$.