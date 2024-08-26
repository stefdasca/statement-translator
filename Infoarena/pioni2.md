## Task

Nargy and Fumeanu are playing a game on a directed acyclic graph with $N$ nodes (numbered from $1$ to $N$) and $M$ arcs. In this graph, there are $K$ pawns placed in nodes. Each player must move, when it's their turn, all the pawns that can be moved from the nodes they are currently in to adjacent nodes. More precisely, a pawn located in node $x$ can be moved to node $y$ if there is an arc from $x$ to $y$. The player who cannot move any pawn when their turn comes loses the game. At the beginning of a game, the first move is made by the player Nargy. Given multiple configurations of pawns, determine who wins the game if both players play optimally.

## Input data

The input file `pioni2.in` contains on the first line 3 natural numbers $T\ N\ M$. The following $M$ lines will contain two natural numbers $a\ b$ indicating that there is an arc from $a$ to $b$. The following $T$ lines will describe pawn configurations as follows: the first number on the line will be $K$ and will be followed by $K$ natural numbers representing the nodes in which the pawns are located. The numbers on each line are separated by spaces.

## Output data

The output file `pioni.out` will contain $T$ lines, one line for each pawn configuration from the input file. The $i$-th line will contain the name of the player who wins (Nargy or Fumeanu) for the $i$-th pawn configuration from the input file.

## Constraints and clarifications

$1 \leq T \leq 5$  
$1 \leq N \leq 20\ 000$  
$1 \leq M \leq 50\ 000$  
$1 \leq K \leq 30\ 000$

There may be multiple pawns in the same node.

## Example

`pioni2.in`  
```
2 4 3
2 1
3 1
4 3
3 2 2 3
2 1 4
```

`pioni2.out`  
```
Nargy
Fumeanu
```

## Explanation

1. According to the game rules, Nargy must move all 3 pawns, and the only possibility is to move them all to $1$. Fumeanu cannot move anymore.
2. Nargy moves the pawn from $4$ to $3$, and Fumeanu moves from $3$ to $1$. These are the only possible moves.