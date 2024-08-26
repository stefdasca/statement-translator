Iv

Nobody knows why $Igor$ and $Vitalie$ started engaging in mathematics. The fact is, they encountered a problem for which pencil and paper are not sufficient. Given two strings of characters, they attempt to merge them in such a way as to obtain a palindrome. Although obtaining a single palindrome is an easy task, they would like to calculate how many different ways there are to merge the two strings such that the result is a palindrome.

## Task

Help $Igor$ and $Vitalie$ solve this problem that troubles their minds.

## Input data

The file $iv.in$ contains two lines, one for each string of characters, each consisting of at most $500$ lowercase letters of the English alphabet.

## Output data

The file $iv.out$ will contain on the first line a single number, representing the calculated number of possibilities modulo $3210121$.

## Constraints and clarifications

The length of each string of characters is between $1$ and $500$.

For $20\%$ of the tests, the length of each of the two strings is between $1$ and $10$.

For $60\%$ of the tests, the length of each of the two strings is between $1$ and $200$.

## Example

$iv.in$

`ab`

`ba`

$iv.out$

`4`

## Explanations

There are $4$ ways to merge the two strings such that the result is a palindrome. The characters of the first string are marked in red, those of the second string are marked in blue:

$ab \; ba$

$a \; b \; b \; a$

$b \; a \; a \; b$

$ba \; ab$