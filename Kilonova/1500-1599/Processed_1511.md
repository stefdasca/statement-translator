---

On a grid paper with $N$ horizontal cells (on the same row) and $M$ vertical cells (on the same column), Alex painted ships. We define a line ship ($L$) as a set of shaded, consecutive cells on a row of the grid paper. We define a column ship ($C$) as a set of shaded, consecutive cells on a column of the grid paper. The size of a ship is equal to the number of cells it is composed of. A ship formed from a single cell is neither a line nor a column. Ships can have different sizes. Two different ships do not touch on sides or corners, do not overlap, and do not have common cells. On the grid paper, only 3 types of ships are painted: line ship ($L$), column ship ($C$), or single cell ship.

# Task

Given $M$, $N$, and Alex's painting, write a program to determine:
1. The number of ships made of only a single cell;
2. The number of line ships and column ships, as well as their sizes.

# Input data

The input file boats.in contains on the first line a natural number $P$ representing the task that needs to be solved ($1$ or $2$). The second line of the file contains two integers, separated by a space, representing the values $M$ and $N$ from the statement. On the next $M$ lines, there are $N$ values equal to $0$ or $1$, separated by a space ($0$ if the cell is not part of a ship, $1$ if the cell is part of a ship).

# Output data

If the task is $P = 1$, then on the first line of the file `boats.out` a natural number will be printed, representing the number of ships made of a single cell.

If the task is $P = 2$, then in the file `boats.out` will be written, on each line, separated by a space, three values: the character $L$ followed by the numbers $d$ and $c$, in increasing order by the value $d$, where $d$ represents the length of the ship (number of cells) and $c$ the number of line ships of length $d$. Then, on each of the following lines, separated by a space, the character $C$ followed by two numbers: $d$ and $c$, in increasing order by $d$, where $d$ represents the length of the ship (number of cells) and $c$ the number of column ships of length $d$.

# Constraints and clarifications

* $2 \leq M, N \leq 1\ 000$
* The existence of at least one ship is guaranteed.
* For the correct solving of the first task, $20\%$ of the score will be awarded, and for the correct solving of the second task, $80\%$ of the score will be awarded.

# Example 1

`boats.in`
```
1
12 12
0 0 0 0 0 0 0 0 0 0 0 1
0 1 1 1 1 1 0 0 0 0 0 1
0 0 0 0 0 0 0 1 0 0 0 1
0 1 0 0 0 0 0 0 0 0 0 0
0 1 0 0 0 0 0 0 0 0 0 0
0 1 0 1 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 0 0 0 0
0 0 0 0 0 0 0 1 0 0 0 0
0 0 0 0 0 0 0 1 0 0 0 0
0 0 0 0 0 0 0 1 0 0 0 0
0 1 1 0 0 0 0 0 0 0 0 0
```

`boats.out`
```
1
```

## Explanation

Only task $1$ is solved.
There is a single ship made of a single cell.

$
0\ 0\ 0\ 0\ 0\ 0\ 0\ 0\ 0\ 0\ 0\ 1\\
0\ 1\ 1\ 1\ 1\ 1\ 0\ 0\ 0\ 0\ 0\ 1\\
0\ 0\ 0\ 0\ 0\ 0\ 0\colorbox{yellow}{\color{black}1}\ 0\ 0\ 0\ 1\\
0\ 1\ 0\ 0\ 0\ 0\ 0\ 0\ 0\ 0\ 0\ 0\\
0\ 1\ 0\ 0\ 0\ 0\ 0\ 0\ 0\ 0\ 0\ 0\\
0\ 1\ 0\ 1\ 1\ 1\ 1\ 1\ 1\ 0\ 0\ 0\\
0\ 0\ 0\ 0\ 0\ 0\ 0\ 0\ 0\ 0\ 0\ 0\\
0\ 0\ 0\ 0\ 0\ 0\ 0\ 1\ 0\ 0\ 0\ 0\\
0\ 0\ 0\ 0\ 0\ 0\ 0\ 1\ 0\ 0\ 0\ 0\\
0\ 0\ 0\ 0\ 0\ 0\ 0\ 1\ 0\ 0\ 0\ 0\\
0\ 0\ 0\ 0\ 0\ 0\ 0\ 1\ 0\ 0\ 0\ 0\\
0\ 1\ 1\ 0\ 0\ 0\ 0\ 0\ 0\ 0\ 0\ 0\\
$

# Example 2

`boats.in`
```
2
12 12
0 0 0 0 0 0 0 0 0 0 0 1
0 1 1 1 1 1 0 0 0 0 0 1
0 0 0 0 0 0 0 1 0 0 0 1
0 1 0 0 0 0 0 0 0 0 0 0
0 1 0 0 0 0 0 0 0 0 0 0
0 1 0 1 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 0 0 0 0
0 0 0 0 0 0 0 1 0 0 0 0
0 0 0 0 0 0 0 1 0 0 0 0
0 0 0 0 0 0 0 1 0 0 0 0
0 1 1 0 0 0 0 0 0 0 0 0
```

`boats.out`
```
L 2 1
L 5 1
L 6 1
C 3 2
C 4 1
```

## Explanation

Only task $2$ is solved.
There are $3$ line ships: one line ship of length $2$, one line ship of length $5$, and one line ship of length $6$.\
There are $3$ column ships: $2$ column ships of length $3$, and one column ship of length $4$.

$
0\ 0\ 0\ 0\ 0\ 0\ 0\ 0\ 0\ 0\ 0\color{grey}1\color{white}\\
0\colorbox{yellow}{\color{black}1\ 1\ 1\ 1\ 1}\ 0\ 0\ 0\ 0\ 0\color{grey}1\color{white}\\
0\ 0\ 0\ 0\ 0\ 0\ 0\ 1\ 0\ 0\ 0\color{grey}1\color{white}\\
0\color{grey}1\color{white}\ 0\ 0\ 0\ 0\ 0\ 0\ 0\ 0\ 0\ 0\\
0\color{grey}1\color{white}\ 0\ 0\ 0\ 0\ 0\ 0\ 0\ 0\ 0\ 0\\
0\color{grey}1\color{white}\ 0\colorbox{yellow}{\color{black}1\ 1\ 1\ 1\ 1\ 1}\ 0\ 0\ 0\\
0\ 0\ 0\ 0\ 0\ 0\ 0\ 0\ 0\ 0\ 0\ 0\\
0\ 0\ 0\ 0\ 0\ 0\ 0\color{grey}1\color{white}\ 0\ 0\ 0\ 0\\
0\ 0\ 0\ 0\ 0\ 0\ 0\color{grey}1\color{white}\ 0\ 0\ 0\ 0\\
0\ 0\ 0\ 0\ 0\ 0\ 0\color{grey}1\color{white}\ 0\ 0\ 0\ 0\\
0\ 0\ 0\ 0\ 0\ 0\ 0\color{grey}1\color{white}\ 0\ 0\ 0\ 0\\
0\colorbox{yellow}{\color{black}1\ 1}\ 0\ 0\ 0\ 0\ 0\ 0\ 0\ 0\ 0\\
$

