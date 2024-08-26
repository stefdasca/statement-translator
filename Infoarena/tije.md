# Rods

Consider $N+1$ rods, numbered from $1$ to $N+1$. The rods $1 \dots N$ each contain $N$ balls. The balls on rod $i$ all have the color $i$. Rod $N+1$ is empty. At any moment, you can perform the following type of moves: take a ball from the top of a source rod and place it on top of a destination rod, provided that the source rod contains at least one ball before the move, and the destination rod contains at most $N$ balls after the move. Determine a sequence of moves such that, after executing the moves, each rod from $1$ to $N$ will have $N$ balls, each ball having a different color, and rod $N+1$ will be empty.

## Input data

The first (and only) line of the file $tije.in$ contains the integer $N$.

## Output data

In the output file $tije.out$, you will display the moves made, in order, one per line. A move is displayed as two distinct rod numbers, $A$ and $B$, separated by a space, meaning that a ball is moved from the top of rod $A$ to the top of rod $B$.

## Constraints and clarifications

$1 \leq N \leq 100$

The minimum number of moves is not required.

The final order of balls on rods $1 \dots N$ does not matter (it only matters that there is one ball of each color on each rod from $1$ to $N$).

## Example

`tije.in`

```
2
```

`tije.out`

```
2 3
1 3
1 2
3 1
3 1
```