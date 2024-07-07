
A matrix with `N` rows and `M` columns containing only lowercase letters of the English alphabet is given. A *room* is defined as a maximal area of cells in the matrix that contain the same letter, connected in all `4` directions: *up, down, left, right*.

We are interested in answers to questions of the form: "How many rooms are included completely or partially in a given rectangle, viewed as a submatrix?"

# Input data
The first line of the input file `camere.in` will contain `2` numbers `N` and `M` separated by a space, and on the next `N` lines, there will be `M` characters from the English alphabet (not separated by spaces). Line `N + 2` will contain a number `Q` representing the number of queries, and the next `Q` lines will contain `4` numbers `x1, y1, x2, y2` separated by a space, representing a rectangle defined by the diagonal opposite points of coordinates `(x1, y1)` and `(x2, y2)`.

# Output data
The output file `camere.out` will contain `Q` numbers, each on a separate row, representing the answers to the questions in the order they were given in the input file.

# Constraints and clarifications
* `1 \leq N, M \leq 2 000`
* `1 \leq Q \leq 5 000`
* `1 \leq x1 \leq x2 \leq N`
* `1 \leq y1 \leq y2 \leq M`
* For `52` out of `100` points, it is guaranteed that any room can be completely included in any query rectangle (i.e., any room can be translated to be inside that rectangle).

# Example
`camere.in`
```
5 6
aabbcc
abbbcc
cbeaed
adeeed
affttz
3
1 1 5 6
2 1 4 5
3 3 5 6
```
`camere.out`
```
12
8
6
```

Explanations
---
We have `3` queries

Query `1 1 5 6` refers to the whole matrix, which has `12` rooms.

The rectangle `2 1 4 5` contains `8` rooms, of which `4` are complete and the other `4` are incomplete.

The rectangle `3 3 5 6` contains `6` rooms, of which `5` are complete and one room is incomplete.
```

Make sure to check for translation accuracy and syntax correctness according to the rules of the English language.