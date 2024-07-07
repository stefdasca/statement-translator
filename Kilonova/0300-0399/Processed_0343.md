You are given a matrix with $n$ rows and $m$ columns. Its entries are consecutive starting from $0$ left to right, top to bottom like below:

| $0\\ $ | $1\\ $  |  $2\\ $  | $3\\ $    | $4\\ $  |
|---|---|---|---|---|
| $5\\ $ | $6\\ $  |  $7\\ $  | $8\\ $  | $9\\ $  |
| $10\\ $ | $11\\ $ |  $12\\ $ |  $13\\ $ | $14\\ $ |
| $15\\ $ | $16\\ $ |  $17\\ $ |  $18\\ $ | $19\\ $ |

There are $q$ operations which modify the matrix in the following way: a submatrix is chosen inside the matrix and it will be inverted horizontally and vertically. For example, if the submatrix with the top-left coordinate $(1, 3)$ and bottom-right coordinate $(3, 5)$ is inverted, it will look like this:

| $0\\ $  | $1\\ $  | $14\\ $ | $13\\ $ | $12\\ $ |
|---|---|---|---|---|
| $5\\ $  | $6\\ $  |  $9\\ $  | $8\\ $    | $7\\ $  |
|  $10\\ $ | $11\\ $ |  $4\\ $  | $3\\ $    | $2\\ $  |
| $15\\ $ | $16\\ $ |  $17\\ $ |  $18\\ $ | $19\\ $ |

You are also given the coordinates $(x, y)$ of a cell; type the value of that cell after all $q$ operations.

# Task

# Input data

The first line will contain $5$ integers, $n, m, q, x$ and $y (1 \leq n, m \leq 10^9), (1 \leq q \leq 3 \cdot 10^5), (1 \leq x, y \leq n)$.

The following $q$ lines will contain $x_1, y_1, x_2$ and $y_2$ which describe the top-left, bottom-right coordinates of the submatrix $(1 \leq x_1 \leq x_2 \leq n), (1 \leq y_1 \leq y_2 \leq n)$.

For tests worth $20$ points it is guaranteed that $(1 \leq n, m \leq 100), (1 \leq q \leq 100)$

# Output data

Print the value of the matrix cell at coordinates $(x, y)$ after all operations.

# Example

`stdin`
```
4 5 1 1 3
1 3 3 5
```

`stdout`
```
14
