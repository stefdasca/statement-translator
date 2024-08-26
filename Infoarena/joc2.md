## Task

Two participants take turns eating from chocolate bars following these rules:
- Cut a bar into two, the cut must be parallel to one of the sides of the bar and must not cut the chocolate squares.
- Break and eat any row or column of squares that is not on the edge of the bar.
- Break and eat all the squares on the edge of the bar, provided the remaining bar is at least $1 \times 1$ in size.

None of these three moves can be made on a bar of size $1 \times 1$. The player who can no longer make a move loses.

## Input data

The input file `joc2.in` will contain the number $N$ of bars, and on the next $N$ lines it will contain pairs of integers representing the dimensions of the bars.

## Output data

The output file `joc2.out` will contain a single integer, which represents the number of ways to make the first move such that there is a strategy to win the game.

## Constraints and clarifications

$1 \leq N \leq 100$

the dimensions of the bars are between $1$ and $100$

the first player always moves first

it is assumed that both participants play optimally

the move is identified by the bar on which it is made, by type, and by the row/column it affects.

## Example

`joc2.in`
```
2
1 2
2 2
```

`joc2.out`
```
0
```

## Explanation

In the first move, the first player can either split the first bar into two, resulting in two bars of 1 square, and one of 4 squares. In the second move, the second player can split (either horizontally or vertically) the 4-square bar into two bars of 2 squares. In the third move, the first player can split one of the 2-square bars into two bars of 1 square and one of 2 squares. In the fourth move, the second player can split the remaining 2-square bar into two bars of 1 square. The first player can no longer make a move.

Another game variant could be:
In the first move, the first player can split (either horizontally or vertically) the 4-square bar into three bars of 2 squares. In the second move, the second player can split one of the 3 2-square bars into two bars of 1 square and 2 of 2 squares. In the third move, the first player can split one of the 2 2-square bars into two bars of 1 square and one of 2 squares. In the fourth move, the second player can split the remaining 2-square bar into two bars of 1 square. The first player can no longer make a move. In conclusion, no matter what the first player does in the first move, they will always lose the game.