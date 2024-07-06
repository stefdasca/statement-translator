**Sile learned the definition of a bipartite graph during his math class. We consider an undirected graph $G$ consisting of a set of nodes $V$ and a set of edges $E$. We say that $G$ is bipartite if and only if there exist two subsets $V^1, V^2 \\subseteq V$ such that:**
- $V^1 \\cap V^2 = \\varnothing$;
- $V^1 \\cup V^2 = V$;
- each edge in $E$ has one endpoint in $V^1$ and the other endpoint in $V^2$.

**Sile came across an undirected graph $G$, with nodes $V$ and edges $E$, consisting of $N$ nodes ($V = \\{1, 2, \\dots, N\\}$) and $M$ edges ($|E| = M$). He now wonders for which nodes $v \\in V$ the graph $G \\setminus v$ obtained by removing node $v$ and its incident edges from $G$ is bipartite.**

**You need to help Sile solve the problem for $T$ scenarios.**

# Interaction Protocol
The contestant has to implement the following function, which will be called for $T$ independent scenarios:
```cpp
void solve(int N, int M, int* X, int* Y, char* S);
```
$N$ represents the number of nodes in the graph, $$M$$ represents the number of edges in the graph. $X$ and $Y$ are two arrays of length $M$ that encode the set of edges of the graph: for every $0 \\leq i < M$ there is an edge between $X_i$ and $Y_i$. The contestant has to write the answer in the array $S$ of length $N$: for $0 \\leq i < N$ we have $S_i =$ `1` if the graph $G \\setminus \\{i+1\\}$ is bipartite, and $S_i =$ `0` otherwise. **The values written in $S$ are characters, not numbers**.

# Constraints
- There will be no edges with $a = b$.
- There will be no duplicate edges within the same scenario.
- Edges $(a, b)$ and $(b, a)$ are considered identical.

## Subtask 1 (23 points)
- $1 \\leq T \\leq 600$
- $1 \\leq N \\leq 2\\ 000$
- $1 \\leq M \\leq 5\\ 000$
- The sum of all values $N$ will not exceed $20\\ 000$.
- The sum of all values $M$ will not exceed $20\\ 000$.

## Subtask 2 (32 points)
- $1 \\leq T \\leq 20\\ 000$
- $1 \\leq N \\leq 100\\ 000$
- $1 \\leq M \\leq 250\\ 000$
- The sum of all values $N$ will not exceed $120\\ 000$.
- The sum of all values $M$ will not exceed $350\\ 000$.
- **Full points will be awarded to any solution that correctly finds the answer at least for nodes $v \\in V$ which have at most two incident edges in $G$.** However, it is required that $S_i$ values are always `0` or `1` for $0 \\leq i < N$.

## Subtask 3 (22 points)
- $1 \\leq T \\leq 20\\ 000$
- $1 \\leq N \\leq 100\\ 000$
- $1 \\leq M \\leq 250\\ 000$
- The sum of all values $N$ will not exceed $120\\ 000$.
- The sum of all values $M$ will not exceed $350\\ 000$.

## Subtask 4 (23 points)
- $1 \\leq T \\leq 40\\ 000$
- $1 \\leq N \\leq 1\\ 000\\ 000$
- $1 \\leq M \\leq 2\\ 500\\ 000$
- The sum of all values $N$ will not exceed $1\\ 000\\ 000$.
- The sum of all values $M$ will not exceed $2\\ 500\\ 000$.

# Example
| Commission Calls | Effect |
-|-
| `solve(4, 3, {1,1,2}, {2,3,3}, S)` | $S =$ `1110` |
| `solve(6, 7, {1,1,2,2,4,4,5}, {2,3,3,4,5,6,6}, S)` | $S =$ `000000` |

# Explanation
We have $T = 2$ scenarios to solve.
\\
In the first scenario, the graph $G$ is the one in the image below.

~[1.png]

We observe that nodes $1$, $2$, and $3$ are pairwise neighbors, from which we deduce that graph $G$ is not bipartite. By removing any of the nodes $1$, $2$, or $3$, the resulting graph will be bipartite. For example, if we remove node $2$ (and thus its incident edges $2 \text{ – } 1$ and $2 \text{ – } 3$), then the resulting graph $G \\setminus \\{2\\}$ will be bipartite because we can choose the subsets $V^1 = \\{1, 4\\}$ and $V^2 = \\{3\\}$ to satisfy the properties in the statement (note that there are other ways to choose the subsets $V^1$, $V^2$). Removing node $4$ would not lead to a bipartite graph. Therefore, the answer for this scenario is `1110`.
\\
In the second scenario, the graph $G$ is the one in the image below.

~[2.png]

In this case, regardless of which node $v \\in V$ is removed from $G$, the resulting graph $G \\setminus \\{v\\}$ would not be bipartite. Therefore, the answer in this case is `000000`.