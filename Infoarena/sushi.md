# Sushi

Given a sequence of $N$ natural numbers. Let the function $Sushi(i,j)$ return the sum of the "or" of elements from $i$ to $j$ and the "and" of elements from $i$ to $j$. "Or" and "And" refer to the two binary operations. Determine the subarray $(i,j)$ which has the maximum value of $Sushi(i,j)$. In case of a tie, determine the one with the smallest $i$ index. If there is still a tie, determine the one with the largest $j$ index.

## Task

## Input data

The input file `sushi.in` will contain:

- The first line will contain a natural number $N$.
- The second line will contain $N$ natural numbers.

## Output data

The output file `sushi.out` will contain 3 natural numbers: $i$, $j$, and $val$, representing the left end of the subarray, the right end of the subarray, and the value of the $Sushi(i,j)$ function, respectively.

## Constraints

$1 \leq N \leq 1\,000\,000$

The values in the array are in the range $[1, 1\,000\,000\,000]$

## Example

`sushi.in` `sushi.out`
```
2
1 2
2 2 4
```