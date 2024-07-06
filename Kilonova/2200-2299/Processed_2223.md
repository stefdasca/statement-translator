# Task

A matrix of dimensions $N \cdot M$ is given. All elements of the matrix have the value $0$ or $1$. There will be $Q$ queries of the form: is there a rectangle with $L$ rows and $C$ columns with all elements equal to $1$ located entirely between the rows $L_1$ and $L_2$ of the matrix, including $L_1$ and $L_2$?

# Input data

The file `lcdr.in` contains on the first line the numbers $N$, $M$ and $Q$ with the meanings from the statement. The following $N$ lines will each contain $M$ numbers with the value $0$ or $1$, without spaces between them. Following are $Q$ lines with four numbers each: $L$, $C$, $L_1$, $L_2$ with the meaning from the statement.

# Output data

The file `lcdr.out` will contain $Q$ numbers, one per line representing the answers to the queries.

# Constraints and clarifications

* $1 \leq N, M \leq 500$
* $1 \leq Q \leq 500\ 000$
* For $30\%$ of the tests, $Q \leq 500$.
* For another $40\%$ of the tests, $Q \leq 200\ 000$.

# Example

`lcdr.in`
```
4 5 5
00000
11100
01111
01100
3 2 2 4
4 3 1 4
1 3 1 2
1 2 4 4
1 3 4 4
```

`lcdr.out`
```
1
0
1
1
0
```