# Substr

The tests for this problem are not well-constructed enough to correctly differentiate inefficient or incorrect solutions. Click here if you want to help us improve the quality of the tests for this problem! You are given a text consisting of $N$ characters (uppercase letters, lowercase letters, and digits). A substring of this text is a sequence of characters that appear at consecutive positions in the text.

## Task

Given a number $K$, determine the length of the longest substring that appears in the text at least $K$ times.

## Input data

The input file `substr.in` contains on the first line the numbers $N$ and $K$ separated by space. The second line contains a text consisting of $N$ characters (uppercase letters, lowercase letters, and digits), without spaces and ending with a newline character.

## Output data

The output file `substr.out` must contain a single line with the maximum length of a substring that appears at least $K$ times in the original text.

## Constraints and clarifications

$1 \leq N \leq 16 \ 384$

$1 \leq K \leq N$

For $30\%$ of the tests, $N \leq 1 \ 000$

## Example

`substr.in`

`13 3`

`yabadabadooba`

`substr.out`

`2`

## Explanation

The substring $ba$ appears three times in the text. Any substring of larger size (e.g., $aba$) appears less than three times.