As always, Toronaga-san has decided to pester Paisen today as well. To this end, after classes, she randomly pulls out a competitive programming problem to confront Paisen with. As usual, Paisen struggles with this and doesn't know how to solve the problem, but maybe you can help him.

Given is a sequence `P` of $2^{10}$ numbers, indexed from `0`. Additionally, a matrix `A` of `N` by `M`, also indexed from `0`, where $0 \leq A[i][j] < 2^{10}$. We define `S(i, j, k, l)` as the bitwise OR of the continuous rectangular submatrix of `A` that starts at row `i` and column `k` and ends at row `j` and column `l`. The following sum is required:
$ \displaystyle v(S) = \left(\sum_{0 \leq i \leq j < N } \sum_{0 \leq k \leq l < M } P[S(i,j,k,l)]\right) \mod 10^9 + 7$,

In other words: consider the bitwise OR of all continuous rectangular submatrices of `A`. If these values are $v_1, ... , v_K$ where `K` is the number of continuous rectangular submatrices of A, compute $P[v_1] + ... + P[v_K]$ mod $10^9 + 7$.

# Task
Compute the result `v(S)`.

# Input data
The first line contains 2 integers `N M` which represent the number of rows and columns of matrix `A`, respectively. The next line contains the elements of the sequence `P` separated by spaces. The subsequent `N` lines contain `M` elements separated by spaces, representing matrix `A`.

# Output data
Print on a single line the required result, `v(S)`.

# Constraints and clarifications
* `N \cdot M \leq 2 000 000`.
* $0 \leq P[i] \leq 10^9$.
* `P` always has a length of $2^{10}$.
## Subtask 1 (3 points)
* `N, M \leq 20`
## Subtask 2 (4 points)
* `N, M \leq 100`
## Subtask 3 (9 points)
* `N = 1`
## Subtask 4 (9 points)
* Each `A[i][j]` is chosen uniformly and independently from ${0, ... , 2^{10} - 1}$.
## Subtask 5 (17 points)
* `P[i] = i`
## Subtask 6 (11 points)
* `N, M \leq 600`
## Subtask 7 (47 points)
* No additional constraints.

# Examples

`stdin`

```
3 3
0 1 2 ... (up to 1023)
1 2 3
1 2 3
1 2 3
```

`stdout`

```
90
```

`stdin`

```
4 5
0 1 2 ... (up to 1023)
537 152 39 245 765
487 748 533 897 881
980 571 568 972 894
88 901 637 47 822
```

`stdout`

```
134162
```
