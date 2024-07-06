*We all know what a sieve is; we can use one to separate the coarse flour from the fine flour. However, in this problem, we will try to sieve the nodes of a tree.*

Nadgob the Siever has a tree (a connected, undirected, acyclic graph) with $N$ nodes. Nadgob wants to choose a subset $S$ of the tree's nodes. To make this choice, he will sit, one by one, in $K$ **distinct** nodes of the tree. Once seated in a node $x$ of the tree, he can, as many times as he wants, choose a node $y$ and "sieve" (i.e., add to $S$) all nodes $z$ for which $y$ lies on the shortest path between $x$ and $z$. Of course, a node that is already in $S$ will not be added again.

Nadgob finds himself in a state of existential confusion. Full of anxiety, he wonders in how many ways he can choose the subset $S$ according to the preceding procedure (modulo $10^9 + 7$). Two ways are considered distinct if the resulting subsets are distinct.

# Interaction Protocol
The contestant will implement the function `solve` with the following signature:
```cpp
int solve (int N, std::vector<int> p, std::vector<int> q, std::vector<int> r);
```
The parameters of this function have the following meaning:
* $N$ - the number of nodes in the tree;
* $p, q$ - arrays of length $N - 1$ containing the endpoints of the tree's edges (more precisely, there is a bidirectional edge between nodes $p[i]$ and $q[i]$, for any $0 \le i < N$);
* $r$ - an array of length $K$ containing the nodes where Nadgob will sit, in order.

The function will return the result as required in the problem statement. **The contestant will NOT implement a `main` function**.

# Constraints
* $1 \le K \le N \le 10^5$
## Subtask 1 (4 points)
* $1 \le N \le K \le 20$
## Subtask 2 (7 points)
* $1 \le N \le 20$
## Subtask 3 (5 points)
* The tree contains at most one node with a degree greater than $1$.
## Subtask 4 (6 points)
* The tree contains no nodes with a degree greater than $2$.
## Subtask 5 (7 points)
* $K = 1$
## Subtask 6 (7 points)
* $K = N$
## Subtask 7 (20 points)
* $K = 2$
## Subtask 8 (21 points)
* $1 \le N \le 10^3$
## Subtask 9 (23 points)
* Initial constraints.

# Examples
`Input`
```
3 1
0 1
0 2
0
```
`Output`
```
5
```

`Input`
```
7 4
0 1
0 2
3 0
4 2
3 6
3 5
4 3 1 2
```
`Output`
```
39
```

Explanations
---

For the first example:
~[wbtree.jpg] 
Nadgob is seated in node $0$.
* Selecting no $y$, results in $S = \emptyset$.
* Selecting $y = 0$, results in $S = \{0, 1, 2\}$.
* Selecting $y = 1$, results in $S = \{1\}$.
* Selecting $y = 2$, results in $S = \{2\}$.
* Selecting $y = 1$ and $y = 2$, results in $S = \{1, 2\}$.

For the second example:
~[wbtree1.jpg]