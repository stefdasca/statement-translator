```markdown
A matrix with $2$ rows and $n$ columns is given, which has $k$ occupied cells.

There are $q$ queries of the form $(x_1, y_1, x_2, y_2)$, with the following meaning: if you occupy two distinct free cells of the initial matrix, $(x_1, y_1)$ and $(x_2, y_2)$, can you completely pave the matrix with domino pieces of sizes $2 \times 1$ and $1 \times 2$? After performing a query, the occupied cells associated with it will become free again (changes made to the matrix do not persist between queries).

# Task

Determine, for each query, whether it is possible to completely pave the matrix with domino pieces of sizes $2 \times 1$ and $1 \times 2$.

# Input data

The first line of the file `dominoes.in` contains $n$ and $k$.

The next $k$ lines contain the coordinates of the occupied positions, in the form $(x, y)$.

The $(k + 2)$-th line contains $q$. Each of the following $q$ lines contains the values $x_1$, $y_1$, $x_2$ and $y_2$, separated by a space, with the meaning from the task.

# Output data

The file `dominoes.out` will contain $q$ lines, each line containing the answer (`1` if it's possible, and `0` if it's not) corresponding to each query, in the order in which they appear in the input file.

# Constraints and clarifications

* It is guaranteed that the initial matrix can be completely paved with domino pieces.
* $1 \leq x, x_1, x_2 \leq 2$
* $1 \leq y, y_1, y_2 \leq n$
* $0 \leq k \leq 100\ 000$, $k$ even
* $1 \leq q \leq 100\ 000$
* $1 \leq n \leq 1\ 000\ 000\ 000$

|#| Score | Constraints                             | 
|-|---------|-----------------------------------------------|
|1|    9    | $n, k, q \leq 8$                              |
|2|    6    | $k = 0$                                       |
|3|   11    | $n, k, q \leq 5\ 000$                           |
|4|   12    | $k, q \leq 5\ 000$                              |
|5|   23    | $n \leq 100\ 000$                            |
|6|    6    | $y_1 = y_2$ for each query        |
|7|    8    | $y_1 \neq y_2$ for each query     |
|8|   25    | No additional constraints             |

# Example 1

`dominoes.in`
```
5 2
1 1
2 5
4
1 3 2 3
2 1 1 5
2 3 2 4
1 2 2 4
```

`dominoes.out`
```
0
1
1
1
```

## Explanation

Below are the matrix configurations for each query, in the order from input, with black marking the blocked cells:

~[img1.png|width=15em]

# Example 2

`dominoes.in`
```
6 4
1 1
2 3
1 4
2 6
3
1 2 2 2
1 2 1 3
1 2 1 5
```

`dominoes.out`
```
0
1
0
```

## Explanation

The matrix configurations for each query:

~[img2.png|width=15em]

# Example 3

`dominoes.in`
```
6 2
1 1
2 3
3
1 4 2 6
1 4 2 5
1 3 2 5
```

`dominoes.out`
```
1
0
0
```

## Explanation

The matrix configurations for each query:

~[img3.png|width=15em]
```
