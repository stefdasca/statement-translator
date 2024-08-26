Otilia

Otilia and Burbucel, standing in front of a pile of $N$ stones and having nothing to do, establish the rules of a new game. The two children want the game to be simple, so they impose only three rules:

1. The first player is allowed to take at most $K$ pieces from the pile.
2. Except for the first move, each player is allowed to take at most $P * t$ stones, where $t$ is the number of stones that were taken from the pile in the previous move.
3. The player who moves last (the one who takes the last stones from the pile) loses.

The two have played many games, with Burbucel always choosing the numbers $N$, $K$, and $P$, and Otilia being the first player to move. Otilia noticed that Burbucel's choices repeat after $M$ games (the choice number $M+1$ is identical to choice number $1$, choice number $M+2$ is identical to choice number $2$, $\dots$). She would like to know if she can win or not for each of the first $M$ choices of Burbucel. The reason is easy to intuit: Otilia does not want to give Burbucel the chance to win, so she will give up on the games where she does not have a winning strategy.

## Task

Write a program that solves Otilia's dilemma.

## Input data

The first line of the file `otilia.in` contains $M$, the number of Burbucel's choices.
The next $M$ lines contain three numbers each, $N$, $K$, and $P$ representing one of Burbucel's choices ($N$ - the number of stones in the pile, $K$ - the maximum number of stones Otilia can take on her first move, $P$ - the factor by which the number of stones taken on the previous move is multiplied, resulting in the maximum number of stones that can be taken on the current move).

## Output data

The file `otilia.out` contains $M$ lines, with line $i$ containing $1$ if Otilia wins on Burbucel's choice number $i$, or $0$ if she loses (the choices are numbered from $1$ to $M$ in the order found in the input file).

## Constraints

$1 \leq M \leq 30\,000$

$1 \leq N \leq 5\,000\,000$

$1 \leq K \leq N$

$1 \leq P \leq 10$

For $50 \%$ of the tests $N \leq 500\,000$ for all of Burbucel's choices

## Example

`otilia.in`
```
4
1 1 3
3 2 8
5 1 3
100 1 1
```

`otilia.out`
```
1
0
1
0
```