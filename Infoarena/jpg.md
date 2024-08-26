# Grid Game

After becoming the President of Romania, Dubluveu had to give up gambling, but he quickly found a new pastime. In his free time, when not occupied with the country's affairs, he and the Prime Minister play the following game. They draw $N$ segments of length $1 \, u$ (one unit), parallel to the coordinate axes, such that it is possible to reach any point from any other point on the figure by moving only along the drawn segments (fig. $1$). After establishing the game board, the two can start to alternately color the segments. The player making a move can color a segment only if it is the edge of a $1 \times 1$ square that does not have any other edge colored. For example (fig. $2$), the player making a move can color any of the segments marked in green. However, they cannot color any segment marked in blue because area $a$ is a square with a side of $2 \, u$ (two units), and area $b$ (a $1 \times 1$ square) already has one edge colored (the red one). Additionally, the segment marked in purple cannot be colored because the only square it belongs to, square $c$, already has a colored edge. The player who can't make any more colorings loses.

## Task

Knowing that both players play optimally and that Dubluveu always starts the game, determine if he has a winning strategy, and if so, indicate all the possibilities for him to make the first move to defeat the Prime Minister.

## Input data

The input file `jpg.in` contains the natural number $N$ which represents the number of segments drawn. It is followed by $N$ quadruples $(x1, y1, x2, y2)$, representing the coordinates of a segment.

## Output data

In the output file `jpg.out`, on the first line, print $1$ if Dubluveu has a winning strategy, or $2$ otherwise. If Dubluveu wins, the second line will contain all his possible first moves to defeat the Prime Minister. Specifically, the indices of the segments such that if the respective segment is the first one colored by Dubluveu, he will win the game, will be printed in ascending order.

## Constraints and clarifications

$1 \leq N \leq 50$ each segment has length $1$ and is parallel to $OX$ or $OY$ the coordinates are natural numbers within the interval $[0, 50]$ All segments in the input file are distinct for $30\%$ of the tests $N \leq 13$ for $60\%$ of the tests $N \leq 23$

## Example

`jpg.in`
```
8
2 1 2 0
1 2 2 2
2 2 2 1
0 2 1 2
1 1 1 2
1 0 1 1
1 1 2 1
0 1 0 2
```

`jpg.out`
```
1
3 5 8
```