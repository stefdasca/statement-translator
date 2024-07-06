Given a binary matrix with rows from $0$ to $nrLin - 1$ and columns from $0$ to $nrCol - 1$, respectively $Q$ independent queries in the form $X_1, Y_1, X_2, Y_2$: *"Suppose we change all bits of $1$ to $0$ in the submatrix with the top-left corner at row $X_1$ and column $Y_1$ and the bottom-right corner at row $X_2$ and column $Y_2$. What is the total number of rows and columns of the new matrix that still have at least one bit of $1$?"*

# Interaction Protocol

The contestant will implement the function `solve`, with the following signature:
```cpp
std::vector<int> solve (int nrLin, int nrCol, int Q, 
                        std::vector<std::string> matrix,
                        std::vector<int> X1, std::vector<int> Y1, 
                        std::vector<int> X2, std::vector<int> Y2);
```
The parameters of this function have the following meaning:
* $nrLin$ the number of rows of the matrix;
* $nrCol$ the number of columns of the matrix; it is guaranteed that $1 \le nrLin \le nrCol$
* $Q$ the number of queries;
* $matrix$ the matrix on which the queries are performed;
* the arrays $X1, Y1, X2, Y2$ contain the information for the queries; these arrays each have $Q$ elements.

The function will return an STL vector containing the $Q$ numbers requested in result, in order. **The contestant will NOT implement a `main` function**.

## Subtask 1 (3 points)
* $1 \le nrCol \le 100$
* $1 \le Q \le 1\ 000$
## Subtask 2 (11 points)
* $1 \le nrCol \le 400$
* $1 \le Q \le 100\ 000$
## Subtask 3 (23 points)
* All submatrices in the queries are square $(X_2 - X_1 = Y_2 - Y_1)$
* $1 \le nrCol \le 1\ 000$
* $1 \le Q \le 1\ 000\ 000$
## Subtask 4 (24 points)
* All submatrices in the queries are square $(X_2 - X_1 = Y_2 - Y_1)$
* $1 \le nrCol \le 1\ 800$
* $1 \le Q \le 1\ 500\ 000$
## Subtask 5 (26 points)
* $1 \le Q, nrLin \cdot nrCol \le 400\ 000$
## Subtask 6 (13 points)
* $1 \le nrLin \cdot nrCol \le 3\ 240\ 000$
* $1 \le Q \le 1\ 500\ 000$

# Examples
`Input`
```
2 2 5
11
01
0 0 1 1
0 0 0 0
0 1 0 1
1 0 1 0
1 1 1 1
```
`Output`
```
0
3
4
4
3
```
`Input`
```
2 3 8
100
111
0 0 1 1
0 0 0 0
1 0 1 0
0 1 1 2
0 1 0 1
1 1 1 1
0 2 0 2
1 2 1 2
```
`Output`
```
2
4
5
3
5
4
5
4
```
`Input`
```
1 2 1
01
0 0 0 1
```
`Output`
```
0
```