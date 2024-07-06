```markdown
A **directed** graph with $n$ nodes and $m$ edges is given. Each edge has a cost of $1$ (it can be traversed in one minute). Two "friends" (cousins) start from node $S$. One of them wants to reach node $A$, and the other one wants to reach node $B$.

The two friends will walk together until they cycle, meaning until they reach the same node a second time, denoted by $Z$. After cycling, they can continue their paths separately. However, if they want, they can continue together on the same path: only the obligation to walk together disappears.

Each of them must finish their journey only after cycling, meaning only after they are no longer obligated to walk together. However, it is okay if one of their paths ends exactly at the node where they cycled (i.e., they cycle at $A$ or $B$).

What is the minimum number of minutes needed so that both can reach their destinations, on the allocated time, in $A$ and $B$, respectively?

In other words, if the two cousins cycle for the first time after exactly $t$ minutes, then continue their paths for another $t_A$ and $t_B$ minutes, respectively, we want to find the minimum value of $max(t + t_A, t + t_B)$.

There are two types of tasks, represented by a number $c$:
- If $c = 1$, the minimum value of $max(t + t_A, t + t_B)$ must be calculated.
- If $c = 2$, a triplet of paths that can be followed by the two cousins must be displayed (the common path from $S$ to $Z$, path followed later by the first cousin from $Z$ to $A$, path followed later by the second cousin from $Z$ to $B$), such that the value associated with the paths, i.e., $max(t + t_A, t + t_B)$, is minimal. Any correct triplet with the associated minimum value can be displayed.

# Input data
The first line contains $c$. The second line contains two integers $n$ and $m$. The third line contains three integers $S$, $A$, and $B$.

The next $m$ lines contain two integers $X$ and $Y$, representing that there is a directed edge from node $X$ to node $Y$, which can be traversed in one minute (cost $1$).

# Output data
If $c = 1$, print a single number, the minimum value of $max(t + t_A, t + t_B)$.

If $c = 2$, print three paths. The first path is from $S$ to $Z$. The second path is from $Z$ to $A$. The third path is from $Z$ to $B$, where $S$, $A$, $B$, $Z$ are defined above.

Each path will be printed on two separate lines:
- The first line will contain the length of the path, i.e., the number of edges.
- The second line will contain the nodes of the path, separated by a space.

The value associated with the paths, i.e., $max(t + t_A, t + t_B)$, must be minimal.

# Constraints and clarifications
- $1 \leq S, A, B, Z \leq n \leq 5000$
- The nodes are numbered from $1$ to $n$.
- $A \neq B$
- $1 \leq m \leq n \times (n-1)$.
- It is guaranteed that for any given test there is at least one solution.
- There are no edges from a node to itself. There is at most one directed edge between any two distinct nodes.
- If the cousins separate at $A$, the first cousin may not take any further steps (his subsequent path would have $0$ edges and would only contain $A$; see example 3). Similarly for $B$.
- For each subtask, tests with $c = 1$ will account for $60\%$ of the score.
- For 30 points, $n \leq 500$, $m = n$ and all edges are of the form $i \rightarrow (i\ mod\ n) + 1$, where $i \in \{1, ..., n\}$.
- For 50 points, $n \leq 500$.
- For 20 points, $n \leq 5000$ and $m \leq 4 \times n$.

# Example 1
`veri.in`
```
2
7 8
1 3 4
1 2
2 5
5 7
7 6
6 7
6 5
5 3
7 4
```
`veri.out`
```
5
1 2 5 7 6 5
1
5 3
2
5 7 4
```
~[1.png|width=45%]
The path followed in common by the two is $1 \rightarrow 2 \rightarrow 5 \rightarrow 7 \rightarrow 6 \rightarrow 5$. The path followed subsequently by the first cousin is $5 \rightarrow 3$. The path continued by the second cousin is $5 \rightarrow 7 \rightarrow 4$. Thus, the first cousin needs $6$ minutes to reach $A$, while the second needs $7$ minutes to reach $B$, so the answer for $c = 1$ is $7$. The two could have cycled at $7$, if they had followed the path $1 \rightarrow 2 \rightarrow 5 \rightarrow 7 \rightarrow 6 \rightarrow 7$. However, although the second cousin would have reached $B$ in just $6$ minutes ($7 \rightarrow 4$), the first cousin would have needed at least $8$ minutes to reach $A$ ($7 \rightarrow 6 \rightarrow 5 \rightarrow 3$).

# Example 2
`veri.in`
```
2
7 8
1 2 5
1 3
1 4
3 2
4 5
6 4
7 3
3 6
4 7
```
`veri.out`
```
5
1 4 7 3 6 4
3
4 7 3 2
1
4 5
```
~[2.png|width=45%]
The correct answer for $c = 1$ is $8$. For this example, there are two correct solutions. The second solution is the triplet of paths $(1 \rightarrow 3 \rightarrow 6 \rightarrow 4 \rightarrow 7 \rightarrow 3,\\ 3 \rightarrow 2,\\ 3 \rightarrow 6 \rightarrow 4 \rightarrow 5)$.

# Example 3
`veri.in`
```
2
5 6
1 3 5
1 2
2 3
3 4
4 3
3 1
3 5
```
`veri.out`
```
4
1 2 3 4 3
0
3
1
3 5
```
~[3.png|width=25%]
The correct answer for $c = 1$ is $5$. A cycle ending in $A = 3$ is used.

# Example 4
`veri.in`
```
1
4 4
1 2 4
1 3
3 2
2 3
2 4
```
`veri.out`
```
5
```
~[4.png|width=45%]
For $c = 2$, the only correct triplet of paths is $(1 \rightarrow 3 \rightarrow 2 \rightarrow 3,\\ 3 \rightarrow 2,\\ 3 \rightarrow 2 \rightarrow 4)$.

**Attention!** The triplet $(1 \rightarrow 3 \rightarrow 2 \rightarrow 3 \rightarrow 2,\\ 2,\\ 2 \rightarrow 4)$ is incorrect, as the first visited node for the second time is not $2$.
```