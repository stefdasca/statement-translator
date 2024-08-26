# Knights

Nargy and Fumeanu are playing a game on a directed acyclic graph with $N$ nodes and $M$ edges. In this graph, there are $K$ knights in nodes. Each player can move, when it is their turn, as many knights as they want from their nodes to adjacent nodes. The player who cannot move when it is their turn loses the game. At the beginning of a game, the first move is made by player Nargy. Given multiple configurations of knights, determine who wins the game if both players play optimally.

## Input data

The input file `pioni.in` contains on the first line the numbers $T$ $N$ $M$ separated by spaces. The next $M$ lines contain two natural numbers $a$ $b$ indicating that there is an edge from $a$ to $b$. The following $T$ lines will describe configurations of knights as follows: the first number in the line will be $K$ and will be followed by another $K$ natural numbers representing the nodes in which there are knights.

## Output data

The output file `pioni.out` will contain the following for each of the $T$ configurations: the name of the player who wins on a line (Nargy or Fumeanu), if Nargy can win, it will also describe a first move that Nargy can make to win: the number representing the number of knights they move in the first turn, followed by pairs of numbers $a$ $b$ indicating that a knight is moved from node $a$ to node $b$.

## Constraints and clarifications

$1 \leq T \leq 5$

$1 \leq N \leq 20\ 000$

$1 \leq M \leq 50\ 000$

$1 \leq K \leq 30\ 000$

Multiple knights can exist in the same node

## Example

`pioni.in`
```
2 4 3
2 1 3
1 4
3 3
2 2
3 2 1 4
```
`pioni.out`
```
Nargy 3 2 1 2 1 3 1
Fumeanu
```

## Explanation

In the first configuration, Nargy can win by moving all the knights from nodes $2$ and $3$ to node $1$. Thus, Fumeanu will not be able to move. In the second configuration, the only knight that can be moved is the one from $4$ (node $1$ has no adjacent nodes). Therefore, Nargy is forced to move from $4$ to $3$, Fumeanu will then move from $3$ to $1$, and Nargy will lose.