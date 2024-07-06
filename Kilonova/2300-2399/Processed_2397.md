```markdown
# Statement

There is a tree with $N$ nodes numbered from $1$ to $N$, out of which $K$ are leaves (nodes with degree $1$). The leaves are numbered from $1$ to $K$.

Other information about this tree is not known, but fortunately, you can ask questions of the type "*what is the distance from leaf $x$ to leaf $y$?*". The distance between two nodes in the tree is equal to the number of edges on the elementary path connecting the two nodes.

# Task

Determine the tree by asking at most $12\ 000$ questions.

# Interaction Protocol

Your program will not read or write any file. Instead, you will need to implement the function
```cpp
std::vector<int> solve(int K);
```
which receives as a parameter the number of leaves $K$ and returns the parent array of the tree (it does not matter which node is considered the root). To determine the tree, you can call the function
```cpp
int query(int x, int y);
```
where $x$ and $y$ are distinct integer numbers between $1$ and $K$, and the function returns the distance between nodes $x$ and $y$.

# Example 
* The jury calls `solve(3)`.
* The participant calls `query(1, 2)` which returns `3`.
* The participant calls `query(2, 3)` which returns `3`.
* The participant calls `query(1, 3)` which returns `2`.
* The function `solve` returns `{4, 5, 4, 0, 4}`.

# Constraints and clarifications

* $3 \leq K \leq 3\ 000$;
* The number of nodes in the resultant tree will not exceed $10\ 000$.
* If the program does not comply with the established interaction, it will receive $0$ points for the respective test.
* You need to include `copac.h`
```