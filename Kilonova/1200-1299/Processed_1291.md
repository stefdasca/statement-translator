Ionică has $n$ identical pencils, numbered from $1$, $2$, $...$, $n$. In a moment of relaxation, he begins to place the pencils on the table, some on top of others, so that he can place a pencil directly on the table or on at least two pencils that are at the same height. All pencils not placed directly on the table are parallel to the table's surface. In this way, several stacks are created on the table, each with a specific height (number of pencil levels).

# Task

Determine the height of the tallest stack.

# Input data

The input file `creioane.in` contains:
* A natural number $n$ on the first line representing the number of pencils.
* On each of the following $n$ lines, there are two numbers separated by a space; thus, on line $i + 1$, the numbers $a_i$ and $b_i \\ (0 \\lt i \\lt n + 1)$ indicate that pencil $i$ is placed on pencils $a_i$ and $b_i$. If pencil $i$ is placed directly on the table, both $a_i$ and $b_i$ are equal to $0$.

# Output data

The output file `creioane.out` will contain the required number on the first line.

# Constraints and clarifications

* $1 \\lt n \\leq 9 \ 000$
* Any pencil placed directly on the table and upon which no other pencil is placed forms a stack of height $1$.

# Example

`creioane.in`
```
7
2 7
0 0
0 0
2 7
4 6
2 7
0 0
```

`creioane.out`
```
3
```

## Explanation

On the table, pencils $2$, $3$, and $7$ are placed. On top of pencils $2$ and $7$, pencils $1$, $4$, and $6$ are placed, and on top of pencils $4$ and $6$, pencil $5$ is placed. The tallest stack has a height of $3$, because:
On level $1$ there are pencils $2$, $3$, and $7$
On level $2$ there are pencils $1$, $4$, and $6$
On level $3$ there is pencil $5$