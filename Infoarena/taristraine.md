## Task

Since our protagonist, Sorin Pastrama, is wealthy, he desires to travel to foreign countries. Everyone knows he values himself highly, so he has chosen the most luxurious airline and decided to travel only with it. The company operates in $N$ large cities around the world, with various flights between them. More precisely, these routes constitute a tree with $N$ nodes, rooted at node $1$, with each edge (representing a flight in both directions) having a certain cost. Since Pastrama is not very good at mathematics (because he attended a school of cunning), he asks you to help him with the following $M$ operations:
- $1\:x\:c$ $\rightarrow$ the cost of the edge from $x$ to its parent becomes $c$ $($ $2 \leq x \leq N$ $)$ 
- $2\:x\:y$ $\rightarrow$ Pastrama wants to travel from node $x$ to node $y$. At each step, if he is at a certain node different from $y$, he will choose with equal probability a neighbor of this node and go there, paying the corresponding cost, of course. He will repeat this until he reaches node $y$. Pastrama would like to know the expected cost of this trip ($y$ is an ancestor of $x$).

## Input data

The input file `taristraine.in` contains on the first line the natural numbers $N$ and $M$, with the meanings given in the statement. On the next $N-1$ lines there are two natural numbers $T\:i$ and $C\:i$ which represent the parent of node $i$ and the cost of the respective edge ($2 \leq i \leq N$). On the next $M$ lines there are the $M$ operations described in the statement.

## Output data

The output file `taristraine.out` will contain the answers to the type $2$ operations, each on a separate line, in the order they appear in the input file. Print the answers in the form $p/q$, where the answer (expected value) is equal to $p/q$ and the lowest common multiple of $p$ and $q$ is $1$.

## Constraints and clarifications

$1 \leq N, M \leq 10^5$

$1 \leq costul unei muchii \leq 10^6$

In the type $2$ operation, the node $y$ is an ancestor of the node $x$ 

Pastrama pays for his pleasures, and therefore the luxury company he chose only owns American planes 

## Example

`taristraine.in`

```
3 2
1 10
1 7
1 2 5
2 2 1
```

`taristraine.out`

```
5 1
```

## Explanation

First operation: the cost of the edge $1 \rightarrow 2$ becomes $5$.

Second operation: the only neighbor of node $2$ is $1$, so the only option is to go there. Thus, the expected cost is $5$.