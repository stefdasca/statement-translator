```markdown
Gigel has a graph with $n$ nodes and $m$ edges, which is not connected. He wants to find out the answer to two questions:

1) What is the minimum number of edges that need to be added for the graph to become connected?
2) If the cost of adding an edge between nodes $a$ and $b$ is $a + b$, what is the minimum total cost of the edges that need to be added for the graph to become connected?

# Input data

The input file `unire.in` contains the numbers $n$ and $m$ on the first line, the number $c$ on the second line, representing the task number $1 \leq c \leq 2$, and on the following $m$ lines are the edges of the graph $a \ b$,  $1 \leq a, b \leq n$, $a \neq b$.

# Output data

The output file `unire.out` will contain on the first line the number $S$, representing the answer Gigel asked for.

# Constraints and clarifications

* $1 \leq n \leq 100\ 000$, $0 \leq m < n-1$
* For tests worth $30$ points, the task will be 1.
* For tests worth $40$ points, $1 \leq n \leq 1\ 000$.

# Example 1

`unire.in`
```
6 3
1
1 2
3 4
5 6
```

`unire.out`
```
2
```

# Example 2

`unire.in`
```
6 3
2
1 2
3 4
5 6
```

`unire.out`
```
10
```

## Explanation

Nodes $1$ and $3$ will be connected, respectively nodes $1$ and $5$. $2$ edges were used, and the total cost will be $1 + 3 + 1 + 5 = 10$.
```