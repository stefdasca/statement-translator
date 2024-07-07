After having visited so many cities, the tourist decided he will become a tour guide. He knows $n$ cities with $m$ undirected roads between them.

He plans to organize a circuit which starts in some city of his choice and for every subsequent city, the city has to be reachable from the current city using some of the roads. His circuit may contain the same city more than once, even in a row. For example, for the city below

~[Tourism.jpg]

He may choose the circuit $1 − 4 − 4 − 2$ (to get from $1$ to $4$ he traverses two direct roads, stays twice at $4$ and traverses two direct roads again to get to $2$) or $5 − 6 − 6 − 5$. The circuit $1 − 5$ is not a good one because there is no path between cities $1$ and $5$.

He wonders for circuits of different lengths how many distinct such circuits exist that he can choose from. Precisely for lengths from $1$ to $q$ you must answer for each the number of possible circuits. Since the answer may be too large you are required to compute it modulo $10^9 + 7$.

# Task

# Input data

The first line will contain three numbers, $n$, $m$ and $q$ ($1 \leq n \leq 10^5$), ($1 \leq m \leq 2 \cdot 10^5$), ($1 \leq q \leq 10^5$). The following $m$ lines contain the description of the graph.

For tests worth $20$ points it is guaranteed that $(1 \leq n \leq 100)$ and $(1 \leq q \leq 100)$.

# Output data

The output will contain on the first line $q$ integers, the number of circuits of length $1, 2, ..., q$.

# Example

`stdin`
```
6 5 2
1 2
1 3
2 3
3 4
5 6
```

`stdout`
```
6 20
