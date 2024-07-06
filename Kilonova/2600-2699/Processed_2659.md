The $S$ soldiers of a military unit are at ease and scattered on the field in known positions. Evidently, they are not lined up, standing at attention. The field can be represented by a two-dimensional array with $n$ rows (numbered from $1$ to $n$) and $m$ columns (numbered from $1$ to $m$), a position in the array being identified by the row and column indices. When the arrival of the unit commander is announced, the $S$ soldiers must line up. The alignment involves placing the $S$ soldiers on the same row $L$, in consecutive columns. To avoid chaos, each of them will move only horizontally and vertically. If soldier $i$ ($1 \leq i \leq S$) is initially in position $(L_i, C_i)$ and at alignment reaches position $(Lin, Col)$, the distance he travels will be $|L_i - Lin| + |C_i - Col|$.

# Task

Write a program that solves the following two tasks:
   1. Determine a row $Lin$, such that for aligning the soldiers in positions $1, 2, \dots, S$ on row $Lin$, the sum of distances traveled by them is minimized;
   2. Determine a row $Lin$ and a column $Col$, such that for aligning the soldiers on row $Lin$ in columns $Col, Col + 1, \dots, Col + S - 1$, the sum of distances traveled by them is minimized.
   
# Input data

The input file `soldati.in` contains on the first line 4 natural values $C$, $n$, $m$, $S$, separated by a space, representing the task that needs to be solved, the number of rows, the number of columns, respectively the number of soldiers. The following $S$ lines contain the positions of the $S$ soldiers, with each soldier on a line, the positions being described by two natural numbers $L$, $C$ separated by a space, representing the row, respectively the column.

# Output data

The output file `soldati.out` will contain on the first line a natural number $D_{min}$ representing the total minimum distance traveled for the soldiers to align according to task $C$ from the input file. If $C = 1$, on the second line contain a natural number $Lin$ representing the row where the alignment is made. If $C = 2$, on the second line contain two natural numbers separated by space $Lin$, $Col$, representing the row where the alignment will be made, respectively the column from which the soldiers begin to align. If there are multiple rows where the soldiers can align traveling the minimum total distance, display the smallest one. For $C = 2$, if there are multiple columns $Col$ starting with which the soldiers can align on row $Lin$ traveling the minimum total distance, display the smallest one.

# Constraints and clarifications

* $2 \leq n, m \leq 10^6$
* $1 \leq S \leq \min(m, 10^5)$
* The initial positions of the soldiers are distinct.

| # | Score  |        Constraints                               | 
|---|--------|--------------------------------------------------|
| 1 |    5   |  The soldiers are initially on the same row.     |
| 2 |   14   |  $2 \leq n, m \leq 1\ 500$                       |
| 3 |   12   |  $C = 1$, $1\ 500 < n, m \leq 10\ 000$           |
| 4 |   33   |  $C = 1$                                         |
| 5 |   12   |  $C = 2$, $1\ 500 < n, m \leq 10\ 000$           |
| 6 |   24   |  $C = 2$                                         |

# Example 1

`soldati.in`
```
1 16 17 11
2 3
6 6
6 8
6 9
6 10
6 11
9 6
11 9
13 8
13 6
15 9
```

`soldati.out`
```
54
6
```

## Explanation

Below is the field represented and the way the soldiers rearrange
~[ex1.png|width=35em]

# Example 2

`soldati.in`
```
2 16 17 11
2 3
6 6
6 8
6 9
6 10
6 11
9 6
11 9
13 8
13 6
15 9
```

`soldati.out`
```
46
6 3
```

## Explanation

- $2 \\ 3 \\rightarrow 6 \\ 3$
- $4$ steps on column $3$
- $6 \\ 6 \\rightarrow 6 \\ 4$
- $2$ steps on row $6$
- $6 \\ 8 \\rightarrow 6 \\ 7$
- $1$ step on row $6$
- $6 \\ 9 \\rightarrow 6 \\ 9$
- $0$ steps (stays in place)
- $6 \\ 10 \\rightarrow 6 \\ 12$
- $2$ steps on row $6$
- $6 \\ 11 \\rightarrow 6 \\ 13$
- $2$ steps on row $6$
- $9 \\ 6 \\rightarrow 6 \\ 5$
- $3$ steps on column $6$ and $1$ step on row $6$
- $11 \\ 9 \\rightarrow 6 \\ 10$
- $5$ steps on column $9$ and $1$ step on row $6$
- $13 \\ 8 \\rightarrow 6 \\ 8$
- $7$ steps on column $8$
- $13 \\ 6 \\rightarrow 6 \\ 6$
- $7$ steps on column $6$
- $15 \\ 9 \\rightarrow 6 \\ 11$
- $9$ steps on column $9$ and $2$ steps on row $6$