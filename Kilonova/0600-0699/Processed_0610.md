# Task

Given a tree with $N$ nodes, each node having a communicating vessel with infinite capacity, respond to $Q$ queries of the form $(u, v, h)$ with the following meaning: We consider the path from $u$ to $v$ and pour $h$ liters of water into node $u$. Through this process, the values on the path from $u$ to $v$ will be (starting with $u$) $h, h-1, \ldots, 1, 0, 0, \ldots, 0$. The value in a node that is not on the path from $u$ to $v$ is the value found in the closest node that is on the path from $u$ to $v$. For each query, the sum of the values in the tree is required.

# Input data

The first line contains the numbers $N$ and $Q$. The next $N-1$ lines each contain a pair of numbers $(u, v)$ indicating that there is an edge between nodes $u$ and $v$. The following $Q$ lines each contain three numbers, $(u, v, h)$, representing a query element.

# Output data

The output file will contain $Q$ lines, the $i$-th line representing the answer for the $i$-th query.

# Constraints and clarifications

* $1 \leq N, Q \leq 200\ 000$
* $1 \leq u, v \leq N$
* $1 \leq h \leq 10^9$

## Subtask 1 (8 points)
* $1 \leq N, Q \leq 1\ 000$

## Subtask 2 (6 points)
* All queries have the same $u$

## Subtask 3 (12 points)
* All queries have the same $v$

## Subtask 4 (53 points)
* $1 \leq N \leq 50\ 000$

## Subtask 5 (21 points)
* No other constraints

# Example
`stdin`
```
10 3
1 2
2 3
3 4
3 5
3 6
4 7
4 8
6 9
6 10
7 10 5
7 10 3
1 10 8
```
`stdout`
```
30
11
59
```

Explanation
---
For the first query, node $7$ is the only one with $5$ liters of water, nodes $4$ and $8$ contain $4$ liters of water, nodes $5$, $3$, $2$, and $1$ contain $3$ liters of water, nodes $6$ and $9$ contain $2$ liters of water, and node $10$ contains one liter of water.