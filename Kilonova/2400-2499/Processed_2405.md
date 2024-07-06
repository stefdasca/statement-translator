# Task

From a matrix $mat$ of $N \times N$, construct 3 matrices $v_1$, $v_2$, $v_3$ with the following properties:
For each cell in the matrix $(i, j)$, $1 \leq i, j \leq N$:

* $0 \leq v_{1 (i, j)}<i$;
* $0 \leq v_{2 (i, j)}<j$;
* $v_{3 (i, j)}=$ sum of the submatrix with the top-left corner $(i-v_{1 (i, j)}, j-v_{2 (i, j)})$ and bottom-right corner $(i, j)$ from the matrix $mat$

You are given $N$, $K$ and the matrices $v_1$, $v_2$, $v_3$. You need to display a way to change exactly $K$ values in the matrix $mat$ so that the sum of the values in $v_3$ becomes minimal. Additionally, in the end, you will need to display the minimal sum. You can choose to keep the element in cell $(i, j)$ in the matrix $mat$ unchanged, in which case you will display $(i, j, the element of matrix $mat$ in cell (i, j))$.

# Input data

The input file `partsum.in` contains on the first line two integers, $N$ and $K$. On the next $N$ lines, there will be $N$ values, representing the values in $v_1$. On the subsequent $N$ lines, there will be $N$ values, representing the values in $v_2$. On the following $N$ lines, there will be $N$ values, representing the values in $v_3$.

**Attention!** In the tests, there are no empty lines between the matrices $v_1$, $v_2$ and $v_2$, $v_3$. These have been added only for clarification in the example!

# Output data

The output file `partsum.out` will contain on the first $K$ lines three values $lin_i, col_i, x_i$, representing that the value in cell $(lin_i, col_i)$ will change to $x_i$. On the $(K+1)^{th}$ line, the minimal sum will be printed.

**Attention!** If at least one value among $lin_i$ or $col_i$ is not in the interval $[1, N]$, the verdict will be Wrong Answer. Additionally, if at least one value $x_i$ is not in the interval $[0, 3 \times 10^6]$, the verdict will be Wrong Answer.

# Constraints and clarifications

* $1 \leq N \leq 600$;
* $1 \leq K \leq N^2$;
* There can be multiple correct solutions, any one of them will be accepted
* If the $K$ changes do not lead to the sum of the values in $v_3$ being the sum printed on the $(K+1)^{th}$ line, $0$ points will be awarded!
* It is guaranteed that the matrices $v_1$, $v_2$ and $v_3$ come from a matrix $mat$
* $0 \leq v_{3 (i, j)} \leq 10^{12}$
* It is guaranteed that the elements of the matrix $mat$ are natural numbers

| # | Points | Restrictions                          |
| - | ------- | ----------                           |
| 1 | 13      | $v_{1 (i, j)}=v_{2 (i, j)}=0$, $1 \leq i, j \leq N$    |
| 2 | 15      | $K=1$                                |
| 3 | 29      | $1 \leq N \leq 50$                   |
| 4 | 43    | No other restrictions                  |

# Example 1

`partsum.in`
```
2 1
0 0
0 0

0 1
0 0

2 5
3 3
```

`partsum.out`
```
1 1 0
9
```

## Explanation

The matrix $mat$ from which $v_1$, $v_2$ and $v_3$ originate is:

```
2 3
3 3
```

If we change the value $2$ to $0$ in cell $(1, 1)$, the sums on row $1$ will become $0 \ 3$, and the sum of the values in $v_3$ becomes $0 + 3 + 3 + 3=9$. This is the minimal sum that can be formed if we change at most one element.