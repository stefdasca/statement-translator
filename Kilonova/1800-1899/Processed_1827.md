~[divine.jpg|align=right]

*Stich wants to map the Hawaiian archipelago using his ship's scanner. The archipelago consists of $N$ islands, numbered with natural numbers from $0$ to $N - 1$, and $M$ bridges connecting two islands. On the last mission, the scanner malfunctioned, so it can only process the following type of command: Stich selects a set of islands, and the scanner tells him the maximum number of islands among the selected ones that can be visited starting from an island in the set, using only existing bridges and never leaving the set during the traversal. Help Stich map the archipelago, using the scanner a relatively small number of times!*

More formally, an undirected graph $G$ with $N$ nodes and $M$ edges is given. In a query, the contestant will select a subset of nodes from $G$ and find out the maximum number of nodes in a connected component of the subgraph formed by the nodes of the subset and the edges between them. The task is to find the graph $G$ in a relatively small number of queries. **Attention! Initially, the contestant only knows the value of $N$, not $M$!**

# Interaction Protocol

**The problem is interactive**. The contestant will implement the function solve with the following signature:
```cpp
void solve (int N, int subtask_id);
```
The parameter $N$ represents the number of nodes in $G$. The parameter $subtask\\_id$ represents the index of the subtask on which the contestant's source is running (an integer between $1$ and $7$, inclusive).

The contestant can use the functions `query` and `answer` with the following signatures:
```cpp
int query (const std::vector<int>& nodes);
void answer (const std::vector<std::pair<int, int>>& ans);
```

The `query` function represents an inquiry. The parameter `nodes` contains the indices of the nodes the query is made on. The function returns the size of the largest connected component as specified in the statement. The nodes may be in any order in `nodes`.
    
The `answer` function will be called only once by the contestant, after they have found the edges of the graph $G$. The parameter $ans$ contains the edges found by the contestant, in any order. The order of nodes within each edge does not matter.
**The contestant WILL NOT implement a `main` function**.

# Constraints
Let $Q$ be the number of queries made by the contestant and $R = \frac{Q}{M}$.
* $N = 512$.
* $N - 1 \leq M \leq 8192$.

## Subtask 1 (3 points)
* $G$ is a path.
* If $R \leq 35$, the subtask will receive full points.

## Subtask 2 (1 point)
* $G$ is a star graph.
* The scoring is the same as in the previous subtask.

## Subtask 3 (30 points)
* $G$ is a tree.
* All nodes in $G$ have a degree of at most $3$.
* If $R \leq 15$, the subtask will receive full points.
* If $15 < R \leq 25$, the subtask will receive $(115 - R)\%$ of the points.
* If $25 < R \leq 35$, the subtask will receive $(190 - 4R)\%$ of the points.
* If $35 < R$ and $Q \leq 130\ 816$, the subtask will receive 1 point.

## Subtask 4 (30 points)
* $G$ is a tree.
* The scoring is the same as in the previous subtask.

## Subtask 5 (3 points)
* $G$ is a cycle.
* The scoring is the same as in the previous subtask.

## Subtask 6 (16 points)
* All nodes in $G$ have a degree of at most $10$.
* If $R \leq 11$, the subtask will receive full points.
* If $11 < R \leq 12$, the subtask will receive $75\%$ of the points.
* If $12 < R \leq 13$, the subtask will receive $50\%$ of the points.
* If $13 < R \leq 25$, the subtask will receive $25\%$ of the points.

## Subtask 7 (17 points)
* There are no additional constraints.
* The scoring is the same as in the previous subtask.

# Examples
Committee: $N = 3, subtask\\_id = 1$
Contestant: Query: $\{0, 1, 2\}$
Committee: $3$
Contestant: Query: $\{0, 1\}$
Committee: $2$
Contestant: Query: $\{2, 0\}$
Committee: $2$
Contestant: Query: $\{1, 2\}$
Committee: $1$
Contestant: Answer: $\{(0,1), (0,2)\}$
