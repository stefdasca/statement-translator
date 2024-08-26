Addk

## Task

Consider an array $A$ with $N$ natural number elements $A_1, \dots, A_N$ and a natural number $K$. You are asked to process $Q$ queries of the following two types:
1. $i_1, i_2, \dots, i_K$: perform a left circular permutation on the elements $A_{i_1}, \dots, A_{i_K}$ of the array. Thus, the new values of elements $A_{i_1}, A_{i_2}, \dots, A_{i_{K-1}}, A_{i_K}$ will be $A_{i_2}, A_{i_3}, \dots, A_{i_K}, A_{i_1}$. Note that $i_1, i_2, \dots, i_k$ are distinct and not necessarily in increasing order.
2. $l, r, m$: calculate the sum of the elements of all continuous subarrays of length $m$ from the sequence $A_l, A_{l+1}, \dots, A_{r-1}, A_r$. Note that elements appearing in multiple subarrays will be summed multiple times.

## Input data

The first line of the input file `addk.in` contains two integers, $N$ and $K$. The second line contains $N$ integers: the elements of the array $A$. The third line contains an integer $Q$, the number of queries, and then $Q$ lines containing the queries, which can be of the two types described above.

## Output data

The output file `addk.out` must contain the answers to the type 2 queries, one per line.

## Constraints

$0 \leq A_i \leq 10^6$

$1 \leq l \leq r \leq N$

$1 \leq m \leq r - l + 1$

Additionally:

## Constraints and clarifications

1. $1 \leq N, Q \leq 10,000, K = 1$
2. $10,001 \leq N, Q \leq 100,000, K = 1$
3. $1 \leq N, Q \leq 100,000, 2 \leq K \leq 10$

## Example

`addk.in`
```
8 3
7 2 5 1 9 3 4 6
3
2 2 7 4
1 2 5 8
2 2 7 3
```

`addk.out`
```
52
50
```

## Explanation

The first query is of type 2 and requires the calculation of the sum of all subarrays of length $m = 4$ from the sequence $2, 5, 1, 9, 3, 4$. These subarrays are $(2, 5, 1, 9), (5, 1, 9, 3), (1, 9, 3, 4)$, and the sum of their elements is $52$. The second query is of type 1 and results in a circular permutation of the array elements located at positions $2, 5, 8$. Thus, array $A$ becomes $7, 9, 5, 1, 6, 3, 4, 2$. The third query is of type 2 and requires the calculation of the sum of all subarrays of length $m = 3$ from the sequence $9, 5, 1, 6, 3, 4$. These subarrays are $(9, 5, 1), (5, 1, 6), (1, 6, 3), (6, 3, 4)$, and the sum of their elements is $50$.