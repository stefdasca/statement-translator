## Task

Recently, Bulănel started taking salsa lessons. Being an accomplished dancer, he quickly learned $N$ moves, numbered from $1$ to $N$, which he can use at parties. For each move $i$, he knows exactly one move, $nextMove[i]$, with which he can continue. Each move takes one second to execute. The songs at parties have various lengths. Curious by nature, Bulănel sometimes wonders in how many ways he can dance to a song of $X$ seconds. To avoid boring the girls, during the song Bulănel must use only different moves. He can start with any move he wants. Help Bulănel find out in how many ways he can dance to a song of $i$ seconds for each $i$ between $1$ and $N$. Two ways are considered different if there exists an index $i$ such that the moves performed at second $i$ in the two ways are different.

## Input data

The input file `salsa.in` contains a whole number $N$ on the first line, representing the total number of moves. The next line contains $N$ whole numbers, the $i$-th of these representing $nextMove[i]$, the move that can be executed after move $i$.

## Output data

The output file `salsa.out` should contain $N$ whole numbers, the $i$-th of these representing the answer to question $i$ - specifically, the number of ways Bulănel can dance to a song of $i$ seconds.

## Constraints and clarifications

$2 \leq N \leq 100 \ 000$
 
It is guaranteed that $nextMove[i] \ne i$ and $1 \leq nextMove[i] \leq N$, for any $i$ between $1$ and $N$.
 
For some tests worth $10$ points, it is guaranteed that the array $nextMove[\ ]$ will have all distinct elements.
 
For other tests worth $10$ points, it is guaranteed that $2 \leq N \leq 1 \ 000$.
 
The problem will be evaluated on tests worth $90$ points.

## Examples

``
salsa.in
4
4 1 2 2

salsa.out
4 4 4 1
``

## Explanation

In the first example:
For a song of $1$ second, Bulănel can perform $4$ valid sequences of moves: $1$, $2$, $3$, $4$.

For a song of $2$ seconds, Bulănel can perform $4$ valid sequences of moves: $1-4$, $2-1$, $3-2$, $4-2$.

For a song of $3$ seconds, Bulănel can perform $4$ valid sequences of moves: $1-4-2$, $2-1-4$, $3-2-1$, $4-2-1$.

For a song of $4$ seconds, Bulănel can only perform one valid sequence of moves: $3-2-1-4$.