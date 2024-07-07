
A matrix of natural numbers $A$ with $N_1$ rows and $N_2$ columns is given. Determine another matrix $B$, where $B_{i_1,i_2}$ is the smallest natural number that is not found in the rectangle determined by the top-left corner $(0, 0)$ and bottom-right corner $(i_1, i_2)$ in $A$.

# Interaction Protocol
The contestant must implement a function:
```cpp
void solve(int N1, int N2, int** A, int** B);
```
Parameters $N_1$ and $N_2$ have the meaning from the statement. $A$ represents the initial matrix. The contestant must fill matrix $B$ according to the task. The elements at position $(i, j)$, where $0 \leq i < N_1$, $0 \leq j < N_2$, of matrices $A$ and $B$ can be accessed using the expressions $A[i][j]$ and $B[i][j]$, respectively.

# Constraints
* $1 \leq N_1, N_2 \leq 2\ 000$
* $0 \leq A_{i_1,i_2} \leq 4 \cdot 10^6$
## Subtask 1 (22 points)
* $N_1, N_2 \leq 100$
## Subtask 2 (27 points)
* $N_1, N_2 \leq 500$
## Subtask 3 (34 points)
* $N_1, N_2 \leq 1\ 000$
## Subtask 4 (17 points)
* Without additional constraints.

# Example
`Committee calls`
```cpp
int A[3][3] = {{0, 0, 1}, {1, 2, 3}, {0, 4, 1}};
int B[3][3];
solve(3, 3, A, B);
```

`Effect`
$B$ will be equal to `{{1, 1, 2}, {2, 3, 4}, {2, 3, 5}}`.
```

Please review and confirm the translation and formatting. If there are any additional requirements or corrections, let me know!