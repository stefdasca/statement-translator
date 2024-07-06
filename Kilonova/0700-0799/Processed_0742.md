After translating and adjusting according to the specified instructions, here is the processed text:

---

As you probably know, accountants keep their data in the form of tables and calculate all sorts of sums on rows and columns. Our accountant Atoc has organized his values in the form of a table with $n$ rows (numbered from $1$ to $n$) and $m$ columns (numbered from $1$ to $m$). The elements of the last column are the sums of the elements on the rows (more precisely, the element on row $i$ and column $m$ is equal to the sum of the elements on row $i$ located on columns $1, 2, \ldots, m-1$), and the elements of the last row are the sums of the elements on the columns (more precisely, the element on row $n$ and column $i$ is equal to the sum of the elements on column $i$ located on rows $1, 2, \ldots, n-1$). An example of such a table is given in the following figure.

Unfortunately, Atoc spilled water on his wonderful table and thus some of the numbers in the table became unreadable.

~[tabel.png|width=30em]

# Task

Write a program that reconstructs all the data in the table.

# Input data

The first line of the input text file `tabel.in` contains two natural numbers $n$ and $m$, separated by a space, representing the number of rows and respectively the number of columns of the table. The second line of the input file contains a natural number $p$ which represents the number of undamaged values in the table. Each of the following $p$ lines contains three natural numbers, separated by a space $l \\ c \\ v$, where $l$ is the row number, $c$ is the column number and $v$ is the value of the element on row $l$ and column $c$ of the table.

# Output data

The output text file `tabel.out` will contain the reconstructed table, on $n$ lines each with $m$ values separated by a space.

# Constraints and clarifications

* $1 < n, m \leq 50$
* The values in the table are natural numbers $< 32 \ 000$.
* In all tests, the data in the table can be reconstructed.

# Example

`tabel.in`
```
3 4
10
1 1 2
1 2 5
1 3 7
1 4 14
2 2 6
2 4 23
3 1 13
3 2 11
3 3 13
3 4 37
```

`tabel.out`
```
2 5 7 14
11 6 6 23
13 11 13 37
```

---