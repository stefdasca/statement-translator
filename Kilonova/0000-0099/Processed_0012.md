
A sequence `a` of `N` positive integers not exceeding `M` is given. The goal is to partition the sequence into as many stable groups as possible. A stable group is defined as a continuous and non-empty sequence of numbers $a_s, a_{s+1}, a_{s+2}, \ldots, a_{d-1}, a_d$, satisfying the following condition:
* any other element outside the interval `[s,d]` is either strictly greater or strictly less than all values in `[s,d]`.

More specifically, for any `i ∈ [s,d]`, only one of the following conditions is satisfied:
1. `a[i] < a[j]`, for any `s \leq j \leq d`;
2. `a[i] > a[j]`, for any `s \leq j \leq d`.

Partitioning the sequence implies that each number is part of exactly one group.

# Task
Given `N`, `M`, and the sequence `a` of `N` numbers, find a partition of the sequence `a` into as many stable groups as possible.

# Input data
The first line contains two numbers `N` and `M` separated by a space. The second line contains the `N` elements of the sequence `a` separated by spaces.

# Output data
In the file `compact.out`, there will be two lines. The first line will contain the maximum number of stable groups `G`, and the second line will contain `G` values, representing the position of the last element of each stable group in increasing order.

# Constraints and clarifications
* `1 \leq N \leq 1\ 000\ 000`.
* `1 \leq M \leq N`.
* `1 \leq a[i] \leq M`, for `1 \leq i \leq N`.
* For tests worth `21` points `N \leq 100`.
* For other tests worth `28` points `N \leq 3000`.
* It is guaranteed that each natural number from `1` to `M` appears at least once.
* The last index in every solution will always be `N`.
* In case there are multiple solutions with the maximum number of stable groups, the lexicographically smallest solution will be printed.
* A sequence $a_1, a_2, \ldots, a_n$ is lexicographically smaller than another sequence $b_1, b_2, \ldots, b_n$ if there exists an integer `P` less than or equal to `N` such that: $a_1 = b_1, a_2 = b_2, \ldots, a_{P-1} = b_{P-1}$, and $a_P < b_P$.
* Clarification: 3 of the tests were unavailable and have been eliminated.

# Example

`compact.in`

```
6 5
1 4 2 3 5 5
```

`compact.out`

```
5
1 2 3 4 6
``` 

`compact.in`

```
7 5
1 3 2 1 5 2 4
```

`compact.out`

```
1
7
``` 

`compact.in`

```
14 10
5 8 6 7 5 2 1 2 3 3 4 10 9 10
```

`compact.out`

```
5
5 8 10 11 14
``` 

`compact.in`

```
4 3
3 1 2 1
```

`compact.out`

```
2
1 4
``` 
