```markdown
# Task

Given the integers $N$, $M$ and $T$. Calculate the number of ways to construct a matrix with $N$ rows and $M$ columns using integer values in the closed interval $[0, T]$, such that each row and each column of the matrix has elements in arithmetic progression with a strictly positive ratio. The progressions are considered for the sequence of elements in the rows from left to right, and for the columns from top to bottom. Moreover, each row and each column can have its own ratio, distinct from the others, and the ratios associated with the rows and columns must increase from top to bottom, respectively from left to right. Since this number can be very large, it will be displayed modulo $10^9 + 9$.

# Input data
The first line of the file `matrice.in` contains the numbers $N$, $M$ and $T$ with the meaning from the task.

# Output data
The file `matrice.out` will contain only the required number of ways, modulo $10^9 + 9$.

# Constraints and clarifications
* $1 \leq N, M \leq 200$;
* $1 \leq T \leq 20 \ 000 \ 000$;
* Be aware of the memory limit!

|#| Score | Constraints|
| - | - | ---------- |
| 1 | 11| $N = 1$ or $M = 1$ and $T \leq 1 \ 000$ |
| 2 | 9 | $N = 1$ or $M = 1$ |
| 3 | 15| $T \leq 100$ |
| 4 | 17| $T \leq 1 \ 000$ |
| 5 | 26| $T \leq 100 \ 000$ |
| 6 | 22| Without additional constraints |

# Example 1

`matrice.in`
```
2 3 5
```

`matrice.out`
```
8
```

## Explanation

The 8 matrices are: 

$$\begin{pmatrix}
    0 & 1 & 2 \\
    1 & 2 & 3
\end{pmatrix}, \begin{pmatrix}
    1 & 2 & 3 \\
    2 & 3 & 4
\end{pmatrix}, \begin{pmatrix}
    2 & 3 & 4 \\
    3 & 4 & 5
\end{pmatrix}$$

$$\begin{pmatrix}
    0 & 1 & 2 \\
    2 & 3 & 4
\end{pmatrix}, \begin{pmatrix}
    1 & 2 & 3 \\
    3 & 4 & 5
\end{pmatrix}, \begin{pmatrix}
    0 & 1 & 2 \\
    3 & 4 & 5
\end{pmatrix}$$

$$\begin{pmatrix}
    0 & 1 & 2 \\
    1 & 3 & 5
\end{pmatrix}, \begin{pmatrix}
    0 & 2 & 4 \\
    1 & 3 & 5
\end{pmatrix}$$

It can be observed that the ratios of the rows and columns **DO NOT** necessarily need to be *strictly* increasing.

# Example 2

`matrice.in`
```
2 3 1000
```

`matrice.out`
```
437458160
```
```