## Task

RAU-Gigel is thinking about a game with chess pieces. He draws a chessboard in the form of a square matrix with a side length of $N$ and places a chess piece in each of the $N \times N$ cells. It is considered that there are $N \times N$ pieces of each possible type (kings, queens, rooks, bishops, knights, pawns) and the color is irrelevant. RAU-Gigel wonders what is the minimum number of cells a certain king has to go through to reach any queen. The king can move one cell in four possible directions: $N, E, S, W$. But that's not all. At the beginning of the game, all kings have 16 lives. When RAU-Gigel moves a king (any king) over the first pawn, it loses one life. The good news is that after that, the king can take any number of pawns without its number of lives being affected. When it takes a knight, the king loses two lives, but after that, it can take any number of knights without losses. The same applies to bishops, the first bishop costs four lives and rooks, which cost eight lives. RAU-Gigel wants to know which king to choose and which path this king should take to a queen so that at the end of the game it has as many lives left as possible and the path is as short as possible.

Tasks:
a) What is the maximum number of lives the chosen king has left?
b) How many cells does the shortest path take? Which king moves and what path does it take?

If there are multiple paths of minimum length, then the lexicographically smaller path will be determined. (A cell is lexicographically smaller than another cell if it is on a row with a smaller index or it is on the same row as the second cell but on a column with a smaller index).

## Input data

The input file `jocdesah.in` contains on the first line a natural number $A$. For all input tests, the number $A$ can only have the value 1 or value 2.

The second line contains the natural number $N$, as mentioned in the statement.

On the next $N$ lines, there are $N$ capital letters with the following meanings:
$P$ – pawn, $C$ – knight, $B$ - bishop, $R$ - rook, $Q$ – queen, and $K$ – king. The characters on each row do not have spaces between them.

## Output data

If the value of $A$ is 1, only task point a) from the ## task will be solved. In this case, the output file `jocdesah.out` will contain a single natural number representing the number of lives left at the end of the game for the king chosen by RAU-Gigel. 

If the value of $A$ is 2, only task point b) from the ## task will be solved. In this case, the output file `jocdesah.out` will contain on the first line the natural number $K$ which represents the number of cells through which the chosen king passes (both the starting cell and the arrival cell are counted), then on the next $K$ lines there are pairs in the form $i j$ (separated by a single space) where $i$ and $j$ represent the row and column of the cells through which the king passes (in order of movement). Rows and columns are indexed from 1 to $N$.

## Constraints and clarifications

$$
2 \leq N \leq 100
$$

$$
In\ every\ test,\ there\ is\ at\ least\ one\ K\ letter\ and\ at\ least\ one\ Q\ letter
$$

45 points are awarded for the correct solution of the first ## task.

## Examples

### Example 1

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

RAU-Gigel will choose to move the king from position $3 \ 4$. The path will go through 5 cells (including the starting and ending cells), and they are: $3 \ 4, 3 \ 5, 4 \ 5, 5 \ 5, 6 \ 5$. On his path, he only took pawns, so he lost just one life, leaving him with 15 lives:

$$\begin{matrix}
 & & & & & & & & & & & & & & K & P\\
 & & & & & & & & & & & & & & P & \\
 & & & & & & & & & & & & & & P & \\
 & & & & & & & & & & & & & & Q &
\end{matrix}$$

It is observed that there is another path of length 5 that also costs only one life:
$$\begin{matrix}
 & & & & & & & & & & & & & & K & \\
 & & & & & & & & & & & & & & P & P \\
 & & & & & & & & & & & & & & P & \\
 & & & & & & & & & & & & & & Q & \\
\end{matrix}$$

The path is: $3 \ 4, 4 \ 4, 4 \ 5, 5 \ 5, 6 \ 5$, but it is lexicographically smaller than: $3 \ 4, 3 \ 5, 4 \ 5, 5 \ 5, 6 \ 5$ (the pair $3 \ 5$ is smaller lexicographically than the pair $4 \ 4$).

Also, another path is: $3 \ 4, 3 \ 3, 3 \ 2, 3 \ 1$:

$$\begin{matrix}
 & & & & & & & & & & & Q & N & P & K & \\
\end{matrix}$$

this path is even shorter (it passes through only 4 cells), but on this path, the king would attack a pawn and a bishop, which would cost $1 + 4 = 5$ lives and leave him with only 11 lives, so he will not choose it.

### Example 2

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
15
```

