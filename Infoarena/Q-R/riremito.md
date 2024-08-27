## Task

Dragon Quest, a classic RPG game, provides a character named Hero for you to explore, fight monsters, and find treasures. Most of the time, the treasures are hidden in caves and labyrinths that can be described as trees with edge costs. Hardcore fans play these games countless times and eventually achieve maximum efficiency, reaching a point where they spend the minimum required time to find all the treasures in the game. What helps them move quickly through the labyrinth is a very powerful spell called Riremito. This spell teleports the player instantly to the entrance, saving a lot of time required to navigate through the labyrinths. The producers, already accustomed to these players, try hard to extend their game time so they do not get bored too quickly. They have already received the labyrinth plans from the designers and cannot change their layout, but they can choose the entrance to the labyrinth from a limited number of points. They wonder, for each of these possible entrance points, what the visiting cost of the entire tree would be (players being forced to do this to discover all the treasures).

## Input data

The input file `riremito.in` will contain on the first line $N$ the number of nodes of the tree that describes the labyrinth. The next $N - 1$ lines will describe the tree's edges, each on a separate line. Thus, on each line, there will be 3 integers $x$, $y$, and $z$ with the meaning that there is an edge from the node with index $x$ to the node with index $y$ which can be traversed in $z$ seconds. On the next line, there will be a number $K$ which represents the number of possible nodes where the entrance of the labyrinth could be placed, and the next line will contain those $K$ numbers representing the indices of the nodes where the entrance could be placed.

## Output data

The output file `riremito.out` must contain $K$ lines, one for each of the $K$ nodes from the input file, representing the minimum time to visit the entire tree with the entrance fixed at each of the $K$ nodes.

## Constraints

$1 \leq N \leq 100000$

$1 \leq x, y \leq N$

$1 \leq z \leq 1000000000$

Riremito is instantaneous and can be used any number of times

$1 \leq K \leq 10$

For 30% of the score $N \leq 20$

## Example

`riremito.in`
```
5
2 4 3
5 3 2
4 1 2
5 4 3
2
4
5
```

`riremito.out`
```
10
12
```

## Explanation

The tree structure and the edges corresponding to the input data are:

```
    1
   / 
  4 - 2
  |   |
  5 - 3
```

The edge costs are:
```
(2, 4) = 3
(5, 3) = 2
(4, 1) = 2
(5, 4) = 3
```

To visit the entire tree starting from node $4$, the minimum total time is $10$ seconds.

To visit the entire tree starting from node $5$, the minimum total time is $12$ seconds.