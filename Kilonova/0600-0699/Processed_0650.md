
A matrix $A$ with $N$ rows and $M$ columns is given, with values ranging between $1$ and $N \cdot M$ inclusive, not necessarily distinct. An **operation** consists of selecting two consecutive rows or two consecutive columns and swapping them. A **yin-yang** matrix is a matrix where $A[i][j] \geq A[i][j – 1]$ for any pair $(i, j)$ with $1 \leq i \leq N$ and $2 \leq j \leq M$ and $A[i][j] \geq A[i – 1][j]$ for any pair $(i, j)$ with $2 \leq i \leq N$ and $1 \leq j \leq M$.

# Task

Determine the minimum number of operations needed to transform the given matrix into a yin-yang matrix.

# Input data

The input file `yinyang.in` contains on the first line the natural numbers $N$ and $M$, with the meaning described above. Each of the following $N$ lines contains $M$ natural numbers, representing the elements of the given matrix $A$. The numbers on the same line of the file are separated by a space.

# Output data

The output file `yinyang.out` must contain the minimum number of required operations or $-1$ if no solution exists.

# Constraints and clarifications

* $1 \leq N, M \leq 100$;
* For tests worth $9$ points: $1 \leq N, M \leq 5$;
* For other tests worth $18$ points: $N = 1$;
* For other tests worth $36$ points: the elements in the matrix are **DISTINCT**.

# Example 1

`yinyang.in`
```
2 3
1 2 4
3 5 6
```

`yinyang.out`
```
0
```

## Explanation

The given matrix is already a yin-yang matrix.

# Example 2

`yinyang.in`
```
2 3
6 6 5
4 6 2
```

`yinyang.out`
```
3
```

## Explanation

The operations can be as follows:
- `swap(row 1, row 2)`;
- `swap(column 2, column 3)`;
- `swap(column 1, column 2)`.

The given matrix will finally be in the yin-yang form:

~[yinyang.png]

