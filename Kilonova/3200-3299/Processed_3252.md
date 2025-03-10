
# Task

You are given an integer $N$ and a permutation of the values from $0$ to $N-1$. Calculate the number of (contiguous) *deal* subarrays. A subarray $[l, r]$ is considered *deal* if its elements satisfy one of the following properties:

- There exists a position $i$ ($l \leq i \leq r$) such that the subarray $[l, i]$ is strictly increasing and the subarray $[i, r]$ is strictly decreasing.
- It is either strictly increasing or strictly decreasing.

# Input data

The first line contains an integer $N$, representing the size of the permutation. The second line contains $N$ distinct integers, representing the permutation of the values from $0$ to $N-1$.

# Output data

Print a single integer, representing the total number of *deal* subarrays in the permutation.

# Constraints and clarifications

* $1 \leq N \leq 1\ 000\ 000$;
* The permutation is an arrangement of values from $0$ to $N-1$, each value appears exactly once;
* For tests worth $20$ points, $N \leq 200$;
* For other tests worth $30$ points, $N \leq 5\ 000$;
* For other tests worth $50$ points, there are no additional constraints.

# Example

`stdin`
```
8
7 4 1 2 0 6 5 3
```

`stdout`
```
20
```

## Explanation

Among the *deal* subarrays are: $(7); (7, 4, 1); (1, 2, 0); (2); (0, 6); (0, 6, 5, 3)$. In total, there are $20$ *deal* subarrays.

A counterexample of a *deal* subarray is $(4, 1, 2)$.
