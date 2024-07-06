```markdown
A matrix with `m` rows and `n` columns is given, each row representing a permutation. It is known that rows from `2` to `m` are circular permutations of the first row. A row `x` `(1 \leq x \leq m)` can be applied the following operations:
- a left circular permutation: the element at position `i (1 < i \leq n)` moves to position `i-1`, except the first element, which becomes the last;
- a right circular permutation: the element at position `i (1 \leq i < n)` moves to position `i+1`, except the last element, which becomes the first.

The goal is to circularly permute the rows, to the left or right, so that eventually all rows are equal, using a minimum number of operations.

# Task
Given a matrix with the described property, the task is to determine the minimum number of operations required to obtain a matrix where all rows are equal.

# Input data
The input file `permutare.in` contains on the first line two natural numbers `n` and `m`, representing the number of columns and the number of rows of the matrix. The second line of the input file contains `n` natural numbers, representing the permutation on the first row of the matrix. On the next `m-1` lines, there is a natural number between `0` and `n-1`. The `i`-th `(0 < i < m)` of these numbers represents the number of positions with which the `(i+1)`-th row is circularly permuted to the right compared to row `1`.

# Output data
The output file `permutare.out` will contain a single natural number representing the minimum number of necessary operations.

# Constraints and clarifications
* `1 \leq n, m \leq 100 \ 000`
* Two rows in an array are equal if the elements in the same column are equal.

# Example

`permutare.in`

```
6 5
3 1 4 2 6 5
1
1
3
3
```

`permutare.out`

```
5
```
Explanation
---

The matrix will be:

```
3 1 4 2 6 5
5 3 1 4 2 6
5 3 1 4 2 6
2 6 5 3 1 4
2 6 5 3 1 4
```

If we circularly permute the first row to the right by one position, and the rows `4` and `5` to the left by two positions, we will obtain a matrix in `5` operations where all rows are equal. The rows will be determined by the permutation: `5 3 1 4 2 6`
```