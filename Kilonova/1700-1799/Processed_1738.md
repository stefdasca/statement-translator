# The **cmin** game involves finding a strategy to move a certain number of identical tokens on a square board to achieve a final configuration with minimum cost.

The board has **n x n** cells, located at the intersection of $n$ rows numbered from $1$ to $n$ from top to bottom and $n$ columns numbered from $1$ to $n$ from left to right. The number $n$ is always even.

At the initial moment of the game, there are $k$ tokens in known positions on the board. Each token can only be moved vertically, from its initial cell to a final cell not occupied by another token. A token can be moved even if there are cells occupied by other tokens between its initial and final positions.

The cost of moving a token vertically, from the current cell to an adjacent cell, is $1$ (one unit). A token can be moved multiple times. The player decides the order of moving the tokens. They can move $0, 1$, or even all the tokens to finish the game with a minimum total cost. The total cost is the sum of the costs of moving all tokens.

The **cmin** game ends when the absolute difference between the number of tokens that are on the first $n/2$ rows (the upper ones) and the number of tokens on the last $n/2$ rows (the lower ones) is minimized.
~[img1.jpg]

# Task
Knowing the number $n$ of rows and columns of the board and the initial positions of the tokens, determine the minimum total cost required to move them so that the absolute difference between the number of tokens that will be found on the first $n/2$ rows and the number of tokens that will be found on the last $n/2$ rows is minimized.

# Input data

The input file `cmin.in` will contain on the first line a natural number $n$, even, with the meaning described above. The next $n$ lines describe the initial configuration of the board. Each line contains $n$ values $1$ or $0$, separated by a space. The value $1$ represents a cell occupied with a token, and $0$ a free cell.

# Output data

The output file `cmin.out` will contain on the first line a single natural number $c$, representing the required minimum cost, respecting the rules of the **cmin** game.

# Constraints and clarifications

* $2 \leq n \leq 100$ (n – even number);
* $1 \leq k \leq n \times n$.

# Example 1

`cmin.in`
```
2
0 0
1 0
```

`cmin.out`
```
0
```

## Explanation

No token movement is necessary.

# Example 2

`cmin.in`
```
4
1 1 1 1
1 1 0 0
1 0 0 0
0 0 0 0
```

`cmin.out`
```
3
```

## Explanation

One possible way: Move the token from cell $(2, 1)$ to cell $(4,1)$. The cost is $2$. Then move the token from cell $(2, 2)$ to cell $(3, 2)$. The cost is $1$. The sum of the costs is $3$. Another possible way: move the tokens from cells $(3,1)$, $(2,1)$, and $(2,2)$ each one cell. The same final state is achieved as in the first way. Another possible way: from cell $(2,2)$ to $(3,2)$ and from cell $(1,3)$ to $(3,3)$.