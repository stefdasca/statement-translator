## Xor Max

Paftenie is an exceptional student. Many times, he asks questions that may or may not have answers. This time he came up with a new idea. He has a sequence of $N$ non-negative integers and wants to choose a subarray of the sequence $a_i a_{i+1} \dots a_j$ such that $a_i \, \text{xor} \, a_{i+1} \, \text{xor} \dots \text{xor} \, a_j$ is maximized.

## Task

Help Paftenie solve the problem!

## Input data

The input file `xormax.in` contains on the first line the number $N$ of integers in the sequence.
The next line contains the elements of the sequence separated by spaces.

## Output data

The output file `xormax.out` will contain on the first line 3 numbers: $max$, $start$, $stop$, representing the maximum value found, the starting position of the subarray, and the ending position of the chosen subarray. If there are multiple solutions, the subarray with the minimum $stop$ will be chosen, and if there are still multiple solutions, the shortest subarray will be chosen.

## Constraints and clarifications

$1 \leq N \leq 100\ 000$

The numbers in the sequence are strictly less than $2^{21}$.

## Example

`xormax.in`
```
5
1 0 5 4 2
```

`xormax.out`
```
6 4 5
```

## Explanation

The maximum value found is $6$. The subarray consists of the last two elements of the sequence $4 \, \text{xor} \, 2 = 6$.