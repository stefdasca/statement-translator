Desiring to get hired, Arius M. had to go through an interview where he received the following simple problem: given `N` sorted arrays of integers, determine the longest common subsequence of these arrays.

# Task
Solve this problem which Arius M. found quite easy.

# Input data
The first line of the file `ausoara.in` contains `N`, the number of arrays. The next `N` lines describe the `N` arrays. Line `i` contains $M_i$, the number of elements in the current array, followed by $M_i$ numbers, representing the elements of array `i`.

# Output data
The file `ausoara.out` will contain on the first line `T`, the number of elements of the longest common subsequence of the `N` arrays. Followed by `T` integers describing the elements of the longest common subsequence.

# Constraints and clarifications
* `0 < N < 101`
* $0 < M_i < 1001$
* If we have an array of numbers $a_1, a_2, \ldots, a_n$ then we call a subsequence an array of the form $a_{i_1}, a_{i_2}, \ldots, a_{i_k}$ with $i_1, i_2, \ldots, i_k$ belonging to the set `{1, 2, \ldots, n}` and $i_1 < i_2 < \ldots < i_k$.
* The elements of the arrays are integers in the range `[1, 1000000]`.
* The elements of each array are in ascending order.
* For `60%` of the tests, the elements of each array are distinct.
* For `90%` of the tests, the elements of the arrays are in the range `[1, 10000]`.

# Examples:

`ausoara.in`

```
1
3 1 2 3
```

`ausoara.out`

```
3 1 2 3
```

`ausoara.in`

```
2
2 1 2
2 2 3
```

`ausoara.out`

```
1 2
```

`ausoara.in`

```
3
6 1 2 2 3 5 5
9 2 2 2 2 2 5 5 5 7
9 2 2 2 4 5 7 7 7 7
```

`ausoara.out`

```
3 2 2 5
```

`ausoara.in`

```
3
3 1 2 3
3 4 5 6
3 7 8 9
```

`ausoara.out`

```
0
```

`ausoara.in`

```
3
3 1 1 1
1 1
2 1 1
```

`ausoara.out`

```
1 1
```