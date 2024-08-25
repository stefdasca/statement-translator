# Triopalindrome

Georgică has discovered a new type of character string and thought to name it a triopalindrome. A triopalindrome is a string that is formed by concatenating the same string exactly three times. Given a string of lowercase English alphabet characters, answer Georgică's question: How many triopalindrome subarrays exist in the given string?

## Input data

The input file `triopalindrom.in` contains Georgică's string of characters.

## Output data

The output file `triopalindrom.out` contains, on a single line, the number of triopalindrome subarrays in the given string.

## Constraints

$1 \leq N \leq 5\,000$, where $N$ is the length of the string.

## Example

`triopalindrom.in`:
```
aaaabcbcbc
```

`triopalindrom.out`:
```
3
```

## Explanation

There are three triopalindrome subarrays: `aaa`, `aaa`, `bcbcbc`.