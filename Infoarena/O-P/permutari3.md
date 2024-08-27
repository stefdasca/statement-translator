# Permutations3

A permutation of order $K$ consists of all numbers $1,2,\dots,K$ not necessarily in this order. A sequence of length $L$ consists of $L$ elements of the array located at consecutive positions. We say that a sequence of length $L$ is a permutation of order $L$ if it contains all numbers $1,2,\dots,L$, not necessarily in this order.

## Task
Given an array of $N$ non-zero natural numbers $a_1,\dots,a_N$, which represents a permutation of order $N$. Calculate the number of subarrays in the array $a$ that have the property of being permutations. 

## Input data

The input file `permutari3.in` contains:
- The first line contains the natural number $N$
- The second line contains the first $N$ non-zero natural numbers, separated by spaces. The $N$ numbers given are not necessarily in strictly increasing order.

## Output data

The output file `permutari3.out` will contain a single natural number representing the number of permutation-type subarrays that appear in the given array.

## Constraints

$1 < N \leq 100\ 000$ 

## Example

`permutari3.in`
```
7
4 2 5 1 3 7 6
```

`permutari3.out`
```
3
```

## Explanation

In the array there are 3 permutation-type subarrays, of lengths $1$, $5$, and $7$: 

$1$: $4$

$5$: $4\ 2\ 5\ 1\ 3$

$7$: $4\ 2\ 5\ 1\ 3\ 7\ 6$

There are no permutation subarrays of lengths $2$, $3$, $4$, or $6$.