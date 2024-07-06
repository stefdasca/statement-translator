# RAU-Gigel has finished his online courses for the day. He keeps thinking about games, this time about a game with chess pieces. He draws a chessboard as a square matrix of size $N$ and places a chess piece in each of the $N \times N$ cells. It is considered that he has $N \times N$ copies of each possible piece (kings, queens, rooks, bishops, knights, pawns), and the color is irrelevant. RAU-Gigel wonders what the minimum number of squares (cells) a king must pass through to reach any queen. The king can move one cell in four possible directions: N, E, S, W.

But that's not all. At the beginning of the game, RAU-Gigel has $15$ lives. When RAU-Gigel moves a king (any king) over the first pawn, he loses one life. The good news is that after that, RAU-Gigel can take any number of pawns without his number of lives being affected. When taking a knight, the king loses two lives, but after that, he can take, without any loss, any number of knights. The same applies to bishops, the first bishop costs him four lives and similarly for rooks, which cost him eight lives.

RAU-Gigel wants to find out what is the shortest path from any king to any queen, but with the condition that at the end of the game he retains as many lives as possible.

# Task
1) What is the maximum number of lives that RAU-Gigel retains?
2) Through how many squares does the path of minimum length pass? Which king moves and on what path? If there are multiple paths of minimum length, then the lexicographically smaller path is determined (a cell is lexicographically smaller than another cell if it is on a row with a smaller index or if it is on the same row with the second cell but on a column with a smaller index).

# Input data
Read from the file `jocdesah.in` a natural number $A$. For all input tests, the number $A$ can have only the value $1$ or the value $2$. Then read another line that contains the natural number $N$, as described in the problem statement. On the following $N$ lines, there are $N$ capital letters with the following meanings: `P` – pawn, `C` – knight, `N` – bishop, `T` – rook, `Q` – queen, and `K` – king. The characters on each line do not have spaces between them.

# Output data
If the value of $A$ is $1$, only the first task is to be solved. In this case, print to the file `jocdesah.out` a single natural number that represents the number of lives that RAU-Gigel retains at the end of the game.

If the value of $A$ is $2$, only the second task is to be solved. In this case, print to the file `jocdesah.out`, the first line will contain the natural number $K$ representing the number of squares through which the chosen king passes (counting both the departing square and the arrival one), then on the next $K$ lines are pairs in the form $i\ j$ (separated by a single space) where $i$ and $j$ represent the row and column of the cells through which the king passes (in order of movement).

# Constraints and clarifications
- $2 \le N \le 100$
- In each test, there is at least one letter `K` and at least one letter `Q`.
- The first task is worth 45 points.

# Example 1
`jocdesah.in`
```
1
6
PCQPNP
PCCCCP
QNPKPK
PCKPPP
NKPPPP
NNPPQP
```
`jocdesah.out`
```
14
```
# Example 2
`jocdesah.in`
```
2
6
PCQPNP
PCCCCP
QNPKPK
PCKPPP
NKPPPP
NNPPQP
```
`jocdesah.out`
```
5
3 4
3 5
4 5
5 5
6 5
```

## Explanation
Both examples describe the same chessboard.

RAU-Gigel will choose to move the king from position $(3, 4)$. The path will travel through $5$ cells (counting both the departure and arrival cells), and these are: $(3,4)$, $(3,5)$, $(4,5)$, $(5,5)$, $(6,5)$. On his path, he took only pawns, so he lost just a single life, remaining with $14$.

It is noted that there is another path of length $5$ which would also cost him a single life: $(3,4)$, $(4,4)$, $(4,5)$, $(5,5)$, $(6,5)$. However, this path is lexicographically larger than the path chosen by RAU-Gigel (the pair $(3,5)$ is lexicographically smaller than the pair $(4,4)$), hence he will not choose it.

Another path is: $(3,4)$, $(3,3)$, $(3,2)$, $(3,1)$, which is indeed shorter (passing through only $4$ cells). However, on this path, RAU-Gigel would attack a pawn and a bishop, costing him $1 + 4 = 5$ lives, leaving him with only $10$, so he will not choose it.