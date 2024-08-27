## Task

Given a simple character string $A$ with $N$ characters and a periodic and infinite character string $B$ with a period of $M$ characters. The goal is to find the length of the longest common subsequence from $A$ and $B$. By common subsequence, we mean a string found in consecutive positions in both strings.

## Input data

The first line will contain the string $A$ and the second will contain the string $B$.

## Output data

A single number representing the length of the longest common subsequence of the strings $A$ and $B$.

## Constraints

$1 \leq N$

$1 \leq M \leq 250\ 000$

It is guaranteed that the answer is greater than or equal to $M$.

## Example

`potriveala.in`

`potriveala.out`

`FDCABCABCF`

`ABC`

`7`

## Explanation

The second string is $\dots ABCABCABC \dots$ and the longest common subsequence is $FD CABCABC F$.