Here is the translated competitive programming problem statement:

A square board is composed of $N \times N$ identical square cells, grouped into $N$ rows and $N$ columns numbered from $1$ to $N$. From any cell at row $i$ and column $j$, one can move only to the neighboring cell $(i + 1, j)$ or $(i, j + 1)$, if it exists. Inside $M$ cells of this matrix, a token is placed.

We define a path on this board as any sequence of cells traversed according to the movement rule described earlier. The length of such a path is equal to the number of cells traversed.

# Task

Given the size of the board $N$, the total number of tokens $m$, and two natural numbers $L$ and $K$, determine a number $d$, representing the number of distinct paths modulo $31\ 607$ of length $L$ starting from cell $(1, 1)$ and containing exactly $K$ tokens.

# Input data

The input file `drumuri.in` contains on the first line four natural numbers $n$, $m$, $K$, $L$ separated by a space, with the significance described earlier.
Each of the next $m$ lines contains two natural numbers $x$, $y$ separated by a space, representing the row and column where a token is located.

# Output data

The output file `drumuri.out` will contain on the first line a single natural number $D$ representing the number of paths modulo $31 \ 607$ that start from cell $(1, 1)$, have a length of $L$, and pass through $K$ cells containing tokens.

# Constraints and clarifications

* $1 \leq K \leq N \leq 250$
* $1 \leq M \leq 10\ 000$
* $1 \leq L < 500$
* Two paths are considered distinct if they differ by at least one cell.
* A cell contains at most one token.

# Example 1

`drumuri.in`
```
3 4 3 4
1 1
1 3
2 2
2 3
```

`drumuri.out`
```
3
```

## Explanation

There are $3$ paths of length $4$ containing $3$ tokens:
* $(1, 1), (1, 2), (1, 3), (2, 3)$;
* $(1, 1), (1, 2), (2, 2), (2, 3)$;
* $(1, 1), (2, 1), (2, 2), (2, 3)$.

# Example 2

`drumuri.in`
```
4 5 2 4
1 2
2 1
1 3
3 2
4 3
```

`drumuri.out`
```
5
```

## Explanation

There are $5$ paths of length $4$ containing $2$ tokens:
* $(1, 1), (1, 2), (1, 3), (1, 4)$;
* $(1, 1), (1, 2), (1, 3), (2, 3)$;
* $(1, 1), (1, 2), (2, 2), (3, 2)$;
* $(1, 1), (2, 1), (2, 2), (3, 2)$;
* $(1, 1), (2, 1), (3, 1), (3, 2)$.