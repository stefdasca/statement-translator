## Graph Game

Cristinel and Alexei found an undirected graph with $N$ nodes and $M$ edges. On each edge and node, there was a natural number written. Inspired by this masterpiece of discrete mathematics, Alexei proposed to play a game on that graph. The game is played alternately, each has to choose a node that has not been chosen before, until the graph is exhausted. At the end, the score of each player is the sum of the numbers on the chosen nodes and of the edges whose endpoints are in the set of nodes chosen by that player. Formally, the score of a player is if. Where $S$ is the set of nodes chosen by a player. What is the difference between the scores of the players, if both players play optimally and Alexei starts first? Note: Optimal play means maximizing the score difference.

## Input data

The input file `jocgraf.in` contains on the first line the number of tests $T$. 
Then follows the description of each test which starts with $N$ and $M$, the number of nodes and respectively the number of edges of the graph. On the next line are the numbers written on each node. On the next $M$ lines the edges are described as a triplet $u, v, number$ written on the edge.

## Output data

The output file `jocgraf.out` will contain $T$ lines with the correct answer (I am sure about that) for each of the $T$ tests.

## Constraints and clarifications

$0 \leq N, M \leq 10^5$

$0 \leq Number$ written on nodes $\leq 10^5$

$0 \leq Number$ written on edges $\leq 10^5$

$1 \leq T \leq 10$

## Example

`jocgraf.in`

```
1
3 3
1 1 1
1 2 1
2 3 1
3 1 1
```

`jocgraf.out`

```
2
```

## Explanation

Because all nodes and edges have a cost of $1$, it does not matter which nodes each player will choose, the score difference will always be $2$.