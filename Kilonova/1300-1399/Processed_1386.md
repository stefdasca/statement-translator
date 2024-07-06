~[cartier1.png|align=right]
Victor is a smart and friendly boy, but he gets bored very easily. His father has to constantly invent new games to stimulate him. The latest game, cartier, has three levels and is played using a set of gray cubes, all of the same size.
At the first level, Victor has to build a rectangular block with $m$ cubes such that the sum of the height of the block $(H)$ and its width $(L)$ is minimal and $L \leq H$. For example, for $n = 6$, four blocks can be constructed as shown in the image, but only the first block $(B_1)$ meets the required conditions.
To complete the second level of the game, Victor has to build a neighborhood, having at his disposal a given number of cubes for each block forming the neighborhood. For the construction of each block, the requirements from the first level of the game are respected. Inside the neighborhood, the blocks are placed, in the order they are obtained, adjacent to each other.
At the third level, Victor has to determine a maximum number of adjacent blocks so that the height of the first block in the sequence and the height of the last block in the sequence are not prime numbers relative to each other.
Help Victor complete the second and third levels of the cartier game.

# Task

Write a program that determines the following numbers:

1. $x$, which represents the number of blocks of maximum height built at the second level
2. $y$, which represents the sum of the widths of the blocks from the neighborhood built at the second level
3. $z$, which represents the number of blocks in the sequence determined at the third level

# Input data

The input file `cartier.in` contains the first line a natural number $n$ (the number of blocks to be built) and the second line contains $n$ natural numbers, separated by spaces, representing the number of cubes corresponding to each block.

# Output data

The output file `cartier.out` contains the numbers $x$, $y$ and $z$, in this order, each on a separate line.

# Constraints and clarifications

* The natural numbers read belong to the interval $[1, 100\ 000]$
* Correctly solving task $1$ gets $30\\\%$ of the score. Correctly solving task $2$ gets $30\\\%$ of the score. Correctly solving task $3$ gets $40\\\%$ of the score.

# Example

`cartier.in`

```
6
7 4 10 12 10 15
```

`cartier.out`

```
1
13
4
```

## Explanation

~[cartier2.png|align=center]
~[cartier3.png|align=center]