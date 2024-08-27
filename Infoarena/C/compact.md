## Task

Let $P$ be a permutation with $N$ elements. A sequence of elements that are on consecutive positions in the permutation is called a subarray of the permutation. A subarray of at least 3 elements is compact if and only if the first element of the subarray is the minimum, while the last element is the maximum relative to all elements in the subarray. Determine the number of compact subarrays for the permutation $P$.

## Input data

The input file `compact.in` contains on the first line $N$, the number of elements in the permutation. The second line of the file contains $N$ distinct natural numbers, representing the elements of the permutation.

## Output data

The output file `compact.out` will contain a single natural number representing the number of compact subarrays of the permutation.

## Constraints and clarifications

$3 \leq N \leq 1\ 000\ 000$

## Example

`compact.in` 
```
8 
3 2 7 5 4 8 1 6 
```

`compact.out` 
```
1 
```

## Explanation

The only compact subarray is $(2, 7, 5, 4, 8)$. This subarray is compact because the first element, $2$, is the minimum, and the last element, $8$, is the maximum among the numbers in the subarray.