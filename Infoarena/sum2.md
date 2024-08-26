# Sum2

A sequence of integers is given. We are looking for a subarray of length between $L$ and $U$ consisting of consecutive elements of the initial sequence with the maximum sum of elements.

## Task

Write a program that determines the maximum sum of such a subarray.

## Input data

The input file `sum2.in` contains on the first line three integers $N$, $L$, and $U$, separated by a space. $N$ represents the length of the large sequence, and $L$ and $U$ have the meanings given in the statement. The next line contains the $N$ numbers, separated by a space.

## Output data

The output file `sum2.out` will contain on the first line an integer representing the maximum sum that can be obtained.

## Constraints and clarifications

$1 \leq L$

$L \leq U$

$U \leq N \leq 100\ 001$

The numbers in the sequence are integers and have values ranging from $[-10\ 000, 10\ 000]$.

## Example

`sum2.in`

```
9 2 3
100 -100 0 10 -5 0 10 0 1
```

`sum2.out`

```
11
```