
A chessboard with `n + 1` rows (numbered from top to bottom starting at `1`) and `2n + 1` columns (numbered from left to right starting at `1`) is given. On the first row, the square in the middle contains `1` gram of hay, while the other squares on the first row contain nothing. Starting from the second row, each square contains a quantity of hay obtained by summing the hay quantities of the `3` squares of the previous row with which it neighbors (vertically and diagonally). For example, if `n = 3`, the board has `4` rows, `7` columns, and the following configuration.

~[2sah.png]

A horse starts from the first row, from a column `k \leq n`, and jumps from any position `(i, j)` to the position `(i + 1, j + 2)` as long as possible and eats all the hay from the squares it passes through. For example, for `n = 3` and `k = 2`, the squares the horse passes through are marked with asterisks (*).

# Task
1. Knowing `n` and `k`, calculate the amount of hay on the `k`-th row of the board.
2. Knowing `n` and `k`, calculate how many grams of hay a horse eats that starts from the first row, from column `k`.

Since these numbers can be large, only the remainder modulo `100003` is required for these numbers.

# Input data
The input file `2sah.in` will contain on the first line a number `t` with a value of `1` or `2`. The second line of the input file contains two natural numbers `n` and `k` separated by a space.

If `t = 1`, the first task will be solved, so for the read value `n`, the board has `n + 1` rows and `2n + 1` columns, and `k` represents the row number from where the amount of hay should be calculated.

If `t = 2`, the second task will be solved, so for the read value `n`, the board has `n + 1` rows and `2n + 1` columns, and `k` represents the column number in the first row where the horse starts.

# Output data
If `t` from the input file is `1`, only the first task will be solved.
In this case, the output file `2sah.out` will contain a single number representing the total amount of hay from all the squares located on the board on row `k` (the remainder modulo `100003` must be printed).

If `t` from the input file is `2`, only the second task will be solved.
In this case, the output file `2sah.out` will contain a single number representing the total amount of hay eaten by a horse that starts from row `1` and column `k` (the remainder modulo `100003` must be printed).

# Constraints and clarifications
* $1 \le k \le n \le 1\ 000\ 000\ 000$
* For task 1, for $80\\%$ of the tests, $k \le n \le 1\ 000\ 000$, and for the other $20\\%$ of the tests, $k \le n \le 1\ 000\ 000\ 000$.
* For task 2, for $30\\%$ of the tests, $k \le n \le 1\ 000$, for another $30\\%$ of the tests, $k \le n \le 1\ 000\ 000$, and for the remaining $40\\%$ of the tests, $k \le n \le 1\ 000\ 000\ 000$.
* A correct solution to the first task ensures $20\\%$ of the respective test score.
* A correct solution to the second task ensures $80\\%$ of the respective test score.

# Examples

`2sah.in`
```
1
3 2
```

`2sah.out`
```
3
```

`2sah.in`
```
2
3 2
```

`2sah.out`
```
2
```

Explanations
---

For the first test:
`t = 1`, so the first task is solved.
On the second row, there are `3` squares, each containing one gram of hay. (see the drawing in the statement)

For the second test:
`t = 2`, so only the second task is solved.
The horse's path is: `(1, 2) → (2, 4) → (3, 6)`, meaning exactly the squares marked with asterisks in the drawing from the statement. The first position does not contain hay, while the other two contain one gram of hay each. Therefore, the horse eats `2` grams of hay.
