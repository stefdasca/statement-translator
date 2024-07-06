# We call a Sudoku table a matrix with $n^2$ elements that contains only the digits $1$, $2$, and $3$ such that in each square formed by $2 \times 2$ adjacent elements, all $3$ digits exist and any two adjacent elements in a row or column are distinct. Each Sudoku table $i$ is associated with a number obtained by writing the digits in order, starting with the first line.

~[image.png|align=right]

For example, the Sudoku table in the adjacent image is associated with the number: 2132132132213211321321321.

The sequence $S(n)$ is defined as an ordered sequence consisting of all Sudoku tables with $n^2$ elements, {$s_1, s_2, s_3, \cdots$}. For any pair $(s_i, s_j)$ in $S(n)$ with $i \lt j$, the number associated with Sudoku table $s_i$ is strictly less than the number associated with Sudoku table $s_j$.

For $n = 2$, the sequence $S(2)$ contains, in order, the Sudoku tables:

~[image2.png|align=left]

# Task

Given two natural numbers $n$ and $k$, determine:

- the number of Sudoku tables in the sequence $S(n)$;
- the Sudoku table at position $k$ in the sequence $S(n)$.

# Input data

The file `sudoku.in` contains on its first line two natural numbers $n$ and $k$ separated by a space.

# Output data

The output file `sudoku.out` will contain:

On the first line, a natural number representing the number of Sudoku tables in the sequence $S(n)$.
On the next $n$ lines, there will be $n$ digits, separated by a space, representing, in order, the lines of the Sudoku table at position $k$ in the sequence $S(n)$.

# Constraints and clarifications

* $2 \leq n \leq 32$;
* $1 \leq k \lt 10^{19}$;
* For correctly solving the first task, $20\%$ of the score is awarded, and for correctly solving the second task, $80\%$ of the score is awarded.
* Points for the second task are awarded only if there is an answer for the first task in the output file, regardless of its correctness.

# Example

`sudoku.in`
```
2 6
```

`sudoku.out`
```
12
2 1
3 2
```

## Explanation

The sequence $S(2)$ contains $12$ Sudoku tables, with the table at position $6$ in the sequence being:
 
- $ \begin{pmatrix} 2 & 1 \\ 3 & 2 \end{pmatrix} $