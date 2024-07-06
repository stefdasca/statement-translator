Anei loves to play on the computer. Now she has a new game where $n$ horizontal blocks made of squares with side length $1$ fall vertically. The game surface is represented as an array with $L \\ (L > n)$ rows numbered from $1$ to $L$ and $C$ columns, numbered from $1$ to $C$, as in the figure. The array is made up of $L \\times C$ square cells with side length $1$. Each block consists of one or more adjacent squares, located only in the horizontal direction. The blocks are numbered from $1$ to $n$ and fall in order, always from row $L$, at different time intervals and at the same falling speed. Each square in the block falls to the row with the smallest number that is not occupied by another square from a previously fallen block. If it does not encounter another previously stopped square, it stops on row $1$. Thus, squares from the same block can stop on different rows.
~[patrate.png|align=center]
After all the squares of all the blocks have reached their final positions, Ana needs to determine a continuous area of maximum length $L_{max}$, measured horizontally, with the property that the height of each of its columns is at least $h$.

# Task

Determine the starting column index $c_i$ and the maximum length $L_{max}$ measured horizontally of the continuous area formed by squares with the property that each column of squares in the area has a height of at least $h$.

# Input data

The input file `patrate.in` contains:
* The first line contains two natural numbers $n$ and $h$, separated by a space, with the meanings from the statement.
* Each of the next $n$ lines contains two natural numbers $c$ and $p$, separated by a space. The values of $c$ and $p$ on the line $i + 1$ represent the column corresponding to the first square of the left end of block $i$, respectively the number of squares in the block.

# Output data

The output file `patrate.out` contains on a single line the natural numbers $c_i$ and $L_{max}$, separated by a space. If there are several solutions, then the one for which $c_i$ is minimal is displayed.

# Constraints and clarifications

* $1 \\leq h \\lt n \\leq 1 \\ 000$
* $2 \\leq c + p \\leq 1 \\ 000 \\ 000 \\ 000$
* The problem admits a solution for all input data.

# Example

`patrate.in`
```
4 2
3 2
2 6
7 3
6 3
```

`patrate.out`
```
6 3
```

## Explanation

In the figure, the numbering of the squares identifies the blocks they belong to. The area of squares of maximum length starts at column $6$ and has a length of $3$.