# Secv9

Given a sequence of $N$ integers, find the longest subarray with a sum greater than or equal to a given number $S$.

## Task

## Input data

The input file `secv9.in` contains the following:
- The first line contains two integers, $N$ and $S$.
- The second line contains the $N$ values of the sequence.

## Output data

The output file `secv9.out` will contain the length of the longest subarray with a sum greater than or equal to $S$.

## Constraints

$1 \leq N \leq 10^5$

The values of the sequence, the sum of any subarray, as well as the value $S$, fit within 32-bit signed integers.

A solution is guaranteed to exist for all test cases.

## Example

`secv9.in`
```
5 7
-4 10 -3 6 -12
```

`secv9.out`
```
4
```

## Explanation

The subarray between indices 1 and 4 of the sequence has a sum of 9. It is the longest subarray with a sum greater than or equal to 7.