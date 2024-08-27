Invcs

Gigel is playing again with the algorithm for finding the longest increasing subsequence. For this, he uses an auxiliary array $v$ with the meaning $v_i = \text{the length of the longest increasing subsequence in the initial array that ends at position} \ i$. Looking at the obtained array, he asks the following question:

## Task

How many permutations of the first $N$ natural numbers lead to obtaining this auxiliary array?

## Input data

The first line of the input file `invcs.in` will contain the non-zero natural number $N$ representing the length of an array on which Gigel applied the algorithm for finding the longest increasing subsequence. The next $N$ lines will contain the auxiliary array $v$ calculated by Gigel.

## Output data

The output file `invcs.out` will contain a single line with the required number.

## Constraints and clarifications

$N \leq 20$

## Example

`invcs.in`
```
5
1
1
1
2
2
```

`invcs.out`
```
6
```