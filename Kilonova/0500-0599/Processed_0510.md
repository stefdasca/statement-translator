~[Castel.png|align=right|width=25%]

A game has $N$ yellow blocks and $N$ blue blocks, all of the same size; on each yellow block, there is a natural number written, with at most $9$ digits. The game aims to build a castle consisting of several rows of blocks, where the top row is made of a single yellow block, and each of the other rows starts and ends with a yellow block. Any two neighboring blocks in the same row share a common side, and each block, except the yellow ones at the edges, shares a common side with a block belonging to the row above. Any two blocks sharing a common side have different colors.

The rows of blocks are numbered from bottom to top, starting from $1$. To build the castle, the yellow blocks are taken in the order they are given, while the blue blocks are taken in any order, and they are placed in rows from bottom to top, and in each row from left to right, as follows: the first block is placed on the base row (numbered $1$), then each block (yellow or blue) is placed either next to it on the current row to the right, or on a new row, above a block of the current row. After placing the block at the top of the castle, on each blue block, a number is written equal to the sum of the numbers written on the two neighboring yellow blocks located on the same row, to its left and right. To win the game, the resulting castle should have a maximum number of rows, even if it does not use all the given blocks.

# Task

Knowing the numbers written on the $N$ yellow blocks in the given order, write a program that determines:
1. The number of yellow blocks, among the $N$ given, that have single-digit values written on them;
2. The row on which the block at the top of the castle is located and the number written on this block;
3. The number of blue blocks forming the castle and the sum of all the numbers written on them.

# Input data

File `castel.in` contains:
* The first line contains two natural numbers $C$ and $N$, in this order, separated by a space, where $C$ represents the task number and can have the values $1$, $2$ or $3$, and $N$ has the meaning given in the statement;
* The second line contains $N$ natural numbers separated by a space, representing the numbers written on the yellow blocks, in the order they are taken.

# Output data

File `castel.out` contains on the first line:
* A single natural number for solving task $1$, representing the determined value according to this requirement;
* Two natural numbers separated by a space, in the case of tasks $2$ and $3$. For task $2$, the first number represents the row on which the block at the top of the castle is, and the second number represents the number written on this block. For task $3$, the first value represents the number of blue blocks forming the castle, and the second value represents the sum of all the numbers written on these blocks.

# Constraints and clarifications
* $3 \leq N \leq 5 \ 000$;
* For $25$ points, $C = 1$;
* For $30$ points, $C = 2$;
* For $45$ points, $C = 3$.

# Example 1

`castel.in`
```
1 12
17 5 11 2 17 17 4 2 2 5 34 88
```

`castel.out`
```
6
```

## Explanation

$C=1$ and there are $6$ blocks on which single-digit numbers are written.

# Example 2

`castel.in`
```
2 12
17 5 11 2 17 17 4 2 2 5 34 88
```

`castel.out`
```
4 5
```

## Explanation

The example corresponds to the image in the statement and $C=2$. The block at the top of the castle is on row $4$ and has $5$ written on it.

# Example 3

`castel.in`
```
3 12
17 5 11 2 17 17 4 2 2 5 34 88
```

`castel.out`
```
6 110
```

## Explanation

The example corresponds to the image in the statement and $C=3$. There are $6$ blue blocks in the castle and the sum of the numbers written on them is $110$.