
The wizard Roxanne, after numerous hours of researching ancient mysteries, decided to go to the café to relax. When she arrived at the old café, she saw a strange structure on the wall called a _tree_. Formally, a _tree_ is a collection of $N$ vertices numbered with consecutive natural numbers, where vertex $0$ is the root, and all other vertices have a unique parent (vertex $v$ has the parent $p_v$). Since the café is run by wizards and programmers, the tree is drawn with the root at the top.

The wizard, intrigued by this structure, decides to pour magical coffee into one of the vertices. If the coffee is poured into vertex $u$, then it spreads in the subtree rooted at vertex $u$. Since it's magical coffee, it doesn't flow randomly but occupies the _longest path_ it can occupy, in the subtree rooted at vertex $u$, **when passing through the node $u**. The amount of coffee lost when it flows is proportional to the length of the path the coffee occupies. Roxanne notes this quantity as $r_u$. Remember that the edges of the tree can have different lengths.

# Task

Roxanne is interested in the amount of coffee she might lose if she pours it into all the vertices of the tree, which is the sum of the values $r_u$ from all vertices $u$ of the tree. This is not hard to calculate initially, but the programmers decide to challenge her and **increase** the length of certain edges $Q$ times. Can you help Roxanne find the total length of all the paths occupied by coffee, if the coffee is poured into all the vertices, initially and after each of the $Q$ modifications? Attention! You need to provide answers **modulo** $10^9 + 7$.

# Input data

The first line contains a single integer $N$, the number of vertices.

The second line contains $N - 1$ integers: $p_1, p_2, \dots, p_{N-1}$, where $p_v$ is the parent of the node $v$, while node $0$ is the root.

The third line contains $N - 1$ integers: $d_1, d_2, \dots, d_{N-1}$, where $d_v$ is the length of the edge between vertex $v$ and $p_v$.

The fourth line contains $Q$, the number of increments.

Each of the next $Q$ lines contains two integers $v_i$ and $add_i$, representing the $i^{th}$ modification: the length of the edge between vertices $v_i$ and $p_{v_i}$ increases by $add_i$.

# Output data

Print $Q+1$ lines: on line $i+1$, display the answer after the $i^{th}$ modification. On the first line, display the answer before any modification.

All answers must be printed **modulo** $10^9 + 7$.

# Constraints and clarifications

* $1 \leq N \leq 100 \ 000$
* $1 \leq Q \leq 100 \ 000$
* $1 \leq d_i \leq 100 \ 000 \ 000$ for any $1 \leq i \leq N - 1$
* $0 \leq p_i \leq i$
* $1 \leq add_i \leq 10^9$ for any $1 \leq i \leq Q$

| # | Score | Constraints            |
| - | ------ | ------------------- |
| 1 | 11     | $1 \leq N, Q \leq 1 \ 000$ |
| 2 | 13     | The height of the tree is at most $50$.      |
| 3 | 31     | $d_i = 100 \ 000 \ 000$ for any $1 \leq i \leq N - 1, \ add_i = 1$ for any $1 \leq i \leq Q$   |
| 4 | 45     | No additional constraints.    |

# Example

`stdin`
```
5
0 0 1 1
0 0 0 0
10
1 2
2 2
3 2
4 2
4 1
3 1
2 1
1 1
4 1000
2 1000
```

`stdout`
```
0
2
4
8
10
12
13
14
15
2015
3015
```
