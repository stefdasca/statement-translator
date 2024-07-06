```markdown
At the wood processing exam, the apprentice engineers received a door with $N$ hinges, each with a resistance $R_1, \dots, R_N$.

The first task of the exam involves determining the total resistance of the door, which is an array $T_1, \dots, T_K$ composed of $K$ numbers, calculated as follows.

First, the matrix $A_{ij}$ with $N - K + 1$ rows and $K$ columns is defined such that the $i$-th row of $A$ is the subarray $R_i , \dots, R_{i + K - 1}$ of the array $R$. For example, if $N = 9$, $R = [2, 5, 4, 3, 2, 1, 8, 7, 3]$ and $K = 3$, then:

$$
A = \begin{pmatrix}
2 & 5 & 4\\
5 & 4 & 3\\
4 & 3 & 2\\
3 & 2 & 1\\
2 & 1 & 8\\
1 & 8 & 7\\
8 & 7 & 3
\end{pmatrix}
$$

Next, the matrix $B_{ij}$ is defined, also with $N - K + 1$ rows and $K$ columns, such that the $i$-th row of $B$ contains exactly the elements of the $i$-th row from matrix $A$, but in ascending order. For example, for the previous values of $N$ and $R$, we have:

$$
B = \begin{pmatrix}
2 & 4 & 5\\
3 & 4 & 5\\
2 & 3 & 4\\
1 & 2 & 3\\
1 & 2 & 8\\
1 & 7 & 8\\
3 & 7 & 8
\end{pmatrix}
$$

Finally, we define $T_j$ as the maximum of column $j$ from $B$, meaning $T_j = \max_i B_{ij}$. In the above example, the column maxima are $3$, $7$, $8$, and are enclosed in rectangles.

# Task

Given $N$, $K$ and $R_1, \dots, R_N$, calculate $T_1, \dots, T_K$.

# Input data

The first line of the file `balama.in` will contain the numbers $N$ and $K$, as described in the statement. The next line will contain the resistances of the $N$ hinges $R_1, \dots, R_N$, separated by spaces.

# Output data

In the output file `balama.out` print $K$ numbers separated by spaces, the $i$-th number representing $T_i$.

# Constraints and clarifications

* $1 \leq N \leq 200\ 000$
* $1 \leq K \leq N$
* $0 \leq R_i \leq 10^9$ for $1 \leq i \leq N$

| # | Points | Constraints          |
| - | ------- | ------------------- |
| 1 | 5      | $1 \leq N \leq 1\ 000$ |
| 2 | 6      | $1 \leq N \leq 10\ 000$      |
| 3 | 9      | $0 \leq R_i \leq 1$ for $1 \leq i \leq N$      |
| 4 | 38      | $1 \leq N \leq 75\ 000$      |
| 5 | 42     | No additional constraints |

**Note:** Subtask 5 contains five test groups, worth $7$, $8$, $8$, $9$ and respectively $10$ points.


# Example

`balama.in`
```
9 3
2 5 4 3 2 1 8 7 3
```

`balama.out`
```
3 7 8
```

## Explanation

Matrix $A$ has values

$ \begin{pmatrix}
2 & 5 & 4\\
5 & 4 & 3\\
4 & 3 & 2\\
3 & 2 & 1\\
2 & 1 & 8\\
1 & 8 & 7\\
8 & 7 & 3
\end{pmatrix}$

Matrix $B$ has values

$\begin{pmatrix}
2 & 4 & 5\\
3 & 4 & 5\\
2 & 3 & 4\\
1 & 2 & 3\\
1 & 2 & 8\\
1 & 7 & 8\\
3 & 7 & 8
\end{pmatrix}$

The column maxima are $3$, $7$, $8$.
```