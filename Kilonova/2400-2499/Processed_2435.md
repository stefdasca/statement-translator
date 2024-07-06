```markdown
Given a matrix $A$ with integers that has $N$ rows and $M$ columns, indexed from $1$.

A submatrix of matrix $A$ is a matrix formed from all elements in rows with indices $x_1, x_1+1, \dots, x_2$ and columns with indices $y_1, y_1+1, \dots, y_2$ from matrix $A$, where $1 \leq x_1 \leq x_2 \leq N$ and $1 \leq y_1 \leq y_2 \leq M$.

# Task
Calculate the number of submatrices of $A$ for which the **greatest common divisor** of their elements is $1$ (the **greatest common divisor** of a set of numbers is the largest number that all of them divide exactly).

# Input data
The first line of input contains two integers $N$ and $M$, representing the number of rows and columns of matrix $A$.
Each of the following $N$ lines contains $M$ integers, where the element with index $j$ from line $i$ in the input represents the element $A[i][j]$ from the matrix (each dimension of the matrix is indexed from $1$).

# Output data
Print a single line with an integer: the number of submatrices of $A$ for which the **greatest common divisor** of their elements is $1$.

# Constraints and clarifications

* $1 \leq N , M \leq  800$
* $1 \leq A[i][j] \leq 400$

| # | Score | Constraints | 
| - | ----- | ------------ |
| 1 | 10 | $N, M < 16$ |
| 2 | 25 | $N, M < 64$ |
| 3 | 25 | $N , M < 128$ and $\\max\\{A[i][j]\\} < 64$|
| 4 | 25 | $\\max\\{A[i][j]\\} < 4$|
| 5 | 15 | No additional constraints. |

# Example

`stdin`
```
2 2
1 2
3 4
```

`stdout`
```
5
```

## Explanation

In the given example, a submatrix for which the **greatest common divisor** of its elements is $1$ is the entire matrix.

```