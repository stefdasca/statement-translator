Disappointed with his results in the last competition, Paftenie gave up programming and focused strictly on laborious work that involves less intellectual effort. This time, he receives a text and needs to calculate the average length of the words in the text, with a word being defined as a maximal continuous sequence of English alphabet characters ('a' $\dots$ 'z', 'A' $\dots$ 'Z'). We define the average length = (total length of the words in the text) / (number of words in the text).

## Task

Write a program that solves Paftenie’s problem.

## Input data

The first line of the input file text.in contains the given text.

## Output data

The output file text.out will contain on the first line a single integer, representing the integer part of the average length of the words in the text.

## Constraints and clarifications

The size of the input file is at most $1 \text{MB}$.

The input file will contain only uppercase and lowercase letters, digits, spaces, and symbols (meaning it will not contain special characters).

## Example

`text.in`  
Lasa-ma in pace, ca am invatat azi noapte toata ziua!

`text.out`  
3

## Explanation

The total length of the words in the text = $41$, the number of words = $11$ $\Rightarrow$ $\left[ \frac{41}{11} \right] = 3$.