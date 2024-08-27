# Bits

Gigel is passionate about computer science, especially the digits 0 and 1; so much so that he has assigned each of his $2^N$ friends a label, in the form of a bit string of length $N$. All the labels are distinct. One day, Gigel thought he wanted to build a label for himself, of the smallest possible length, that contains each of his $2^N$ friends' labels exactly once as a subarray.

## Task

Write a program that determines Gigel's label, of minimal length.

## Input data

The first line of the input file `biti.in` will contain the number $N$.

## Output data

The first line of the output file `biti.out` will contain the length of the string. The second line will print a string of bits 0 or 1 which will represent the found label.

## Constraints and clarifications

$1 \leq N \leq 20$

If there are multiple solutions of minimum length, print the smallest one in lexicographic order.

## Example

`biti.in`
```
3
```

`biti.out`
```
10
0001011100
```