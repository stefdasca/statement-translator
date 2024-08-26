# MMsir

Given an array with $N$ integer elements. We define the degree of a sequence as the number of monotony changes. The number of monotony changes in a sequence with $N$ elements represents the number of positions $i$ $(1 < i < N)$ such that $a[i-1] < a[i] > a[i+1]$ or $a[i-1] > a[i] < a[i+1]$. The task is to find the number of subarrays of the sequence with degree $K$.

## Task

## Input data

The file `mmsir.in` will contain on the first line 2 numbers representing the numbers $N$ and $K$. The second line will contain $N$ numbers representing the sequence.

## Output data

The file `mmsir.out` will contain a single number, the result requested in the statement.

## Constraints and clarifications

$1 \leq N \leq 1\,000\,000$

$0 \leq K \leq N$

the numbers in the sequence will be less than or equal to $2^{30}$

## Example

`mmsir.in`

```
6 2
1 2 0 4 6 5
```

`mmsir.out`

```
3
```

## Explanation

The three subarrays have their endpoints at positions $1\dots4$, $1\dots5$, and $2\dots6$.