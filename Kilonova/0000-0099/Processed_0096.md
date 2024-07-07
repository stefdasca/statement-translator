Sure, here is the translated text:

```
In the wake of their regional (soon to be international) success, Los Patrons (a team composed of Gustavo, Alfredo, and Estefano) have accumulated a considerable sum of money, to the point where they stumble upon it in their daily lives. Alfredo found two large stacks of money (one in his left pocket, and the other in his right pocket), so he distributed them to his two colleagues for counting, expecting them to tell him the total sum. Estefano and Gustavo thought of giving him a new challenge: finding the number of pairs of values of the two initial stacks.

For this, they will tell him an arbitrary base `B`, the total sum of money in base `B` (and the number of digits of this sum in this base), along with `M` additional properties of the digits of the values (in base `B`) of the two initial stacks. Let `a` and `b` be the value of the first and second stack respectively. The additional properties are of the type $a_i + b_j = k$, $a_i - b_j = k$, where `k` is a constant (possibly different for each property), and $a_0, ..  , a_{N-1}$ and $b_0, ... , b_{N-1}$ are the digits of the two values, where $a_0$ and $b_0$ are the least significant, and $a_{N-1}$ and $b_{N-1}$ are the most significant.

Alfredo solved this problem quite quickly, so he challenges you (in turn) to solve it as well. Knowing that the answer can be very large, it is sufficient to find only the remainder when dividing it by $10^9 + 7$.

# Task
The first line contains `3` integer numbers `N, M, B`, representing the number of digits of the values of the `2` stacks (and the sum of these values), the number of restrictions between the digits, and the numerical base. The second line contains, space-separated, the digits of the sum, from the most significant to the least significant. The next `M` lines contain the restrictions which are either of the form `i + j k` meaning $a_i + b_j = k$, or of the form `i - j k` representing $a_i - b_j = k$.

# Input data
The first line contains `3` integer numbers `N, M, B`, representing the number of digits of the values of the `2` stacks (and the sum of these values), the number of restrictions between the digits, and the numerical base. The second line contains, space-separated, the digits of the sum, from the most significant to the least significant. The next `M` lines contain the restrictions which are either of the form `i + j k` meaning $a_i + b_j = k$, or of the form `i - j k` representing $a_i - b_j = k$.

# Output data
Print a single line containing a single integer number, representing the number of possible pairs modulo $10^9 + 7$.

# Constraints and clarifications
* `1 \leq N \leq 18`
* `1 \leq M \leq 70`
* `2 \leq B \leq 10 000 000`
* Both of the `2` values and their sum have exactly `N` digits (the most significant digit of each number is non-zero).
* An additional test has been added.

## Subtask 1 (7 points)
* `1 \leq N \leq 18, M=0, B \leq 30`
## Subtask 2 (8 points)
* `1 \leq N \leq 6, B = 10`
## Subtask 3 (20 points)
* $1 \leq N \leq 18, c_i = B - 1$ for each `0 \leq i < N` and `B \leq 30`
## Subtask 4 (13 points)
* `1 \leq N \leq 18, B \leq 100`
* All restrictions are between digits of the form $a_i$ and $b_i$.
## Subtask 5 (18 points)
* `1 \leq N \leq 18, B \leq 30`
* All restrictions are of the form $a_i + b_j = k$ (no restrictions with `-`).
## Subtask 6 (11 points)
* `1 \leq N \leq 18, B \leq 30`.
## Subtask 7 (23 points)
* Without additional restrictions.

# Example

`stdin`

```
5 4 20
10 10 10 12 10
3 + 1 10
4 + 1 10
4 - 4 0
0 + 2 10
```

`stdout`

```
11
```

`stdin`

```
2 2 20
10 10
1 + 0 12
1 - 0 0
```

`stdout`

```
1
```

`stdin`

```
2 1 20
10 10
1 + 0 12
```

`stdout`

```
9
```

`stdin`

```
3 1 20
8 10 10
0 - 0 -2
```

`stdout`

```
261
```

`stdin`

```
3 1 20
10 10 8
0 - 0 -2
```

`stdout`

```
341
```

# Explanations

In this explanation, a number in base B with digits $a_k, ... , a_0$, where $a_k$ is the most significant, and $a_0$ is the least significant, is denoted as $[a_k, ... , a_0]$.

For the first example:
1. `[5, 5, 0, 7, 0] + [5, 5, 10, 5, 10]`;
2. `[5, 5, 1, 7, 1] + [5, 5, 9, 5, 9]`;
3. `[5, 5, 2, 7, 2] + [5, 5, 8, 5, 8]`;
4. `[5, 5, 3, 7, 3] + [5, 5, 7, 5, 7]`;
5. `[5, 5, 4, 7, 4] + [5, 5, 6, 5, 6]`;
6. `[5, 5, 5, 7, 5] + [5, 5, 5, 5, 5]`;
7. `[5, 5, 6, 7, 6] + [5, 5, 4, 5, 4]`;
8. `[5, 5, 7, 7, 7] + [5, 5, 3, 5, 3]`;
9. `[5, 5, 8, 7, 8] + [5, 5, 2, 5, 2]`;
10. `[5, 5, 9, 7, 9] + [5, 5, 1, 5, 1]`;
11. `[5, 5, 10, 7, 10] + [5, 5, 0, 5, 0]`.

For the second example:
1. `[6, 4] + [4, 6]`.

For the third example:
1. `[2, 0] + [8, 10]`;
2. `[3, 1] + [7, 9]`;
3. `[4, 2] + [6, 8]`;
4. `[5, 3] + [5, 7]`;
5. `[6, 4] + [4, 6]`;
6. `[7, 5] + [3, 5]`;
7. `[8, 6] + [2, 4]`;
8. `[9, 7] + [1, 3]`;
9. `[1, 19] + [8, 11]`.
