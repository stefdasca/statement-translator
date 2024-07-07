> "The wheel of fortune... when you're up or when you're down, fate is always changing, like the rankings from the day before yesterday." — A great ancient Japanese thinker.

~[roata.png|align=right]

An undirected tree with $N$ nodes, numbered from $1$ to $N$, is given. The root of the tree is fixed at node $1$. Each node $u$ has a value $a_u$, which is a natural number. Because we don’t like trees, we can reduce the tree to a single node by applying the following operation $N - 1$ times:

* Choose any two distinct nodes connected by an edge, $u$ and $v$
* Add the value $|a_u - a_v |$ to the counter $S$. The initial value of the counter $S$ is $0$;
* The two nodes are united. By uniting, we mean deleting both nodes from the tree and creating a new node $w$, for which $a_w = \min(a_u, a_v)$.

All edges incident with $u$ and $v$ will change their endpoint equal to $u$ or $v$ into $w$, except for the edge $(u, v)$, which disappears.

The total cost of the $N - 1$ operations is the value of $S$ after performing them.

# Task

There are $Q$ queries of the type:
* `1 u x`: The value of node $u$ becomes equal to $x`
* `2 u`: The minimum total cost of a valid sequence of operations that reduces the subtree of node $u$ to a single node is required. We remind you that the root of the tree is fixed at node $1$.

# Input Data

The first line of the input contains a natural number $N$, representing the number of nodes in the tree.

The second line contains $N$ natural numbers, the $i$-th number representing the value $a_i$ associated with node $i$ in the tree, where $i$ is a number from $1$ to $N$.

The third line contains $N - 1$ natural numbers, the $i$-th number representing the parent of node $i + 1$ in the tree, where $i$ is a number from $1$ to $N - 1$ (node $1$ does not have a parent, being the root of the tree).

The fourth line contains a natural number $Q$, representing the number of queries. On the next $Q$ lines are the queries in the format described in the statement, one per line.

# Output Data

The output must contain one answer per line corresponding to each type $2$ query, in the order in which they were given.

# Constraints and Clarifications

* $1 \leq N \leq 200\ 000$
* $1 \leq Q \leq 200\ 000$
* $1 \leq a_i \leq 10^9$ for $1 \leq i \leq N$
* $1 \leq x \leq 10^9$ for each type $1$ query.

| # | Points | Constraints          |
| - | ------- | ------------------- |
| 1 | 4      | $1 \leq N \leq 1\ 000, Q = 1$ |
| 2 | 13      | $Q = 1$      |
| 3 | 15      | The tree is a chain and all queries are of type $2$.     |
| 4 | 24      | All queries are of type $2$.     |
| 5 | 12      | The parent of node $i$ is node $1$ for $2 \leq i \leq N$.     |
| 6 | 32     | No additional constraints.      |

# Example 1

`stdin`
```
7
4 7 9 7 4 1 2
1 1 3 2 3 2
1
2 1
```

`stdout`
```
11
```

# Example 2

`stdin`
```
7
6 6 5 1 6 6 4
1 1 2 3 3 3
3
2 1
1 1 1
2 1
```

`stdout`
```
7
11
