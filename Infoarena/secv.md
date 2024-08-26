# Secv

Gheorghe has come across a new computer science problem and needs a bit of help!

## Task

Given an array of $N$ natural numbers, find the minimum length of a subarray that contains a strictly increasing subsequence, and this subsequence includes all numbers from the initial array exactly once. If such a sequence does not exist, the answer will be $-1$.

## Input data

The input file `secv.in` contains:

The first line contains the length $N$ of the array. The second line contains $N$ integers, the array itself.

## Output data

The output file `secv.out` contains the required number.

## Constraints and clarifications

$0 \leq N \leq 5\ 000$

The elements of the array are integers in the range $[0, 2\ 000\ 000\ 000]$


## Example

`secv.in` 
```
8
2 1 3 2 1 3 4 5
```

`secv.out` 
```
7
```

## Explanation

The only subarray that follows the conditions from the problem statement is $1\ 3\ 2\ 1\ 3\ 4\ 5$

This subarray contains the subsequence $1\ 2\ 3\ 4\ 5$ .