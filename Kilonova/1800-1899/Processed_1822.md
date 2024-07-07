
We have a chessboard of size $N \times N$ and a knight piece, but more special than the one known in the popular thinking sport. The knight in our problem also makes L-shaped moves without leaving the chessboard. One of the sides of the L has the length of two squares, and the other side can have any length $x \\ (1 \\leq x \\leq N)$. We call a move of type $x$ a move where one side has a length of $2$ and the other has a length of $x$. 

A sequence of moves will be encoded as a **decreasing** sequence of natural numbers representing the move types it consists of, regardless of the order in which they were performed. For example, the sequence $4\\ 4\\ 4\\ 2$ encodes three moves of type 4 and one of type 2. We say that the sequence of moves $a_1, a_2, \ldots, a_k$ is lexicographically greater than $b_1, b_2, \ldots, b_k$ if there exists an $i$ where $1 \\leq i \\leq k$, such that: $a_i > b_i$ and $a_j = b_j$, for every $j < i$.

# Task

Determine an initial position of the knight and a sequence of moves such that exactly one visit is made to each position on the board (the initial position is considered visited simply because it's the starting point). If there are multiple solutions, the one for which the obtained sequence of encoded moves is the lexicographically largest is required.

# Input data

The input file `cai.in` contains on the first line the number $N$, which represents the number of rows and columns of the game board.

# Output data

The output file `cai.out` contains $N^2$ lines, each containing two natural numbers $lin$ and $col$, separated by a space, representing the row and column coordinates for each position the knight visits, in the order the moves are performed.

# Constraints and clarifications

* $2 \\leq N \\leq 400$.
* The rows and columns are numbered starting with $1$.
* Partial points will be awarded for a correct solution for which the obtained sequence of encoded moves is not the lexicographically largest.

# Example 1

`cai.in`
```
2
```

`cai.out`
```
1 1
2 2
1 2
2 1
```

## Explanation

The solution is encoded by the sequence $2 \\ 2 \\ 1$, consisting of two moves of type $2$ and one move of type $1$. One possible order in which the moves are made is as follows: The knight starts from position $(1,1)$, makes a move of type $2$ first, reaching position $(2,2)$, then makes a move of type $1$, reaching position $(1,2)$ and finally makes another move of type $2$, reaching the final position $(2,1)$. In the table below, the order in which each position is visited is noted.

~[cai.png]

Another variant would be the sequence of moves encoded by the sequence $2 \\ 1 \\ 1$, which is not the lexicographically largest.
The knight starts from position $(1,1)$, makes a move of type $1$ first -- reaching position $(1,2)$, then makes a move of type $2$, reaching position $(2,1)$ and finally makes another move of type $1$, reaching the final position $(2,2)$.
```

I have translated the statement into English, preserving the requested formats and syntax. Please review to ensure it meets your needs.