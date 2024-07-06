Sure, here is the translated text:

---

A matrix is called a shell of order $N$, or simply a shell, if it is constructed based on a non-zero natural number $N$ according to the following rule:
- The shell is initially formed from a $1 \times 1$ square with the value $1$.
- For each step $I$ with the values $2$, $3$, ..., $N$ to the already existing shell, a square will be added to the RIGHT, BOTTOM, LEFT, TOP, repeatedly in this order, where all elements have the value $I$, and the side length of the new square corresponds to the side length of the shell to which it is attached.

\
A shell of order $5$ is formed in $5$ steps as follows:

~[cochilie.jpg]

Rows and columns are numbered from top to bottom and from left to right starting with the value $1$.

# Task
Given the natural numbers $N$ and $P$, you will need to answer the following questions:
1) What are the dimensions of the shell of order $N$?
2) What elements are on row $P$ of the shell of order $N$?

# Input data
The input file `cochilie.in` will contain the value $C$ on the first line, which can be either $1$ or $2$.

If the value of $C$ is $1$, then the next line will contain the value of $N$.
If the value of $C$ is $2$, then the next line will contain the values of $N$ and $P$ separated by a space.

# Output data
The output data will be displayed on the first line of the output file `cochilie.out` depending on the value of $C$ as follows:
1) If the value of $C$ is $1$, then $NRLIN$ and $NRCOL$ separated by a space, representing the number of rows and the number of columns of the shell of order $N$, will be printed.
2) If the value of $C$ is $2$, then the elements on row $P$ of the shell of order $N$, separated by a space, will be printed.

# Constraints and clarifications
- $1 < N < 30$
- Row $P$ always refers to a valid row of the shell.
- For tests worth 8 points, we have $C = 1$.
- For other tests worth 36 points, we have $C = 2$ and $N \leq 17$.
- For other tests worth 20 points, we have $C = 2$ and $P$ refers to the first or last row of the shell.
- For other tests worth 36 points, we have $C = 2$ without additional restrictions.

# Example 1
`cochilie.in`
```
1
5
```

`cochilie.out`
```
8 5
```

## Explanation
The shell of order $5$ has $8$ rows and $5$ columns.

# Example 2
`cochilie.in`
```
2
5 6
```
`cochilie.out`
```
4 4 4 1 2
```

## Explanation
The $6$-th row of the shell of order $5$ consists of the numbers $4\ 4\ 4\ 1\ 2$.