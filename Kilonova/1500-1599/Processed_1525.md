```markdown
Dan is a big fan of fruits, with grapes and watermelons being among his favorites. However, recently he has also discovered his passion for vegetables, especially tomatoes, but most of all small tomatoes. Luckily for him, his grandfather's garden is full of tomatoes.
The garden is in the shape of a matrix with $N$ rows and $M$ columns with natural numbers, not necessarily distinct, where each element in the matrix represents the size of a tomato. The matrix has the property that any column has values in ascending order from top to bottom, i.e., from the first to the last row. His grandfather asks him to solve $Q$ tasks. For each task, Dan receives a natural number $x$ and must find a maximum area submatrix that starts from the first row of the matrix representing the garden and has all elements less than or equal to $x$. In determining the required submatrix, Dan is allowed to move all values from one column in front of any other column. Additionally, he is allowed to perform any number of such moves.

# Task

Calculate the maximum area of a submatrix that meets the specifications in the statement, for each of the $Q$ tasks given by his grandfather.

# Input data

The file `rosiimici.in` contains on the first line three natural numbers $N$, $M$, and $Q$ separated by a space, having the meaning from the statement.
Each of the next $N$ lines contains $M$ natural numbers separated by a space, representing the values of the matrix.
The following $Q$ lines each contain a natural number $x$, representing the size of a tomato.

# Output data

The file `rosiimici.out` will contain on the first $Q$ lines a single natural number, representing the required maximum area for each task, in the order that they appear in the input file.

# Constraints and clarifications

* $1 \leq N, M \leq 1 \ 000$
* $1 \leq Q \leq 100 \ 000$
* $1 \leq A[i][j] \leq N \cdot M, 1 \leq i \leq N, 1 \leq j \leq M$
* $1 \leq x \leq N \cdot M$

# Example

`rosiimici.in`
```
3 4 3
1 9 6 2
1 10 10 4
7 15 10 6
6
10
9
```

`rosiimici.out`
```
4
9
6
```

## Explanation

For the first task, Dan moves the first column in front of the fourth column obtaining the matrix:
~[poza1.jpg]
He then chooses the submatrix with the top left corner at $(1,3)$ and the bottom right corner at $(2, 4)$. Its area is $4$.

For the second task, Dan moves the first column in front of the third column obtaining the matrix:
~[poza2.jpg]
The solution is the submatrix with the top left corner at $(1,2)$ and the bottom right corner at $(3, 4)$. Its area is $9$.

For the third task, Dan moves the last column in front of the first column, obtaining the matrix:
~[poza3.jpg]
The solution is the submatrix with the top left corner at $(1,1)$ and the bottom right corner at $(3, 2)$. Its area is $6$.
```
