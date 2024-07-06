# Task

You are given a tree with $N$ nodes. Each node has values assigned to it, $value[i]$. You must calculate the sum cost of every pair nodes $(u, v)$, where $gcd(value[u], value[v]) > 1$ and $u \ne v$. For a pair of nodes $(u, v)$, we define the cost of that path to be the sum of value of all nodes that lie inside the $(u, v)$ path.

# Input

The first line of the input will contain $N$ ($1 \leq N \leq 100 \ 000$), the number of nodes. The second line will contain $N$ numbers, the $i^{th}$ number, representing the $value[i]$ ($1 \leq value[i] \leq 30 \ 000$). Each of the next $N - 1$ lines will contain a pair of nodes $(u, v)$, each representing an edge of the tree.

# Constraints and clarifications
* For tests worth $20$ points ($ 1 \leq N \leq 1 \ 000 $)
* For tests worth $20$ more points, $value[i] = value[1]$ for $i = 1, 2,...n$

# Output

The output will contain the sum of costs over all pairs of nodes $(u, v)$, such that $gcd(value[u], value[v]) > 1$

# Example

`stdin`
```
5
2 7 14 22 77
1 2
1 3
2 4
4 5
```

`stdout`
```
442
``` 