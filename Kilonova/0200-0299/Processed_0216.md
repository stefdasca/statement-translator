Sure, here is the translated problem statement:

---

A matrix with `R` rows and `C` columns of distinct numbers from `1` to `R*C` is given. Bemo, the emotional character, wants to follow the best *path* from the top left corner, with coordinates `(1, 1)`, to the bottom right corner, with coordinates `(R, C)`.

A path is a sequence of numbers in the matrix where each number is found below or to the right of the previous number, i.e., if `(i, j)` is the position of a number on a path, then the next number can be the one at position `(i+1, j)` or the one at position `(i, j+1)`. To determine if a path `A` is better than a path `B`, the numbers of each path will be sorted and the smallest lexicographically will be chosen, e.g., `[1,3,5,6,8]` < `[1,4,5,6,7]`.

# Task
The input file `bemo.in` contains on the first line two natural numbers `R` and `C`, where `R` is the number of rows, and `C` is the number of columns of Bemo's matrix. On the next `R` lines, there will be `C` numbers separated by a space. Each number will be unique and will be within the interval `[1, R*C]`.

# Input data
The input file `bemo.in` contains on the first line two natural numbers `R` and `C`, where `R` is the number of rows, and `C` is the number of columns of Bemo's matrix. On the next `R` lines, each will contain `C` numbers separated by a space. Each number will be unique and will be within the interval `[1, R*C]`.

# Output data
The output file `bemo.out` will contain `R+C-1` numbers representing the best path that Bemo can choose. The numbers will be written separated by a space.

# Constraints and clarifications
* `0 < R, C < 1501`;
* For `40%` of the tests: `0 < R, C < 751`;
* For `70%` of the tests: `0 < R, C < 1301`;
* We say that a path $A=(a_1, a_2, .., a_{R+C-1})$ is lexicographically smaller than a path $B=(b_1, b_2, .., b_{R+C-1})$ if there is a position `p` such that $x_p < y_p$ and $x_1 = y_1, x_2 = y_2, ..., x_{p-1} = y_{p-1}$.

# Example:

`bemo.in`

```
4 4
7 4 13 3
8 11 12 2
10 9 1 5
16 14 15 6
```

`bemo.out`

```
7 4 11 9 1 5 6 
```

Explanations
---

The best path is the sequence `7, 4, 11, 9, 1, 5, 6`

---