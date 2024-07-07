
A matrix $A$ = $(a_{i, j})$, $1 \leq i, j \leq n$ (a square matrix of order $n$ with rows and columns indexed from $1$ to $n$) is given.
The task is to construct a matrix $B = (b_{i, j})$, $1 \leq i, j \leq n$ with the following properties:

* $(a_{i,j}) \leq (b_{i,j})$, $\forall 1 \leq i, j \leq n$
* $(b_{i,j}) + (b_{i+1, j+1}) = (b_{i+1,j}) + (b_{i,j+1})$, $\forall\ 1 \leq i, j \leq n - 1$ (a matrix with this property is called a balanced matrix)
* The sum of the elements in the matrix $B$ is minimal. (any matrix that satisfies the first two conditions has the sum of the elements greater than or equal to the sum of the elements in matrix $B$).

# Task

Given an arbitrary matrix with natural number elements, determine another balanced matrix with natural number elements that meet the conditions in the statement.

# Input Data

The input file `echilibrare.in` will contain on the first line the number $n$ as defined in the statement. There will follow $n$ lines, each containing $n$ natural numbers separated by a space. The $n$ lines contain the elements of the corresponding rows of the initial matrix.

# Output Data

The output file `echilibrare.out` will contain on the first line a single number representing the sum of the elements of the required balanced matrix. The next $n$ lines will contain $n$ natural numbers separated by space representing the elements of the found balanced matrix.

# Constraints and clarifications

* $1 \leq n \leq 50$
* The elements in the initial matrix are natural numbers with values less than or equal to $35\ 000$.
* The elements in the final matrix are natural numbers and their value can exceed $35\ 000$.
* If there are multiple correct solutions, any of them may be displayed.
* If only the correct sum is determined, $60$ points will be awarded.

# Example

`echilibrare.in`
```
4
1 1 1 1
1 1 1 1
1 1 1 0
1 1 1 1
```

`echilibrare.out`
```
16
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1
```

## Explanation

The matrix in the output file has a sum of elements $16$, each element is greater than or equal to the corresponding element of the matrix in the input file, it is balanced and has the minimal possible sum of elements.
