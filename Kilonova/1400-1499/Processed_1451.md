In this story, it's about a house with multiple rooms. A room has the shape of a square with side length $1$. If two rooms share a common wall, then it is possible to move from one room to the other. The house doesn't necessarily have a rectangular shape. Such a house can be described in our story in two ways:
* by the minimal matrix: a matrix with elements $0$ and $1$ in which there are $N$ values equal to $1$, corresponding to the rooms, and the first row, last row, first column, and last column each contain at least one element equal to $1$.
* by construction: a string of $N-1$ pairs $(a_i, b_i) \\ 1 \\leq i < n$ in which $a_i \\in \\{1, 2, \\dots, i\\}$ and $b_i \\in \\{N, S, E, V\\}$. The rooms will be numbered from 1 to $n$. The pair $(a_i, b_i)$ specifies the position of room $i+1$ relative to room $a_i$: `E` means to the right (east), `N` above (north), `V` to the left (west), `S` below (south). Note that for the first room, there is no specification!

~[img1.jpg]

For example, the house above can be described by the string `(1 E) (2 E) (2 S) (3 S)`, meaning the second room is "attached" to the east of the first room, the next one (third room) to the east of room $2$, the fourth room to the south of room $2$, and the last one to the south of room $3$.

# Task:
1. Given the description of a house by construction, provide the description by the minimal matrix.
2. Given the description of a house by the minimal matrix, provide the description by construction.

# Input data

The file `casa.in` contains:
* The first line contains a natural number $p$ representing the task to solve. For all input tests, the number $p$ can have the value $1$ or $2$.
* If the value of $p$ is $1$, then the following lines contain the description of a house by construction as follows: the second line contains a natural number $N$ representing the number of rooms in the house, and each of the following $N-1$ lines contain two values separated by a space - a natural number and a character, with the above meaning.
* If the value of $p$ is $2$, then the following lines contain the description of a house by the minimal matrix as follows: the second line contains two non-zero natural numbers $M, N$ representing the dimensions of the matrix, and in the following $M$ lines $N$ numbers $0$ or $1$ separated by a space.

# Output data

If the value of $p$ is $1$, then only task 1 will be solved. In this case, the file `casa.out` will contain on the first line two natural numbers $M$ and $N$ separated by a single space representing the number of rows and respective number of columns of the minimal matrix, and in the following $M$ lines, $N$ values 0 or 1 separated by a single space.
If the value of $p$ is $2$, then only task 2 will be solved. In this case, the file `casa.out` will contain on the first line two natural numbers $Nr$ and $C$ separated by a single space. $Nr$ represents the number of rooms, and $C$ the position of room 1 (the smallest number of the order of a column containing the value 1 in the first row). The following $Nr-1$ lines will each contain two values separated by a single space, representing the description of a house by construction according to the statement details. Columns will be numbered starting from 1, and if there are multiple solutions, the smallest will be displayed in lexicographical order: the pair $(k, l)$ will be displayed before the pair $(k', l')$ if $k < k'$ or if $k = k'$ and $l < l'$ (i.e., $E < N < S < V$).

# Constraints and clarifications

* The minimal matrix of a house has a maximum of $100\ 000$ elements.

# Example 1

`casa.in`
```
1
5
1 E
2 E
2 S
3 S
```

`casa.out`
```
2 3
1 1 1
0 1 1
```

# Example 2

`casa.in`
```
2
2 3
1 1 1
1 0 1
```

`casa.out`
```
5 1
1 E
1 S
2 E
4 S
```
