You are in the year 2121 and want to configure a Neuralink network. You have `N` servers at your disposal, whose IPs are represented by permutations of length `M` (of the numbers `0, 1 ... M - 1`). You want your network to be as large as possible, but at the same time, you are afraid of potential security issues: if a hacker finds one of the IPs, it will be easy for them to find a similar IP. Therefore, out of the `N` servers you have available, you want to choose as many servers for your network such that no two servers have similar IPs. Two IPs are similar if one of them can be obtained from the other by exactly one *swap* operation (an interchange of any two elements). For example, the IPs `(0, 1, 2)` and `(1, 0, 2)` are similar, but `(0, 1, 2)` and `(1, 2, 0)` are not.

# Input data
The first line contains the numbers `N` and `M`. The next `N` lines will contain `M` numbers each, elements of the matrix `p`. Line `i` of the matrix `p` represents the `i`-th IP (a permutation of length `M`).

# Output data
The first line will print the maximum number of non-similar IPs.

# Constraints and clarifications
* `1 \leq N \leq 2\ 500`
* `1 \leq M \leq 5\ 000`
* For any `0 \leq i < n`, `p[i]` is a permutation of numbers from `0` to `M - 1`
* For any `0 \leq i < j < n`, `p[i]` and `p[j]` are distinct

## Subtask 1 (11 points)
* `N, M \leq 20`
## Subtask 2 (30 points)
* At most `20` permutations out of the `N` are similar to any other of the `N`
* `N \leq 1000`
## Subtask 3 (36 points)
* `N \leq 300`
## Subtask 4 (14 points)
* `N \leq 1000`
## Subtask 5 (9 points)
* No additional constraints.

# Examples

`stdin`

```
3 3
0 1 2
2 1 0
1 0 2
```

`stdout`

```
2
```

`stdin`

```
5 5
0 1 2 3 4
1 0 2 3 4
0 1 2 4 3
0 4 2 3 1
4 1 2 3 0
```

`stdout`

```
4
```

`stdin`

```
6 3
0 1 2
0 2 1
1 0 2
1 2 0
2 1 0
2 0 1
```

`stdout`

```
3
```

Explanations
---

For the first example, choose the servers with IPs `(2, 1, 0)` and `(1, 0, 2)`. We cannot choose the server `(0, 1, 2)` because its IP is similar to the other two.

For the second example, we can choose all IPs except the first one.

For the third example, we can select the IPs `(0, 1, 2), (1, 2, 0), (2, 0, 1)`.
