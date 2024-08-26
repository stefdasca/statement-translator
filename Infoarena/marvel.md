## Task

Everyone knows that Marvel is the largest superhero universe. While making some kebab, Deadpool started playing a new game on his phone. The game has $N$ missions numbered from $1$ to $N$ and starts from mission $1$. Each time you complete a mission, you may unlock other missions or stop. We can represent the game as a Directed Acyclic Graph (DAG) with $N$ nodes, where the edge from $a$ to $b$ represents the fact that mission $b$ is unlocked once mission $a$ is completed. A story-line is a sequence of missions in which each mission, except for the last one, is followed by a newly-unlocked mission (in other words, a path in the graph starting from node $1$). At the end of each mission, the player has to fight an enemy. For each mission, the index of this enemy is known (a natural number from $1$ to $K$). Deadpool has a list with $P$ friends, all of whom are his enemies (that's life, what can you do). He wants to go through a story-line such that this list of friends appears as a subsequence in the sequence of enemies he faces. You need to say for how many of the $N$ missions there exists such a story-line that ends with that mission. The list can contain the same friend more than once (Deadpool sometimes has too much fun with his friends).

## Input data

The input file `marvel.in` will contain on the first line 4 numbers $N$, $M$, $K$, and $P$ representing the number of nodes, the number of edges, the number of enemies, and the number of friends in Deadpool's list. The next line will contain $N$ numbers, representing the indices of the enemies in each node. The third line will contain $P$ numbers, representing the indices of the friends Deadpool wants to fight, in the order in which they must be encountered. The following $M$ lines will contain 2 natural numbers $a$ and $b$ each, representing the fact that mission $b$ is unlocked once mission $a$ is completed.

## Output data

The output file `marvel.out` will contain a single natural number representing the number of nodes out of the $N$ for which there exists a story-line with the required property. On the second line, it will contain the indices of those nodes in ascending order.

## Constraints and clarifications

$1 \leq N \leq 100\ 000$

$1 \leq M \leq 300\ 000$

$1 \leq P \leq N$

$1 \leq K \leq N$

A mission is considered unlocked if at least one of the missions that can unlock it has been completed. A subsequence $B$ of a sequence $A$ is obtained by deleting certain elements from $A$, possibly none or possibly all. The elements that are not deleted remain in the same order.

## Example

`marvel.in`

```
6 7 3 2
2 1 3 2 2 1
3 2
1 2
1 3
2 4
3 6
6 4
3 4
3 5
```

`marvel.out`

```
2
4 5
```

For mission $4$, there is the path of missions $1 \rightarrow 3 \rightarrow 6 \rightarrow 4$, which has associated enemies $2 \ 3 \ 1 \ 2$. The sequence $3 \ 2$ appears as a subsequence of this.