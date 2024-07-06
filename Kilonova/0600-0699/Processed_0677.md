# Task

The cat _Somnorilă_ is a very sleepy cat! While he was sleeping, he had a dream in which he was together with a mouse in a maze. What is special about this maze is that all the roads between the maze rooms can be traversed in only one direction, and during a walk through the maze he cannot pass through the same room twice. Moreover, only the cat knows the map of the maze, the mouse not having the courage to move from his current room. Being a delicate cat, Somnorilă wants to know if from the room he is currently in, he can reach the room of the mouse, so he can know after he wakes up if his dream was a nightmare or a dream!

Formally, you are given a directed acyclic graph (DAG) with $N$ nodes and $M$ edges, and $Q$ questions of the form: can node $Y$ be accessed from node $X$?

# Task

You need to answer all $Q$ questions of Somnorilă.

# Input data

The first line contains the numbers $N$ and $M$, where $N$ represents the number of nodes of the graph, and $M$ the number of edges. On the next $M$ lines, there will be two numbers $X$ and $Y$, indicating that there is an edge from node $X$ to node $Y$ in the graph. On line $M + 2$ there will be the number $Q$, which represents the number of questions. On the next $Q$ lines, there will be numbers $X$ and $Y$, representing a question.

# Output data

The answer for each question will be printed on a separate line, in the following format: on line $i$ the answer to the $i$-th question will be printed. Print $1$ if from node $X_i$ you can reach node $Y_i$, otherwise print $0$.

# Constraints and clarifications

* $1 \leq N \leq 50\ 000$
* $1 \leq M \leq 200\ 000$
* $1 \leq Q \leq 100\ 000$
* It is guaranteed that in an edge and in a query node $X$ will be at a lower level compared to node $Y$.
* It is guaranteed that for each node on level $X \ (X > 1)$ there will be at least one edge with a node from level $X - 1$, $(\forall) \ X > 1$.
* For $28$ points, $1 \leq N, Q \leq 1\ 000$, the tests are **NOT** grouped.
* For other $72$ points, the original constraints apply, and the tests are grouped into $4 - 5$ tests / group.

# Example

`stdin`
```
12 13
1 4
2 5
3 5
4 6
4 7
4 11
5 6
5 8
5 12
6 9
7 9
7 10
11 12
4
1 9
4 8
7 12
3 6
```

`stdout`
```
1
0
0
1
```

## Explanation

~[5712ba4c6c860cf4a83f1bd85f7e706e.png]

* Node $9$ can be accessed from node $1$. (Example of path: $1 \rightarrow 4 \rightarrow 6 \rightarrow 9$)
* Node $8$ cannot be accessed from node $4$.
* Node $12$ cannot be accessed from node $7$.
* Node $6$ can be accessed from node $3$. (Example of path: $3 \rightarrow 5 \rightarrow 6$)