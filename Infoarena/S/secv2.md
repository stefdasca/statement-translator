# Sequence 2

The tests for this problem are not well designed to correctly differentiate between inefficient or incorrect solutions. Click here if you want to help us improve the quality of the tests for this problem! Gigel has decided to become an Olympiad in informatics, maybe this way he will be able to solve his own problems, and won't ask for your help anymore! During the informatics class, his teacher gave him the problem of finding the subarray with the maximum sum: "Gigel, I give you a series of $N$ integers, and you have to find a subarray (i.e., a subsequence of numbers that appear in consecutive positions in the initial series) with the maximum sum of the elements!" After about 30 minutes, Gigel stood up proudly and said: "I found the optimal complexity algorithm, teacher!" For homework, Gigel has to solve almost the same problem: he needs to find the subarray with the maximum sum of length at least $K$!

## Task

Gigel does not yet know enough informatics to solve this problem, but maybe you can help him! Write a program that solves Gigel's homework problem.

## Input data

The input file `secv2.in` contains on the first line the numbers $N$ and $K$, separated by a space. The second line contains the elements of the series separated by a space.

## Output data

The output file `secv2.out` must contain a single line with three numbers: the starting position and the ending position of the subarray with the maximum sum of length at least $K$ and the sum of the subarray.

## Constraints and clarifications

$1 \leq K \leq N \leq 50\ 000$

The elements in the array are integers in the range $[-25\ 000, 25\ 000]$

## Example

`secv2.in`
```
8 3
0 -6 2 1 4 -1 3 -5
```

`secv2.out`
```
3 7 9
```