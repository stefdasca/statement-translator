
Alex, a great tourism enthusiast, decided to turn his passion into a business and organize tours of the city of Bistrița. The city can be represented as a **directed** graph of tourist attractions, directly connected by streets. However, since Alex's ability to navigate is not comparable to his enthusiasm, organizing the routes is difficult for him. Firstly, he wants to count how many such routes exist in the city. A route represents an ordered list $a$ of $k$ tourist attractions, with the following properties:

* From node $a_i$ one can reach node $a_{i+1}$, for $1 \le i < k$;
* From node $a_k$ one can reach node $a_1$.

We say that one can reach from node $x$ to node $y$ if there is a path of **$0$ or more streets** that starts at node $x$ and ends at node $y$. There are $2$ types of tourist routes:

* Type $1$, where attractions can repeat;
* Type $2$, where attractions must be distinct.

# Task

The graph of tourist attractions is a directed graph where an edge from $x$ to $y$ represents a direct path from node $x$ to node $y$. Alex needs your help to determine how many routes of length $k$ exist for a given type of tourist routes (Type $1$ or Type $2$), for each $k$ from $1$ to $Q$.

# Input data

The first line contains $T$, the type of route. The second line contains $N$, $M$, and $Q$, representing the number of nodes and edges of the graph, respectively the maximum $k$ for which Alex wants to find out the number of routes. The next $M$ lines each contain 2 numbers $x$, $y$, representing a **directed** edge from $x$ to $y$.

# Output data

For each line $k$, from $1$ to $Q$, print the number of routes of length $k$, **modulo $10^9 + 7$**.

# Constraints and clarifications

* $1 \leq N \leq 300\ 000$
* $1 \leq M, Q \leq 1\ 000\ 000$

| # | Points | Restrictions |
| - | - | - |
| 1 | 7 | $T = 1$, $N \leq 6$, $M \leq 30$, $Q \leq 30$ |
| 2 | 15 | $T = 1$, $N \leq 50$, $M \leq 100$, $Q \leq 50$ |
| 3 | 17 | $T = 1$, $N \leq 10^3$, $M \leq 2 \cdot 10^3$, $Q \leq 10^3$ |
| 4 | 21 | $T = 1$, $N \leq 10^5$, $M \leq 2 \cdot 10^5$, $Q \leq 10^5$ |
| 5 | 8 | $T = 2$, $N \leq 10^3$, $M \leq 2 \cdot 10^3$, $Q \leq 10^3$ |
| 6 | 20 | $T = 2$, $N \leq 10^5$, $M \leq 2 \cdot 10^5$, $Q \leq 10^5$ |
| 7 | 12 | $T = 2$, $N \leq 3 \cdot 10^5$, $M \leq 10^6$, $Q \leq 10^6$ |

# Example 1

`turism.in`
```
1
3 2 3
1 2
2 1
```

`turism.out`
```
3
5
9
```

## Explanation
Routes of length $1$ are: $(1)$, $(2)$, $(3)$;
Routes of length $2$ are: $(1, 1)$, $(1, 2)$, $(2, 1)$, $(2, 2)$, $(3, 3)$;
Routes of length $3$ are: $(1, 1, 1)$, $(1, 1, 2)$, $(1, 2, 1)$, $(2, 1, 1)$, $(1, 2, 2)$, $(2, 1, 2)$, $(2, 2, 1)$, $(2, 2, 2)$, $(3, 3, 3)$.

# Example 2

`turism.in`
```
2
3 2 3
1 2
2 1
```

`turism.out`
```
3
2
0
```

## Explanation

Routes of length $1$ are: $(1)$, $(2)$, $(3)$.
Routes of length $2$ are: $(1, 2)$, $(2, 1)$.

# Example 3

`turism.in`
```
1
5 4 10
1 2
2 3
3 1
3 4
```

`turism.out`
```
5
11
29
83
245
731
2189
6563
19685
59051
```

# Example 4

`turism.in`
```
2
6 7 4
1 2
2 3
3 4
4 5
5 3
3 1
3 6
```

`turism.out`
```
6
20
60
120
```

# Example 5

`turism.in`
```
1
8 9 15
1 2
2 3
3 4
2 1
4 5
5 6
6 7
7 8
8 2
```

`turism.out`
```
8
64
512
4096
32768
262144
2097152
16777216
134217728
73741817
589934536
719476260
755810045
46480318
371842544
```
