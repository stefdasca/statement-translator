Below is the translated text in English, preserving the required format and details:

```
It is known that in a connected undirected graph, between any two vertices there is at least one path and the length of a path is equal to the number of edges that compose it. We define the notion of an *optimal path between two vertices $X$ and $Y$* as a path of minimal length that has the vertices $X$ and $Y$ as endpoints. It is evident that between any two vertices of a connected graph, we will have one or more optimal paths, depending on the configuration of the graph.

# Task:
Given a connected undirected graph with $N$ vertices labeled with the ordinal numbers $1, 2, ..., N$ and two of its vertices denoted $X$ and $Y$ ($1 \leq X, Y \leq N, X \neq Y$), write a program that determines the vertices that belong to all optimal paths between $X$ and $Y$.

# Input data:
The file `graf.in` contains 
- The first line contains four natural numbers representing $N$ (the number of vertices of the graph), $M$ (the number of edges), $X$ and $Y$ (as described above).
- The next $M$ lines each contain two non-zero natural numbers $A_i, B_i$ ($1 \leq A_i, B_i \leq N,  A_i \neq B_i$, for $1 \leq i \leq M$), each pair of numbers representing an edge in the graph.

# Output data:
The file `graf.out` will contain
- The first line contains the number of vertices common to all optimal paths between $X$ and $Y$;
- The second line contains the labels of these vertices in ascending order; between any two consecutive numbers on this line there will be a space.

# Constraints and clarifications:
* $2 \leq N \leq 7\ 500$
* $1 \leq M \leq 14\ 000$
* For $50\%$ of the tests $N \leq 200$

# Examples

`graf.in`
```
6 7 1 4
1 2
1 3
1 6
2 5
3 5
5 6
5 4
```

`graf.out`
```
3
1 4 5
```

`graf.in`
```
3 2 1 3
1 2
3 1
```

`graf.out`
```
2
1 3
```
```

Please review the translated text to ensure accuracy and adherence to the provided instructions.