
Consider a string of bits and a natural number `K`. The string is split into sequences such that every bit in the string belongs to a single sequence and each sequence has a length of at least `1` and at most `K`. After the splitting, each sequence of bits is converted to base `10`, resulting in a string of decimal values. For example, for the bit string `1001110111101010011` and `K = 4`, one possible split is `1 0011 101 111 0 1010 011`, then in base `10`: `1, 3, 5, 7, 0, 10, 3`. Another split could be `1 00 1 1 10 11 110 1010 011`, which results in `1, 0, 1, 1, 2, 3, 6, 10, 3`.

# Task
Write a program that:
* Determines the maximum value (in base `10`) that can be obtained from a sequence of at most `K` bits.
* Splits the initial string into sequences of at most `K` bits so that the resulting decimal string contains a strictly increasing subsequence of the maximum possible length.

# Input data
The first line of the input file `blis.in` contains the natural number `K`, and the second line contains the bit string, the string containing no spaces.

# Output data
The output file `blis.out` will contain on the first line a natural number representing the maximum value that can be obtained from a sequence of at most `K` bits, and on the second line a single natural number representing the maximum length of the strictly increasing subsequence that can be obtained from the bit string by splitting it into sequences of at most `K` bits.

# Constraints and clarifications
* `3 \leq \text{length of the bit string} \leq 100\ 000`
* For `70%` of the tests, `\text{length of the bit string} \leq 1000`
* `1 \leq K \leq 30`
* A subsequence is obtained from a string by removing zero, one, two, or more elements;
* A sequence is formed by elements located at consecutive positions in the string;
* For a correct solution to the first task, `20%` of the score is awarded, and for correctly solving the second task, `80%` is awarded.

# Example

`blis.in`
```
4
1001110111101010011
```

`blis.out`
```
15
6
```

Explanations
---

The sequence of maximum value of at most `4` bits is `1111`, i.e., `15` in base `10`.
For the second task, the binary string is split as follows:
`1 00 1 1 10 11 110 1010 011`, 
Resulting in the decimal string:
`1, 0, 1, 1, 2, 3, 6, 10, 3`.
The maximum length strictly increasing subsequence is `0, 1, 2, 3, 6, 10` which has a length of `6`.
