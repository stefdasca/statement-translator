# Task

Given a binary square matrix $A$ of dimensions $N \times N$ with elements from the set $\{0, 1\}$. You start from cell $(0, 0)$ — the top-left corner — with a string $S$, initially empty, and you want to reach cell $(N - 1, N - 1)$ — the bottom-right corner. In each move, you can move down or right by one cell. For each cell you pass through (including the first and last), you add the value from that cell to the right end of the string $S$.

# Task

Determine if it is possible for the resulting string $S$ to be a palindrome. If yes, determine a sequence of down and/or right moves that leads from cell $(0, 0)$ to cell $(N - 1, N - 1)$ for which the obtained string is a palindrome. For this sequence, determine the cells traversed in order.

Since we like you, we decided to let you know that **the matrix was generated randomly**.

# Input data

The first line contains a single integer $N$, representing the side of the matrix.

The next $N$ lines contain $N$ characters from the set $\{0, 1\}$, not separated by spaces, representing the description of the matrix.

It is guaranteed that the matrix is chosen **uniformly at random** among all binary matrices of dimensions $N \times N$.

# Output data

Print `NO` if it is not possible for $S$ to be a palindrome. Otherwise, print `YES` on the first line, then, on each of the next $2N - 1$ lines, print two values, $i_k$ and $j_k \\ (0 \\leq i_k, j_k < N)$ — the coordinates of the $k$-th cell traversed.

# Constraints and clarifications

* $1 \leq N \leq 5\ 000$
* $A_{i, j} \in \{0, 1\}$ for $0 \leq i, j < N$

| # | Points | Constraints          |
| - | ------- | ------------------- |
| 1 | 5      | $1 \leq N \leq 10$ |
| 2 | 9      | $1 \leq N \leq 100$      |
| 3 | 19      | $1 \leq N \leq 500$     |
| 4 | 27      | $1 \leq N \leq 1\ 500$     |
| 5 | 40     | No additional constraints.      |

# Example 1

`stdin`
```
2
01
00
```

`stdout`
```
YES
0 0
0 1
1 1
```

## Explanation

We obtain the string `010`, which is a palindrome.

# Example 2

`stdin`
```
4
0100
1010
0100
0001
```

`stdout`
```
NO
```

## Explanation

It is not possible to obtain a palindromic string.

# Example 3

`stdin`
```
4
0010
1001
1010
0010
```

`stdout`
```
YES
0 0
0 1
0 2
0 3
1 3
2 3
3 3
```

## Explanation

We obtain the string `0010100`, which is a palindrome.