Swaps2

Unfortunately, Miruna does not appear in this problem, only a sequence $S$ of $N$ bits. This sequence needs to be sorted in ascending order, and the only possible operation is a swap. Given two indices $i$ and $j$, by applying the swap operation on the pair $(i, j)$, the values $S_i$ and $S_j$ will be interchanged.

## Input data

The input file `swaps2.in` will contain on the first line the natural number $N$ representing the length of the sequence $S$. On the second line of the input file, there will be the sequence $S$ containing values of 0 or 1.

## Output data

The output file `swaps2.out` will contain on the first line the minimum number $M$ of swaps needed to sort the sequence $S$ in ascending order. The following $M$ lines will contain two numbers each, representing a pair of indices whose values were swapped.

## Constraints and clarifications

$N \leq 1000$

## Example

`swaps2.in`
```
8
01101010
```

`swaps2.out`
```
2
2 6
3 8
```