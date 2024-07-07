
A **binary** matrix with $n$ columns and $m$ rows is given. The columns are numbered from left to right with values from $1$ to $n$, and the rows are numbered **from bottom to top** with values from $1$ to $m$.

The given matrix has a particular form, so that for each column $i$ from $1$ to $n$, all the elements of the matrix in the respective column have the value $1$ for all the rows in the interval $[1, h_i]$ and the value $0$ elsewhere. The values $h_i$ are natural numbers given in ascending order $(h_{i-1} \leq h_i$, $1 \leq i \leq n$).

# Task
Answer $q$ questions of the form: given the numbers $A$, $B$, $C$, $D$, find the sum of the elements in the submatrix determined by the rectangular area having the bottom-left corner in column $A$ and row $B$, and the top-right corner in column $C$ and row $D$.

# Input data
The input file is `tnia.in`.
- The first line contains two natural numbers $n$ and $m$ separated by a space, with the above meaning;
- The second line contains the $n$ elements $h_i$ of the array separated by a space;
- The third line contains a natural number $q$ representing the number of questions;
- The next $q$ lines contain four numbers $A$, $B$, $C$, $D$ with the above meaning, separated by a space.

# Output data
The output file `tnia.out` will contain $q$ lines representing the answer for each question.

# Constraints and clarifications
- $0 \leq h_i \leq m$
- $1 \leq n \leq 100\ 000$
- $1 \leq q \leq 100\ 000$
- $1 \leq m \leq 1\ 000\ 000\ 000$
- For 15 points: $n, m, q \leq 100$.
- For another 16 points: $n, m, q \leq 3\ 000$.
- For another 16 points: $n \leq 100\ 000$, $m \leq 1\ 000\ 000\ 000$, $q \leq 100$.
- For the correct solution to the task, 90 points are awarded.
- 10 points are awarded by default.

# Example
`tnia.in`
```
5 10
2 3 7 8 10
5
1 1 5 10
2 5 4 7
3 2 3 6
3 8 3 10
3 2 3 10
```
`tnia.out`
```
30
6
5
0
6
```

## Explanation
The rectangular area having the bottom-left corner in column $1$ and row $1$ and the top-right corner in column $5$ and row $10$ has the sum of elements $30$.
Similarly, for the other four questions, the correct answers are $6$, $5$, $0$, and $6$.
