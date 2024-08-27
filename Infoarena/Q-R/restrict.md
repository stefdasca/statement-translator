## Constraints

An input tree with $N$ nodes labeled from $1$ to $N$ is given, with the root at node $1$. Each edge has an associated cost. To reach a node $D$ from node $1$, the chain between node $1$ and node $D$ is isolated from the rest of the tree. Then, this chain is traversed from node $1$, moving along the edges up or down, respecting the restrictions imposed on the nodes, until node $D$ is reached. A restriction on a node $X$ is defined as another node $Y$ (an ancestor of $X$), meaning we cannot enter node $X$ if node $Y$ is among the last $K$ nodes visited. The traversal cost includes the cost of each edge traversed. The objective is to determine, for each node $i$, $1 \leq i \leq N$, the minimum cost to reach node $i$ from node $1$, respecting the node restrictions. Additionally, if an edge has been traversed $H$ times in the minimum cost path from the root to a node $X$, then this edge must be traversed at least $H$ times in the minimum cost path from the root to any direct or indirect child of node $X$.

## Input data

The input file `restrict.in` contains the following:
The first line contains two integers $N$ and $K$, as described in the problem statement.  
The next $N-1$ lines each contain 3 integers. The $i$-th line among these $N-1$ lines contains the following 3 values:
- The first number represents the parent of node $i+1$.
- The second number represents the cost of the edge between node $i+1$ and its parent.
- The third number represents the restriction on node $i+1$. This value is $-1$ if there is no restriction on node $i+1$.

## Output data

The output file `restrict.out` should contain $N$ lines, each containing a single value. The $i$-th value represents the minimum cost to reach node $i$ from the root, or $-1$ if it is not possible to reach that node.

## Constraints and clarifications

$0 \leq N, K \leq 100\ 000$  
$0 \leq$ edge cost $\leq 1\ 000\ 000$

For tests worth 10 points, it is guaranteed that:
- $1 \leq N \leq 1\ 000$
- The tree is a chain (each node has at most one child)
- Restrictions do not intersect (if node $X$ has a restriction on node $Y$, then all nodes between $X$ and $Y$ have no restrictions).

For other tests worth 30 points, it is guaranteed that $1 \leq N \leq 1\ 000$.

The problem will be evaluated on tests worth 90 points.

## Examples will represent tests worth 10 points "by default."

## Example

`restrict.in`  
```
6 3
3 2 -1
1 1 -1
1 8 -1
2 3 1
4 1 0
```

`restrict.out`  
```
3
1
8
10
-1
```

## Explanation

For the first example, we have the following tree:

To reach node $1$ from the root, no movement is needed, so the minimum cost is $0$.

To reach node $2$ from the root with a minimum cost, follow the path: $1 \rightarrow 3 \rightarrow 2$, with a cost of $1 + 2 = 3$.

To reach node $3$ from the root with a minimum cost, follow the path: $1 \rightarrow 3$, with a cost of $1$.

To reach node $4$ from the root with a minimum cost, follow the path: $1 \rightarrow 4$, with a cost of $8$.

To reach node $5$ from the root with a minimum cost, follow the path: $1 \rightarrow 3 \rightarrow 2 \rightarrow 3 \rightarrow 2 \rightarrow 5$, with a cost of $1 + 2 + 2 + 2 + 3 = 10$. The restriction on node $5$ disallows entering this node if node $1$ is among the last 3 nodes visited. Thus, after reaching node $2$, go back to node $3$ and then go down to node $5$. Thus, the last 3 nodes visited before entering node $5$ are $2, 3, 2$.

Node $6$ cannot be reached from the root because the restriction on node $6$ disallows entering this node if node $1$ is among the last 3 nodes visited. The minimum cost for this node is $-1$.

In the third example, node $6$ can be reached while respecting the restrictions on the nodes, with a cost of $16$. However, this implies not traversing edge $(2,3)$ at least 3 times (the edge was traversed 3 times to reach node $5$, and node $6$ is a direct child of node $5$).