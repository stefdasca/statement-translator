## Task

Two players (numbered $1$ and $2$) play the following game: They have $N$ piles, numbered from $1$ to $N$. Pile $i$ contains $gp_i$ stones. The two players take alternate turns, with the first move being made by player $1$. A move consists of choosing a pile (with $G>0$ stones) and performing one of the following actions:

- if $G\geq1$, the player can take one stone from the pile.
- if $G\geq2$, the player can split the pile into two piles containing $G_1$ and $G_2$ stones, such that $G_1 + G_2 = G$, $G_1 >0$ and $G_2 >0$.
- if $G\geq3$, the player can take one stone from the pile, and split the remainder into two piles containing $G_1$ and $G_2$ stones, such that $G_1 + G_2 = G-1$, $G_1 >0$ and $G_2 >0$.

The game ends when no more moves can be made (all piles are empty), and the player who made the last move is the winner. Write a program that determines which of the two players has a guaranteed winning strategy.

## Input data

The first line of the input file `g.in` contains the natural number $T$, representing the number of tests described in the file. A test consists of two lines: the first line contains the initial number of piles $N$, and the second line contains the numbers $gp_1, \dots, gp_N$, separated by spaces.

## Output data

The output file `g.out` will contain $T$ lines, one for each test, in the order in which the tests appear in the input file. Each line will contain the number $1$, if player 1 has a guaranteed winning strategy, or $2$, if player 2 has a guaranteed winning strategy.

## Constraints and clarifications

$1 \leq T \leq 16$

$1 \leq N \leq 100000$

The number of stones in a pile is an integer in the interval $[1, 2100000000]$.

## Example

`g.in`
```
5
1
1
1
2
1
3
3
1 2 3
4
1 3 2 4
1
1
```

`g.out`
```
1
1
2
1
2
```