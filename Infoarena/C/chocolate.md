## Task

Consider a chocolate bar with $N$ rows and $M$ columns. The piece of chocolate at position $(X, Y)$ is poisoned. We consider the following game: There are 2 players who move alternately. When a player is to make a move, they choose a non-zero number $K$ and make one of the following actions:
1. Eat the first $K$ rows of the chocolate bar.
2. Eat the last $K$ rows of the chocolate bar.
3. Eat the first $K$ columns of the chocolate bar.
4. Eat the last $K$ columns of the chocolate bar.

The player who eats the poisoned piece of chocolate loses. Considering that the two players play optimally, is there a guaranteed winning strategy for the player who makes the first move?

## Input data

The input file `chocolate.in` will contain on the first line a number $T$. The following $T$ lines contain each a case in the format: $N$ $M$ $X$ $Y$.

## Output data

The output file `chocolate.out` will contain exactly $T$ lines. Line $i$ will contain the number 1 if the player who moves first has a guaranteed winning strategy for that game or 0 otherwise.

## Constraints

$1 \leq T \leq 10$

$1 \leq N, M \leq 1000\ 000$

For tests worth 60 points:
$X = 1, Y = 1$. In other words, the poisoned piece is at the corner of the bar.

For the rest of the tests (worth 40 points), it is guaranteed that $X$ and $Y$ are STRICTLY inside the bar.

## Example

`chocolate.in`
```
3
1 1 1 1
1 3 1 1
4 4 1 3
```

`chocolate.out`
```
0
1
0
```

## Explanation

In the first case, the chocolate is formed only by the poisoned piece. Obviously, the first player loses because they are forced to eat at least one row or column.

In the second case, the first player can eat the last 2 columns of the bar. The second player will lose, for the same reason the first player loses the first case.

The third case is a bit more complicated $\dots$.