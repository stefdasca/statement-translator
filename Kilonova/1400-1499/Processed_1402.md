```markdown
Consider a sequence $a_1, a_2, \ldots, a_N$ of natural numbers. The sequence is divided into four subarrays such that any element from the sequence belongs to only one subarray and each subarray contains at least two elements. Specifically, three indices $i < j < k$ are identified so that the first subarray consists of elements $a_1, a_2, \ldots, a_i$, the second subarray of elements $a_{i+1}, a_{i+2}, \ldots, a_j$, the third subarray of elements $a_{j+1}, a_{j+2}, \ldots, a_k$ and the last subarray of elements $a_{k+1}, a_{k+2}, \ldots, a_n$. For each subarray, its cost is determined as the difference between the maximum value and the minimum value in that subarray.

# Task

Determine a partition of the sequence into four subarrays such that the sum of the costs of the four subarrays is maximum.

# Input data

The file `split.in` contains the natural number $N$ on the first line. The second line contains $N$ natural numbers, separated by a space, representing the elements of the array $a$.

# Output data

The file `split.out` contains a single natural number on the first line representing the maximum sum of the costs of the four subarrays. The second line contains three natural numbers $i$, $j$, and $k$, separated by a space, with the meaning given in the statement.

# Constraints and clarifications

* $8 \leq N \leq 5 \ 000$
* $0 \leq a_i \leq 100\ 000\ 000$, for any $i = 1, 2, \dots, N$
* A subarray can have a cost of $0$ (maximum value equal to minimum value).
* If there are multiple solutions with the same maximum sum, then choose the solution with the smallest $i$. If there are multiple solutions with the same minimum $i$, choose the one with the smallest $j$, and if there are multiple solutions with the same minimum $i$ and $j$, choose the one with the smallest $k$.

# Example

`split.in`
```
11
9 7 3 0 2 1 8 6 0 11 4
```

`split.out`
```
29
4 7 9
```

## Explanation

The 4 subarrays are:

$(9, 7, 3, 0)$ (cost $9 - 0 = 9$)

$(2, 1, 8)$ (cost $8 - 1 = 7$)

$(6, 0)$ (cost $6 - 0 = 6$)

$(11, 4)$ (cost $11 - 4 = 7$)

Another solution that achieves the same maximum sum of $29$ is $i = 5$, $j = 7$, $k = 9$, but it does not have the minimum $i$.
```