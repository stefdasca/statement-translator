Adi and Sorin want to visit the country this summer. The country in which they live can be represented as a graph with $N$ nodes (where each node represents a city in the country) and $M$ weighted edges (where each edge represents a bidirectional road between two cities, and the weight of the edge represents the length of the road in kilometers).

As we know, the two adore the cities of Constanța and Timișoara. Therefore, they decided that their route through the country must pass through these two cities. Formally, we will denote by $X$ the node representing the city of Constanța and by $Y$ the node representing the city of Timișoara. We will denote by $d(u,v)$ the length of a road from node $u$ to node $v$ which respects the following properties:

* the total length (sum of the lengths of the roads in the route) of the road is minimal;
* the road must visit nodes $X$ and $Y$.

# Task

Now, you are curious to calculate $\\sum_{1 \\leq u < v \\leq N} d(u, v)$. Since this number can be very large, only its remainder when divided by $10^9+9$ is required.

# Input data

The first line will contain the numbers $N$, $X$, $Y$ and $M$. The next $M$ lines will each contain three numbers $u$, $v$ and $c$, which signify that there is an edge between nodes $u$ and $v$ with weight $c$.

# Output data

Print a single number, the sum $d(u,v)$ for all unordered pairs $(u,v)$, modulo $10^9+9$.

# Constraints and clarifications

* $1 \\leq N , M \\leq 250 \\ 000$
* $1 \\leq X , Y \\leq N$
* $1 \\leq u, v \\leq N$
* $1 \\leq c \\leq 10^{9}$
* There are no loops or multiple edges in the input.

| # | Points | Constraints |
| - | ----- | ------------ |
| 1 | 12 | $1 \\leq N \\leq 100$, $1 \\leq M \\leq 200$ |
| 2 | 29 | $1 \\leq N \\leq 2 \\ 000$, $1 \\leq M \\leq 4 \\ 000$ |
| 3 | 59 | No additional constraints. |

# Example

`stdin`
```
3 2 1 3
1 2 1
3 1 1
3 2 3
```

`stdout`
```
6
```

## Explanation

$d(1, 2) + d(1, 3) + d(2, 3) = 1 + 3 + 2 = 6$