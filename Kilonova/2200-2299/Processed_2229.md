
# Task

Given an integer $N$ and a permutation of the set $(1, 2, \dots, N)$. A subarray $[i, j]$, $(i \leq j)$ contains all elements of the permutation found between positions $i$ and $j$ inclusively. A subarray is called a compact interval if its elements form a set of consecutive values (not necessarily in the order in the permutation). For example, for the permutation $1 \ 2 \ 6 \ 4 \ 5 \ 3$, the subarrays $6 \ 4 \ 5$ and $2 \ 6 \ 4 \ 5 \ 3$ are compact intervals, while the subarrays $1 \ 2 \ 6$ and $2 \ 6 \ 4 \ 5$ are not compact intervals. Determine the number of compact intervals in the given permutation.

# Input data

The input file `intervale.in` contains on the first line the integer $N$. The following $N$ lines contain one integer each from the given permutation.

# Output data

The output file `intervale.out` contains a single integer representing the total number of compact intervals in the given permutation.

# Constraints and clarifications

* $1 \leq N \leq 200\ 000$
* For $20\%$ of the tests, $N \leq 2\ 000$
* For $60\%$ of the tests, $N \leq 35\ 000$
* Intervals containing a single element will also be counted.

# Example

`intervale.in`
```
6
1 2 6 4 5 3
```

`intervale.out`
```
13
```

## Explanation

The 13 compact intervals in the example are:
* $1$
* $1 \ 2$
* $1 \ 2 \ 6 \ 4 \ 5 \ 3$
* $2$
* $2 \ 6 \ 4 \ 5 \ 3$
* $6$
* $6 \ 4 \ 5$
* $6 \ 4 \ 5 \ 3$
* $4$
* $4 \ 5$
* $4 \ 5 \ 3$
* $5$
* $3$
