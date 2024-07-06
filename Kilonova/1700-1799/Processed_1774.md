Hadrianus enjoys infinite matrices generated according to certain rules. Before the first dam, he thinks about such a matrix, where the element on row $i$ and column $j$ is equal to $i$ _xor_ $j$. Hadrianus wants to determine the sum of elements for some submatrices of the matrix formed by the above rule.

A submatrix with coordinates $(L_1, C_1, L_2, C_2)$, with $1 \leq L_1 \leq L_2$ and $1 \leq C_1 \leq C_2$, is a rectangular area of the matrix that has the top-left corner at row $L_1$ and column $C_1$ and the bottom-right corner at row $L_2$ and column $C_2$.

~[xor.png|align=right]

The _xor_ operation represents the exclusive disjunction operation performed on the bits of the operands. In Pascal, the corresponding operator is `xor`, and in C/C++ this operator is `^`. For example, $20$ _xor_ $14$ = $26$. The formed matrix has the first few elements as shown in the adjacent figure.

# Task

Write a program that reads the coordinates of $T$ submatrices and displays for each of these submatrices the sum of their elements modulo $P$ (the remainder of the sum divided by $P$), where $P$ is a prime number.

# Input data

The input file `xor.in` contains on the first line $T$ and $P$, with the above significance. Each of the following $T$ lines contains $4$ natural numbers $L_1 \\ C_1 \\ L_2 \\ C_2$, separated by a space, representing the coordinates of a submatrix.

# Output data

The output file `xor.out` contains exactly $T$ lines. The line number $i$ contains the sum modulo $P$ of the elements of the $i$-th submatrix from the input file.

# Constraints and clarifications

* $1 \\leq T \\leq 20\\ 000$
* For each of the $T$ submatrices, $1 \\leq L_1 \\leq L_2 \\leq 10^8$ and $1 \\leq C_1 \\leq C_2 \\leq 10^8$
* $P$ is a prime number less than or equal to $30\\ 000$
* The rows and columns of the matrix are numbered starting from $1$
* $10$ tests will be used in evaluation.
  * For the first $2$ tests, $T \\leq 100$ and $L_2, C_2 \\leq 100$
  * For tests $3$ and $4$, $L_2, C_2 \\leq 1\\ 000$
  * For tests $5$ and $6$, $L_1 = L_2$
  * For tests $7$ and $8$, $P = 2$
  * The other two tests respect the above limits and have no special particularities
  
# Example

`xor.in`
```
5 29473
1 3 2 4
2 2 12 15
10000 10000 11000 11000
123 51 54667341 1878099
1234567 1234567 1234678 1234678
```

`xor.out`
```
14
1165
23799
18591
549
```

## Explanation

The first submatrix is formed by elements $2$, $5$, $1$ and $6$. The sum modulo $29\\ 473$ of these elements is: $(2 + 5 + 1 + 6) \\ \\% \\ 29\\ 473 = 14$.