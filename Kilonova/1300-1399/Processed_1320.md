```markdown
Alex and his younger brother Marian bought a bow and arrows, a target poster, and a square board (on which to stick the target poster). The board can be viewed as a square array of size $n$, and the target poster as a square array of size $m$. For $n = 6$ and $m = 5$, we have:
~[tir.png|align=center]
The sizes of the squares composing the board and the poster are equal.
The board's rows are numbered starting from $1$ from top to bottom, and the columns also start from $1$ from left to right. In the array associated with the poster, concentric squares are marked from the outside towards the inside: the outermost has each square value $1$, followed by the concentric square with square values $2$, and so forth. This means that an arrow hitting one of the specified concentric squares receives the corresponding score.
Since Alex is much more experienced than Marian, he does him a favor: he lets Marian shoot at the board $k$ times, after which he sticks the poster parallel to the edges of the board, in the position where the maximum score is obtained. The poster will be completely stuck on the board (without any parts of it extending outside the board), and so that no squares on the board are partially covered.
Each of the arrows shot by Marian hits exactly one square on the board: he does not shoot between two squares, on the edge of the board, or outside the board. For each shot, the position of the arrow on the board (row, and column respectively) is provided.

# Task

Write a program to determine the maximum score, denoted by $p$, that Marian can obtain after sticking the poster, as well as the top-left corner where the poster will be stuck (row and column on the board, denoted by $\\text{lin}$ and $\\text{col}$). If there are multiple possible positions to stick the poster resulting in the maximum score, the one with the smallest top-left corner row index should be chosen, and if there are multiple solutions with the same smallest row index, the one with the smallest column index should be chosen.

# Input data

The input file `tir.in` contains on the first line the numbers $n$, $m$, and $k$ separated by a space, and on the following $k$ lines the positions of the arrows on the board in the format: row and column separated by a space.

# Output data

The output file `tir.out` should contain on the first line $p$, and on the second line, separated by a space, the numbers $\\text{lin}$ and $\\text{col}$ from the task.

# Constraints and clarifications

* $2 < m \leq n < 301$
* $0 < k < 301$
* No partial scores are given.
* There may be multiple arrows in the same square.

# Example

`tir.in`
```
6 5 4
1 1
6 1
1 6
2 6
```

`tir.out`
```
2
1 2
```

## Explanation

By placing the poster starting with the top-left corner in the square at row $1$ and column $2$, two points are obtained corresponding to the arrows in the squares $1 6$ and $2 6$. The poster can also be placed in the squares $1 1$, $2 1$, and $2 2$ (row column), but in each of these cases, the score is $1$.
```