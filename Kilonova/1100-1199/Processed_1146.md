A rectangular billboard contains bulbs, placed side by side, aligned in rows and columns.

Each row and each column has a switch that changes the state of all bulbs on that row or column, from their current state to the opposite state (off/on, on/off). No individual bulb can be operated on. Initially, all bulbs on the board are off.

# Task

Create a program that can bring the board from the initial state to a given configuration by acting on a minimum number of rows and columns, if this is possible.

# Input data

The input will be read from the file `becuri.in`, which has the following format:

* The first line contains two natural numbers, $m$ and $n$, separated by space, representing the number of rows and columns of the board;
* The next $m$ lines contain $n$ columns, consisting of elements $0$ or $1$, separated by space, representing the final configuration of the board. $1$ indicates a lighted bulb, while $0$ indicates a turned-off bulb.

# Output data

A solution must be printed in the file `becuri.out` as follows:

* The first line of the file contains the indices of the columns acted upon, separated by space.
* The second line of the file contains the indices of the rows acted upon, separated by space.

If no action is taken on rows or columns, $0$ will be printed on the corresponding line.

The numbering of rows and columns starts from $1$.

If the problem has no solution, $-1$ will be printed on the first line of the output file.

# Constraints and clarifications

* $m,n \leq 100$

# Example

`becuri.in`
```
5 6
1 0 1 1 0 1
1 0 1 1 0 1
1 0 1 1 0 1
0 1 0 0 1 0
0 1 0 0 1 0
```

`becuri.out`
```
2 5
1 2 3
```

