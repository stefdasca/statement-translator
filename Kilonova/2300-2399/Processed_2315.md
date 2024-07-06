Here is the translated text according to your specifications:

---

Consider a matrix $A$ with $N$ rows and $N$ columns with distinct elements from the set $ \{0, 1 , \dots, N^2-1 \}$. The rows and columns are numbered from $0$ to $N-1$.

We denote with $colmax(i)$ the column containing the maximum element on row $i$ of the matrix. We say that the matrix $A$ is **monotonic** if for any $i_1 < i_2$, $colmax(i_1) \leq colmax(i_2)$.

Let $L= \{ L_1, L_2, \dots, L_k \}$ be a subset of rows of the matrix, and $C= \{ C_1, C_2, \dots, C_p \}$ be a subset of columns. A submatrix of matrix $A$ consists of elements $A_{i, j}$, where $i \in L$ and $j \in C$.

We say that the matrix $A$ is **totally monotonic** if any of its submatrices is monotonic.
For example, the matrix in Figure $1$ is **totally monotonic**, with maximum values on each row bolded. The matrix in Figure $2** is **not totally monotonic** (we have shaded the elements of a submatrix that is not **monotonic**).

~[matrix.png]

# Task

Consider a totally monotonic matrix with $N$ rows and $N$ columns containing distinct values from the set $ \{0, 1 , \dots, N^2-1 \}$. Determine the column containing the maximum element for each row of the matrix.

# Interaction

Your program will not read or write anything. Instead, it will implement the function
```cpp
std::vector<int> solve(int N);
```
which receives as parameter the natural number $N$, representing the dimension of the matrix, and returns an array (indexed from $0$) that will contain, in order, the columns containing the maximum values from rows $0, 1, \dots, N-1$.

Within the `solve` function, you can call the function
```cpp
int query(int lin, int col);
```
which will return the value present in the matrix at row $lin$ and column $col$.

# Constraints and clarifications
* $1 \leq N \leq 100$;
* If your program performs at most $6 \cdot N$ queries, it will receive the maximum score for that test.
* If your program performs more than $6 \cdot N$ queries but not more than $10 \cdot N$ queries, you will receive $50\%$ of the test score.
* If your program reaches the correct result but uses more than $10 \cdot N$ queries, you will receive $20\%$ of the test score.
* If your program does not reach the correct answer or does not interact correctly with the committee's program, you will receive $0$ points for that test.
* You need to include the file `matrix.h`.

# Example interaction

`solve(2)` is called.
In `solve`, `query(0, 0)` is called, which returns $3$.
In `solve`, `query(1, 1)` is called, which returns $2$.
The `solve` function returns $ \{0, 1\}$.

---