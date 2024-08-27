# Flower

One day, when they were bored, Ana and her friends invented a new game, which they played $T$ times. The girls have a flower with $N$ petals and, in one move, they can pluck a minimum of one and a maximum of $K$ of them. Tradition says that the lucky girl who plucks the last petals of the flower will receive $A_0$ red roses, the next one would receive $A_1$ red roses, and so on until the one who moved just before the winner, who receives $A_{M-1}$ roses. Ana can decide the order in which the girls will pluck the petals. Help her, for each of the $T$ games, to win as many roses as possible.

## Input data

The input file `floare.in` contains on the first line the 3 numbers, $M$ - the number of players, $K$ - the maximum number of petals that can be taken in one move, and $T$ - the number of games. The second line contains the sequence $A$. Each of the next $T$ lines contains $N$ - the number of petals of the flower for that game.

## Output data

The output file `floare.out` will contain $T$ numbers, the position of the winning girl for each of the $T$ rounds of the game.

## Constraints and clarifications

$1 \leq T \leq 100$

$1 \leq M \leq 200\ 000$

$1 \leq N \leq 200\ 000$

$1 \leq K \leq 200\ 000$

It is known that each girl plays optimally, meaning she wants to win as many roses as possible.

The values in the sequence $A$ are distinct.

For tests worth at least 30 points, the values of $N$ will be less than or equal to $1\ 000$.

## Example

`floare.in`

```
2 3 1
2 1
6
1
```

`floare.out`

```
1
```

## Explanation

A winning strategy for the first player in the above example could be: take $2$ petals, leaving the flower with $4$ petals. From here, no matter how many petals the second player plucks $(1, 2$ or $3)$, the first player will be able to take whatever is left.