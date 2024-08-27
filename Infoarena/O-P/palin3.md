## Task

Mihai wants to buy tickets to the match. Since no one delivers tickets to Prelungire, he will stay at home and try to guess the match's score. Superstitious by nature, Mihai believes that the performance of the tricolors (Romanian national team) is influenced by the appearance of palindromes of length $3$ in a given string. Mihai can perform the following operation: choose a palindrome subarray of length $3$ and remove it from the string. He is convinced that if, by repeatedly using this operation, he can reduce the string to an empty one, then Romania will win the match. To be as sure as possible, he chooses $T$ such strings.

## Input data

The input file `palin3.in` contains a natural number $T$ on the first line, the number of strings. The next $T$ lines each contain one of the strings chosen by Mihai.

## Output data

The output file `palin3.out` contains $T$ lines. Line $i$ will contain "DA" if the $i^{th}$ string indicates a victory for the tricolors, "NU" otherwise.

## Constraints

$1 \leq T \leq 20$

The length of a string is less than or equal to $100$

The string consists only of lowercase letters of the English alphabet

## Example

`palin3.in`
```
3
miaham
bbbeee
afe
```

`palin3.out`
```
DA
DA
NU
```