# Pp

Petre and Paul are playing the following game. Initially, they have a number $N$. During the game, they make moves alternately. A move consists of dividing the number $N$ by a number $P$ chosen by the player making the move, with the restriction: $2 \leq P \leq K$. Subsequently, the new value of $N$ will be $N/P$ (the integer part of the result is taken). The player who, when it's their turn, reduces the number $N$ to $0$ wins (equivalently, the player who, when it's their turn, has the number $N=0$ available, loses). Determine if the first player has a winning strategy (first player = the one who makes the first move).

## Input data

The first (and only) line of the input file `pp.in` contains the integers $N$ and $K$, separated by a space. 

## Output data

The output file `pp.out` will contain the integer $A$, where $A=1$ if the first player has a winning strategy, otherwise $A=0$. 

## Constraints

$0 \leq N \leq 2\ 000\ 000\ 000$

$2 \leq K \leq 100$ 

## Example

`pp.in` `pp.out`

`1024 7` `1`