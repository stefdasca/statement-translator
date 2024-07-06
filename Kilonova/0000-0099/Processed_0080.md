~[polihroniade.png|align=right]

A square matrix of dimensions `N \times N` with even `N` and elements from the set `{0, 1}` is called a **chessboard** if any two adjacent cells in a row or column have different values (in other words, if there are no two equal adjacent values).

For her birthday, Victor bought Elisabeta such a matrix `A`, which is not *necessarily* a chessboard. Learning about her passion, he now wants to transform the matrix `A` into a chessboard. Since time is limited, he can only perform the following types of operations on the matrix:

- Swap the rows `i` and `j` in `A` (the other rows remain unchanged, and the values within the rows `i` and `j` remain unchanged and maintain their order). The operation makes sense for `1 \leq i, j \leq N`.
- Swap the columns `i` and `j` in `A` (the other columns remain unchanged, and the values within the columns `i` and `j` remain unchanged and maintain their order). The operation makes sense for `1 \leq i, j \leq N`.

Wishing to impress Elisabeta, Victor appeals to you, renowned programmers, to help him transform the matrix `A` into a chessboard. For this, Victor needs the following information:
- Can the matrix `A` be transformed into a chessboard?
- What is the minimum number of operations required to achieve this?
- What would be a sequence of operations that transforms the matrix `A` into a chessboard?

In the case of the last task, to gain Victor's favor, the number of operations performed must be minimal. However, even a non-minimal number of operations will be rewarded, though not as much.

You are given two numbers `P, T` and `T` matrices `A`, representing multiple instances of the problem. For each matrix `A` of the `T`, you will have to solve the task number `P ∈ {1, 2, 3}` from those listed above.

# Input data
The first line contains two positive integers `P` and `T`, representing the task number to solve and, respectively, the number of scenarios for which you will have to solve the problem.
Next are the `T` instances of the problem, each composed of `N + 1` lines: the first line contains the number `N`, and on the following `N` lines are `N` binary digits **not separated** by spaces, representing a row of the matrix `A`.

# Output data
For each of the `T` instances the response will be printed, starting from a new line, as follows:

1. If `P = 1`, then print on a single line `1` if the matrix `A` can be transformed into a chessboard, and `0` otherwise.
2. If `P = 2`, then print on a single line an integer representing the minimum number of row and/or column swaps needed to transform the matrix `A` into a chessboard.
3. If `P = 3`, then print a line with a number `X`. Then, on each of the following `X` lines print a swap of rows or columns, in the following format: `L i j` means rows `i` and `j` are swapped, and `C i j` means columns `i` and `j` are swapped. The matrix obtained after applying the `X` operations on `A` in the given order must be a chessboard.

# Constraints and clarifications
* `1 \leq T \leq 350`
* `1 \leq N \leq 1000`
* `N` is even.
* For tasks of type `P = 2` and `P = 3`, it is guaranteed that the matrix `A` can be transformed into a chessboard using row and/or column swaps.
* The sum of the values of `N` for the `T` scenarios does not exceed `2000`.

## For 40 points
* `P = 1`
## For another 34 points
* `P = 2`
## For another 26 points
* `P = 3`
* If there are multiple solutions, any is considered correct.
* If the number `X` of operations used is not minimal, then `50%` of the score on the test is awarded.

# Example

`stdin`

```
1 3
2
11
11
4
1100
1100
0011
0011
2
10
01
```

`stdout`

```
0
1
1
```

`stdin`

```
2 2
4
1100
1100
0011
0011
2
10
01
```

`stdout`

```
2
0
```

`stdin`

```
3 2
4
1100
1100
0011
0011
2
10
01
```

`stdout`

```
3
L 2 4
C 2 3
L 1 2
0
```

Explanations
---

For the first example, we have `P = 1`, so for the `T = 3` instances, it is only asked whether they can be transformed into a chessboard by swapping rows and/or columns. For the first instance, this is **not** possible, because there are no `0`s in the matrix. For the second instance, we can perform the following operations:
~[polihroniade-2.png]
For the last instance, the matrix `A` is already a chessboard.

For the second example, we have `P = 2`, so for the `T = 2` instances, the minimum number of operations needed to transform them into a chessboard is requested. For the first instance, a solution with `2` operations is presented above, and there are no shorter solutions. For the second instance, the matrix is already a chessboard, so the answer is `0`.

The third example is exactly like the previous one, only that we have `P = 3`, so we need to print exactly what operations bring the matrix to the chessboard form. For maximum points on this example, it would be mandatory to print a solution with `2` operations (i.e., minimum number), such as the one above. However, for demonstration purposes, we present a solution composed of `3` operations, **which earns us only `50%` of the score**:
~[polihroniade-3.png]