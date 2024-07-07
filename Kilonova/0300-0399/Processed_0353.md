
A rectangular swimming pool of $N$ meters in length and $M$ meters in width is divided into $N \times M$ zones of $1 m^2$. Such a zone has the same depth over its entire surface of $1 m^2$, but two different zones may have different depths. The depths of the zones, expressed in meters ($m$), are positive natural numbers and are stored in a matrix $A$ with $N$ rows and $M$ columns.

Due to the constructive restrictions of the pool, the matrix $A$ must be *well-defined*, in the sense that for all $2 \times 2$ submatrices **formed by consecutive rows and columns** of the matrix $A$, the numbers on either of the two diagonals are not both smaller than each of the other two elements. In accordance with the laws of physics, if a zone in the pool contains water, the water tends to distribute in the adjacent zones vertically and horizontally that have depth below the water level.

The owner wants to save water. Considering the demand from the public, he does not need to fill the whole pool, but at least a rectangular area with $K$ zones in length and $K$ zones in width, where $K \leq N$ and $K \leq M$. The area filled with water can be located anywhere in the pool. The depth of the water in the filled area must be at least $1 m$ at every point. The owner wants to find $X$, the minimum amount of water needed for this purpose.

For example, for the pool represented in the matrix $A$ below and $K = 2$, $X = 6 m^3$ of water is needed, and the covered area is given by the $5$ zones whose depth is written in color.
$ A = \begin{bmatrix}
    1 & \textcolor{red}{\textbf 2} & \textcolor{red}{\textbf 3} & 1 \\
    1 & \textcolor{red}{\textbf 2} & \textcolor{red}{\textbf 2} & 1 \\
    1 & \textcolor{red}{\textbf 2} & 1 & 1 \\
\end{bmatrix} $

# Task
Write in $\\text{C}$ or $\\text{C++}$:
1) a function `verifica` with parameters $A$, $N$, $M$ that determines if $A$ is well-defined as described above (the function returns $0$ or $1$; assume that $A$ contains only positive natural numbers);
2) a function `complet` with parameters $A$, $N$, $M$ that returns the amount of water needed to fill **the whole** pool with water of at least $1 m$ depth (do not validate input data);
3) a function `optim` with parameters $A$, $N$, $M$, and $K$ that returns $X$, the minimum amount of water needed (do not validate input data).

The function headers described above are as follows:
```cpp
bool verifica(int A[101][101], int N, int M);
int complet(int A[101][101], int N, int M);
int optim(int A[101][101], int N, int M, int K);
```

# Constraints and clarifications
- $1 \leq N, M \leq 100$
- It is guaranteed that the sum of the elements of the matrix $A$ is $\leq 10^9$.
- The matrix $A$ is indexed from $1$.
- Score distribution in the order of tasks is $25,25,50$. In the contest it was $5,5,10$.
- **Attention! The task is to implement the 3 functions described in the problem statement. The source you submit should not contain the `main` function!** Here is an example of a valid source:
```cpp
#include <algorithm>
using namespace std;

bool verifica(int A[101][101], int N, int M) {
    return 0;
}

int complet(int A[101][101], int N, int M) {
    return A[1][1];
}

int optim(int A[101][101], int N, int M, int K) {
    return *max_element(A[1] + 1, A[1] + M+1);
}
```
