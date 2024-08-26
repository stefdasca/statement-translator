## Valuable Core Season 2

The Valuable Core is back in action. It has an array $V$ with $N$ elements and wants to calculate the cost of the array, haha!!!! The cost of a subarray is $COST [i,j] = \min(COST[i, K] + COST [K + 1, j]) + V[i] + V[i + 1] + \dots + V[j]$, with $K$ from $i$ to $j - 1$. The cost of a subarray of length 1 is $COST [x,x] = V[x]$, too simple!!!!

## Input data

The input file `nucleulvaloros2.in` will contain on the first line a natural number $N$. The second line will contain $N$ natural numbers representing the array $V$.

## Output data

The output file `nucleulvaloros2.out` will contain a single natural number representing the cost of the array (or in other words, $COST [1, N]$).

## Constraints and clarifications

$1 \leq N \leq 3\ 000$

The elements of the array belong to the interval $[1, 10^9]$

## Example

`nucleulvaloros2.in` 
```
5
10 3 4 12 8
```

`nucleulvaloros2.out`
```
118
```