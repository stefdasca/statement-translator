
Let `N` be a non-zero natural number and `P` a permutation of length `N` of the numbers from the set `{1, 2, ..., N}`. We define a visible element in the permutation `P` as a number $P_i$ that has the property that $P_j < P_i$, for `1 \\leq j < i` or `i=1`.

# Task
Determine the number `X` of length `N` permutations that have exactly `M` given elements as visible elements.

# Input data
The input file `pviz.in` contains on the first line two natural numbers `N` and `M`, with the meaning from the statement, separated by a space. The second line of the file contains `M` distinct natural numbers, arranged in ascending order, separated by a space, representing the visible elements.

# Output data
The output file `pviz.out` will contain a single line which will print a natural number representing the remainder of the division of the number `X` by `10007`.

# Constraints and clarifications
* `1 \\leq N \\leq 2000`
* `1 \\leq M \\leq N`
* The visible elements are written in the input file in ascending order.
* For `10%` of the tests, `N \\leq 10`
* For `20%` of the tests, `N \\leq 14`
* For `60%` of the tests, `N \\leq 375`

# Example

`pviz.in`
```
4 2
2 4
```

`pviz.out`
```
3
```

There are `3` permutations, of length `4`, which have `2` and `4` as visible elements:
```
2 4 3 1
2 4 1 3
2 1 4 3
```

The permutation `2 3 4 1` does not meet the task because it has as visible elements both `2` and `4`, as well as `3`.
