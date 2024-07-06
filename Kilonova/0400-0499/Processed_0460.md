```markdown
The Prime Minister of Great Britain, Rishi Sunak, has decided to reorganize the administrative structure of Oxfordshire county. In Oxfordshire, there are $N$ towns numbered from $1$ to $N$, connected by $M$ highways (one-way roads connecting $2$ towns). Rishi has decided that all towns to which citizens of all other towns can reach via the highways should become residences. Because the number of towns and highways in Oxfordshire is very large, Rishi asks for your help in solving two key problems.

# Task
1. What are the indices of the residence towns in Oxfordshire;
2. What is the minimum distance from each town to the nearest residence town.

# Input data
It will be read from the console. The input data contains on the first line $3$ numbers $C$, $N$ and $M$, separated by a space, where $C$ represents the task number, $N$ the number of towns, and $M$ the number of highways. The next $M$ lines contain $3$ numbers $i$, $j$, and $d$, separated by spaces, representing the description of the highways: there is a highway from town with index $i$ to town with index $j$ of length $d$.

# Output data
A single line will be displayed. If $C = 1$, the indices of the residences will be displayed, in increasing order, separated by spaces. If $C = 2$, $N$ numbers will be displayed, separated by spaces, representing the minimum distances from each town (with indices from $1$ to $N$) to the nearest residence of that town (if the town is a residence, $0$ will be displayed).

# Constraints and clarifications
* $2 \leq N \leq 10^5$;
* $1 \leq M \leq min(N * (N − 1), 2 * 10^5)$;
* $1 \leq d \leq 10^4$;
* There is no highway that connects a town to itself;
* No multiple highways connect the same two towns in the same direction;
* In all tests, there is at least one residence;
* Subtask $1$, $20$ points: $C = 1$ and $N \leq 1\ 000$;
* Subtask $2$, $40$ points: $C = 1$;
* Subtask $3$, $10$ points: $C = 2$ and $N \leq 1\ 000$;
* Subtask $4$, $30$ points: $C = 2$.

# Example 1

`stdin`
```
1 6 6
4 3 2
2 4 4
4 2 2
5 4 6
6 2 7
1 3 10
```

`stdout`
```
3
```

# Example 2

`stdin`
```
2 9 12
8 4 30
4 6 16
6 1 13
6 5 1
5 2 26
7 2 10
3 9 23
9 3 5
1 4 7
4 5 18
2 5 8
9 2 19
```

`stdout`
```
24 0 42 17 0 1 10 47 19
```

# Explanation

For the first example, the town with index $3$ is the only residence as it is the only town reachable from all other towns (see Figure 1). For the second example, there are two residence towns: towns with indices $2$ and $5$. Towns with indices $1$, $4$, $6$, and $8$ are closer to the residence with index $5$. Towns with indices $3$, $7$, and $9$ are closer to the residence with index $2$ (see Figure 2).

~[fig.png]
```

Note: I have preserved the specific format requirements and the custom image format as per your instructions. Please review for correctness and clarity.