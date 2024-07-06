```markdown
>"ok, the statements for muxusetre and 3secv are ready, I'm working on the tests for joingraf RIGHT NOW."

For an array $A$ of $N$ numbers, we define its weight as $weight(A) = \displaystyle \sum_{i \leq j}^{N} sp(i,j)$, where $sp(i,j) = \left( \displaystyle \sum_{k = i}^{j} A[k] \right) \mod M$

Sux receives an array $A$ of $N$ elements as a gift from his grandfather. One day, Sux goes on a mountain trip with his $K-1$ friends, and being very attached to the gift, he decides to take the array with him. Upon reaching the foot of the mountain, Sux realizes he cannot carry the array by himself to the top of the mountain because it is too heavy. Therefore, Sux tries to divide the array into $K$ non-empty disjoint subarrays such that each of his $K-1$ friends receives exactly one subarray (leaving exactly one subarray for Sux) and the sum of the cumulative weights is minimized.

# Task

Help Sux calculate the minimum value.

# Input data

The first line contains three integers, $N$, $K$, and $M$.
The second line contains $N$ numbers separated by a space.

# Output data

The first line will contain a number representing the answer to the problem.

# Constraints and clarifications

* If Sux divides the array into $K$ subarrays: $A_1, A_2, A_3, ..., A_k$, then the cumulative weight is $ \displaystyle \sum_{i=1}^{K} weight(A_i)$.
* Legend has it that the tests for [joingraf](https://kilonova.ro/contests/34/problems/1907) are still not ready.

| # | Score | Constraints | 
| - | ----- | ------------ |
| 1 | 10 | $N \leq 10, K \leq 10, M \leq 10$ |
| 2 | 30 | $N \leq 100, K \leq 100, M \leq 30$ |
| 3 | 10 | $N \leq 1500, K \leq 100, M \leq 2$ |
| 4 | 50 | $N \leq 5000, K \leq N, M \leq 30$ |

# Example 1

`stdin`
```
6 2 9
2 6 7 1 8 7 
```

`stdout`
```
62
```

## Explanation

If we choose to divide the array into subsequences $(1, 2)$ and $(3, 4, 5, 6)$, then the total weight will be $sp(1,1) + sp(2,2) + sp(1,2) + sp(3,3) + sp(4,4) + ... + sp(3,6) = 72$
However, if we divide the array into subsequences $(1, 2, 3)$ and $(4, 5, 6)$ we obtain the total weight $62$.

# Example 2

`stdin`
```
10 5 6
57258 79818 45081 80878 97780 67843 78314 38965 34431 9159 
```

`stdout`
```
30
```
```