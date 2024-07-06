# Task

Given are $N$ and $M$, two natural numbers, and a matrix $A$ with $N$ rows (numbered from $1$ to $N$) and $M$ columns (numbered from $1$ to $M$) having elements as integers in the closed interval $[-30\ 000, 30\ 000]$. Various operations can be performed on this matrix including deleting rows, sorting elements within specific rows, or adding new rows at the end of the matrix. Each of these operations is coded by a command with the following syntax:

**Deletion** is specified by a line of the form: $S \ i \ j \ k \ i_1 \ o_1 \ v_1 \ i_2 \ o_2 \ v_2 \ i_3 \ o_3 \ v_3 \dots i_k \ o_k \ v_k$

The command specifies that rows $L \in \{i, i+1, i+2, \dots, j \}$ will be deleted from the matrix if the following conditions are simultaneously met:

- $A_{L \ i_1}$ is in relation $o_1$ to $v_1$
- $A_{L \ i_2}$ is in relation $o_2$ to $v_2$
- $\\dots$
- $A_{L \ i_k}$ is in relation $o_k$ to $v_k$

where $o_1$, $o_2$, $\dots$, $o_k$ can be one of the operators `<` (less than), `>` (greater than), `!` (not equal), `=` (equal).

For example, the command: $S \ 3 \ 5 \ 2 \ 2 < 10 \ 5 \ ! \ 7$ specifies that rows $L \in \{3, 4, 5 \}$ will be deleted if $A_{L \ 2} < 10$ and $A_{L \ 5} \neq 7$.

After deleting all specified rows, the rows in the matrix will be renumbered, and the matrix size will be adjusted.

**Sorting** is specified by a line of the form $O \ i \ j \ t \ col_1 \ ch_1 \ col_2 \ ch_2 \ col_3 \ ch_3 \dots col_t \ ch_t$ meaning that rows $i, i+1, i+2, \dots, j$ are sorted based on the values from column $col_1$, if for two rows the values in column $col_1$ coincide, they will be sorted based on column $col_2$, then based on column $col_3$, and so on. Sorting by a specific column $col_i$ is in ascending order if $ch_i$ is `C` and in descending order if $ch_i$ is `D`. If two rows have identical values in all $t$ columns, their relative order in the original table will be preserved.

**Adding** is specified by a line of the form $A \ v_1 \ v_2 \dots v_M$ meaning that a new row is added to the end of the matrix, with the elements of the new row having, from left to right, the values $v_1 \ v_2 \dots v_M$.

# Task

Write a program that reads the elements of the initial matrix, then reads a sequence of commands and determines the resulting matrix after performing the specified operations in the given order.

# Input data

The input file `matrice.in` contains:
- The first line contains two integers, $a$ and $b$.

# Output data

The output file `matrice.out` will contain:
- The first line contains a natural number $R$ representing the number of rows of the final matrix.
- Each of the following $R$ lines contains $M$ integers, representing the elements of the final matrix. The elements on the same line are separated by a space.

# Constraints and clarifications

- $1 \leq N, R \leq 200$
- $1 \leq M \leq 100$
- $1 \leq P \leq 150$
- None of the intermediate matrices have more than $200$ rows
- The maximum number of conditions for any deletion or sorting command is $20$ ($1 \leq k, t \leq 20$)
- All commands in the input file are syntactically and logically correct, meaning, for example, that no command asks for sorting or deleting rows outside the matrix.

# Example

`matrice.in`
```
10 4
5 1 6 3
4 2 3 7
4 2 3 2
2 8 1 3
4 2 1 6
1 3 2 1
9 7 5 1
9 7 3 8
3 8 2 6
6 7 1 3
8
O 2 5 1 3 C
O 7 10 1 2 C
S 5 9 1 1 < 4
A 7 3 5 1
A 9 2 1 6
O 2 7 3 2 C 1 D 4 D
O 1 11 1 3 C
S 1 11 2 1 > 4 3 ! 5
```

`matrice.out`
```
7
4 2 1 6
2 8 1 3
3 8 2 6
4 2 3 7
4 2 3 2
9 7 5 1
7 3 5 1
```