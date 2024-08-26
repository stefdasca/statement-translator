# Moves

## Task

While bored by the too easy problems on the board during math class, Marian discovered a new game: starting from an array of $N$ natural numbers $A(1)$, $A(2)$, $\dots$, $A(N)$, he needs to reach the array $A(1)$, $0$, $\dots$, $0$ by performing one or more moves. A move consists of choosing a position $K$ $\left( 1 \leq K < N \right)$ and then subtracting the value of $A(K)$ from $A(K + 1)$. The numbers in the array are not allowed to become negative during the moves. Since he is not very skilled in computer science, he thought to ask you, his friends, to tell him if there exists a sequence of moves that solves the game.

## Input data

The input file `mutari.in` will contain on the first line $N$ and on the second line the $N$ natural numbers: $A(1)$, $A(2)$, $\dots$, $A(N)$.

## Output data

The output file `mutari.out` will display on the first line the number of moves $T$ necessary to solve the game, if possible. On the next $T$ lines, it will contain a number representing the position $K$ chosen for the current move. If the game has no solution, it will display $-1$ on the first line.

## Constraints and clarifications

$1 \leq N \leq 100000$

$1 \leq A(i) \leq 2000000000$

It is guaranteed that there will be a solution with $T \leq 1000000$. It is not required to find the minimal $T$. Any correct solution is accepted.

## Example

`mutari.in`

```
5
2 4 2 6 8
```

`mutari.out`

```
8
3
4
4
3
3
1
2
1
```

## Explanation

$2$, $4$, $2$, $6$, $8 \rightarrow 2$, $4$, $2$, $4$, $8 \rightarrow 2$, $4$, $2$, $4$, $4 \rightarrow 2$, $4$, $2$, $4$, $0 \rightarrow 2$, $4$, $2$, $2$, $0 \rightarrow 2$, $4$, $2$, $0$, $0 \rightarrow 2$, $2$, $2$, $0$, $0 \rightarrow 2$, $2$, $0$, $0$, $0 \rightarrow 2$, $0$, $0$, $0$, $0$

There are also other sequences of moves that lead to the array $2$, $0$, $0$, $0$, $0$.