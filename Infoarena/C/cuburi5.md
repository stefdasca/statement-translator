# Cuburi5

Miruna and Laura play with $N$ special cubes every day. Each of these cubes has $K$ natural numbers inscribed on it. Today, the two girls lined up all the $N$ cubes in a row, one after another. They want to choose a subsequence of cubes such that any two adjacent cubes in the subsequence have at least one number in common. Help them find the longest possible subsequence!

## Input data

The input file `cuburi5.in` will contain on the first line two natural numbers $N$ and $K$, having the meaning described in the statement. Each of the next $N$ lines will contain $K$ natural values, representing the numbers inscribed on the cubes.

## Output data

In the output file `cuburi5.out` you will print the indices of the maximal subsequence that respects the imposed conditions. If there are multiple solutions, you will print the first one in lexicographical order.

## Constraints and clarifications

$1 \leq N \leq 50000$

$1 \leq K \leq 2000$

$1 \leq N * K \leq 1000000$

The values inscribed on the cubes are in the interval $[1\ldots100000]$

## Example

`cuburi5.in`

```
5 2 
1 10 
4 5 
4 10 
2 1 
5 4 
```

`cuburi5.out`

```
1 3 5 
```