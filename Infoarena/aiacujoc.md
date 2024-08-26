## Task

The two decide to play multiple games. Help Bulănel find, for each game, the number of positions where he can place the initial square so that he has a winning strategy, meaning he can win regardless of Bulănița's moves.

## Input data

The input file `aiacujoc.in` contains the natural number $T$ on the first line, representing the number of games Bulănel and Bulănița will play. Each of the next $T$ lines contains three natural numbers that define a game: the natural number $N$, representing the number of rows in the grid, followed by the natural number $M$, representing the number of columns in the grid, followed by the natural number $K$, representing the maximum number of rows or columns with which a player can extend the figure at a certain step.

## Output data

The output file `aiacujoc.out` will contain $T$ lines. Each line $i$ will contain one natural number representing the number of positions on the grid where Bulănel can place the initial square that guarantees him a winning strategy for the $i$-th game.

## Constraints and clarifications

For all tests,
$$1 \leq T \leq 10$$

For tests worth $5$ points,
$$N = 1$$ 
$$1 \leq M \leq 20$$ 
$$K \geq \text{max}(N, M)$$

For other tests worth $5$ points,
$$1 \leq N, M \leq 20$$ 
$$K \geq \text{max}(N, M)$$ 
$$N \text{ and } M \text{ have different parities}$$

For other tests worth $10$ points,
$$1 \leq N, M \leq 20$$ 
$$K \geq \text{max}(N, M)$$

For other tests worth $30$ points,
$$1 \leq N, M \leq 1\ 000$$ 
$$K \geq \text{max}(N, M)$$

For other tests worth $10$ points,
$$1 \leq N, M \leq 1\ 000\ 000$$ 
$$K \geq \text{max}(N, M)$$

For other tests worth $20$ points,
$$1 \leq N, M, K \leq 1\ 000\ 000$$

For other tests worth $10$ points,
$$1 \leq N, M \leq 1\ 000\ 000\ 000$$ 
$$1 \leq K \leq 1\ 000\ 000$$

Both players play optimally, which means they do not make mistakes, anticipate the opponent's moves, and if there is a strategy of moves that leads them to win, they will use it. The problem will be evaluated on tests worth $90$ points.

## Examples will represent tests worth

$10$ ("points by default") and will have feedback.

## Example

`aiacujoc.in`
```
2
3 5 5
88 200 200
```

`aiacujoc.out`
```
320
7680
```

## Explanation

First example For the first game, the grid has dimensions $N=3$, $M=5$. A player can extend the figure by a maximum of $K=5$ rows or columns. The positions that guarantee Bulănel a winning strategy are $(1;2)$, $(1;4)$, $(2;3)$, $(3;2)$, $(3;4)$.

For the second game, the grid has dimensions $N=88$, $M=200$. A player can extend the figure by a maximum of $200$ rows or columns. There are $320$ positions that lead to a win.

Second example For the first game, the grid has dimensions $N=3$, $M=5$. A player can extend the figure by a maximum of $K=3$ rows or columns. The positions that guarantee Bulănel a winning strategy are $(1;2)$, $(1;4)$, $(2;1)$, $(2;3)$, $(2;5)$, $(3;2)$, $(3;4)$.

For the second game, the grid has dimensions $N=88$, $M=200$. A player can extend the figure by a maximum of $56$ rows or columns. There are $7680$ positions that lead to a win.