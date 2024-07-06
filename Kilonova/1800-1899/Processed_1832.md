Here's the translated text:

A matrix of natural numbers with $N$ rows and $M$ columns is given. Through a transformation, we can obtain another matrix with $N$ rows and $M$ columns as follows: each element with coordinates $(i, j)$ for $0 \leq i < N$, $0 \leq j < M$, in the newly obtained matrix will be equal to the **xor sum** of the values at the following four positions $(i, j)$, $(i+1, j)$, $(i, j+1)$, $(i+1, j+1)$ in the initial matrix (if any of these positions are outside the matrix, the value at that position will be considered $0$).

# Task
Given a matrix with $N$ rows and $M$ columns, answer queries of the form: what is the value in the first row and first column if we apply $K$ transformations to the initial matrix.

# Interaction
You must implement the functions
```cpp
void initialize(int N, int M, int **matrix);
```
The function receives as parameters the dimensions of the matrix and the matrix itself. It should not return anything.
```cpp
int query(int K);
```
The function receives the value $K$ as a parameter for a query and should return the answer to the query, as described in the statement. The [Interactor](lgrader.cpp) will read data from the input file `xortransform.in` and display the answers to the `query` function in the output file `xortransform.out` in the format observable in the example.

# Constraints and clarifications
* $1 \leq N \times M \leq 2\ 500\ 000$
* $1 \leq matrix[x][y] \leq 2^{30}$, for any $0 \leq x < N$ and $0 \leq y < M$.
* $1 \leq K \leq 1\ 000\ 000\ 000$
* The `query` function will be called at most $1\ 000\ 000$ times during a test.

# Example
`xortransform.in`
```
4 5 3
9 8 1 3 6
1 2 5 2 5
3 4 3 7 7
7 8 3 5 1
3
18
100
```
`xortransform.out`
```
13
8
15
```

Explanations
---
Input data format
```
N M Q
A0,0 A0,1 … A0,M-1
A1,0 A1,1 … A1,M-1
…
AN-1,0 AN-1,1 … AN-1,M-1
K1
K2
…
KQ
```