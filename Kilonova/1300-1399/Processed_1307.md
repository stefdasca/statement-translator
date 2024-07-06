```markdown
A square matrix with $N$ rows and $N$ columns, containing all natural numbers from $1$ to $N \cdot N$, is considered.

Three types of operations are defined on the matrix, encoded as follows:
* $C \ i \ j$ - swaps columns $i$ and $j$ of the matrix
* $R \ i \ j$ - swaps rows $i$ and $j$ of the matrix
* $E \ i \ j \ x \ y$ - swaps the element on row $i$ and column $j$ with the element on row $x$ and column $y$

A set of $M$ such operations will be performed on the matrix.

# Task

Determine the minimum number of complete applications of this set of operations needed to return to the initial state. Within the set, operations are always performed in the same order, and it is not possible to skip an operation. Because this number can be very large, the remainder of its division by $13 \ 007$ is required.

# Input data

The file `perspic.in` contains on the first line the natural numbers $N$ and $M$, separated by a space, representing the size of the matrix and the number of operations in a set, respectively. 

The next $M$ lines contain the descriptions of the operations in the set.

# Output data

The file `perspic.out` will contain the remainder of dividing the determined minimum number by $13 \ 007$.

# Constraints and clarifications

* $1 \leq N \leq 100$
* $1 \leq M \leq 10 \ 000$
* For $60\%$ of the tests, the minimum number of applications of the set of operations required will be less than $2 \ 000 \ 000 \ 000$

# Example 1

`perspic.in`
```
2 2
C 1 2
R 1 2
```

`perspic.out`
```
2
```

# Explanation

The initial matrix:

$$
1 \  2 \\
3 \ 4
$$

Matrix after the first operation:

$$
2  \ 1 \\
4 \ 3
$$

Matrix after the second operation (completion of the first set):

$$
4 \ 3 \\
2 \ 1
$$

Matrix after the third operation:

$$
3 \ 4 \\
1 \ 2
$$

Matrix after the fourth operation (completion of the second set):

$$
1 \ 2 \\
3 \ 4
$$

# Example 2

`perspic.in`
```
3 3
E 1 1 2 2
R 1 2
C 2 3
```

`perspic.out`
```
4
```
```