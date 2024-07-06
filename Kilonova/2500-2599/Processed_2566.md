```markdown
Given a tree with $N$ nodes and root at node $1$. Each node $i$ is associated with a number $a_i$. For a tree $T$ and a node $u$, let $v_1, v_2, \dots, v_k$, $v_1 = 1$, $v_k = u$ be the path from the root to node $u$ in tree $T$. For this node $u$, we define the longest strictly increasing subsequence up to $u$ in tree $T$ as any of the longest strictly increasing subsequences from the sequence of numbers: $a_{v_1}, a_{v_2}, \dots, a_{v_k}$.

There are $q$ queries. For the $i$-th query, there are $k_i$ distinct numbers, $u_1, \dots, u_{k_i}$, which represent nodes in the initial tree $T$. Let the tree $T'$, the connected component that contains the root, result from removing the nodes $u_1, \dots, u_{k_i}$ from tree $T$. For the $i$-th query, we need to find the largest length of the longest strictly increasing subsequence up to any node $v$ in $T'$.

# Task

Determine, for each query, the largest length of the longest strictly increasing subsequence up to any node $v$, in the tree $T'$ associated with the query $i$.

# Input data

The input file `arbsub.in` contains on the first line the number of nodes $N$, and the number of queries, $q$. 

The next line contains the $N$ natural numbers, $a_i$, $a_i$ being associated with node $i$. 

The next $N - 1$ lines contain 2 numbers each, $u_i$ and $v_i$, representing the tree edges.

The next $q$ lines contain the information of each query. On line $N + 1 + i$, the number $k$, followed by $k$ numbers: $u_1, \dots, u_k$, with the significance given in the statement. It is guaranteed that the nodes are distinct, do not contain the tree root, and are integers in the interval $[2, N]$. Note that $k$ can be $0$.

# Output data

The output file `arbsub.out` will contain $q$ lines, with line $i$ containing the answer for the $i$-th query.

# Constraints and clarifications

* $1 \leq N \leq 3 \cdot 10^5$
* $1 \leq a_i \leq 10^9$
* $1 \leq q \leq 3 \cdot 10^5$
* $ \sum{}{} k_i \leq 5 \cdot 10^5$

|#|Score|Constraints|
|-|-|--------|
|1|13|$N \leq 100$, $q \leq 100$|
|2|18|$N \leq 5 \ 000$, $q \leq 5 \ 000$|
|3|31|$N \leq 10^5$, $q \leq 200$, $1 \leq a_i \leq 200$|
|4|38|No additional constraints|

# Example

`arbsub.in`
```
12 4
2 3 3 4 6 3 5 3 5 7 7 8
6 4
7 4
4 8
1 2
2 4
5 2
10 12
5 10
11 9
9 5
3 1
3 5 6 8
4 9 11 12 10
4 2 4 10 12
0
```

`arbsub.out`
```
4
4
2
5
```
```