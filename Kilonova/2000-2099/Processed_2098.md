> I say that a man should be satisfied with his poverty because, if it's a matter, it is not wealth, but the peace of your shed that makes you happy.
— The joke is that, it's like The Lucky Mill, it's like, a high school joke, I don't know if you get it.
Ioan Slavici, Great Classic

# Task

Egor, affected by the gloomy winter weather, chooses to spend his time with a creative activity to improve his mood — painting. Thus, he decided to go outside and admire nature. Walking through Cismigiu, he noticed one of the most special trees he had ever seen: an informatic tree.

The tree has $N$ nodes, and each branch (edge) of this tree has a specific color, making his job as an artist much more complicated.

Egor likes symmetry very much, that is why he decided to emphasize in his painting a path$^1$ in which all the colors of the edges in the path appear an even number of times$^2$. However, he is often undecided; before choosing the path he will emphasize, he would like to know the number of paths that would meet the aforementioned criterion. Help him find this number!

# Input data

The first line will contain a single integer $T$ — the number of different scenarios.

Each scenario will be described as follows: 
- the first line will contain an integer $N$ — the number of nodes in the tree; 
- the next $N-1$ lines will describe the tree. The $i$-th line will contain 3 integers $u_i, v_i, c_i$, representing an edge from $u_i$ to $v_i$ of color $c_i$. 

# Output data

There will be $T$ lines. The $i$-th line will contain a single integer, representing the answer for the $i$-th scenario.

# Constraints and clarifications

 - $^1$: A path in a tree that connects two nodes $x$ and $y$ is a minimal length sequence of edges that links node $x$ to node $y$.
 - $^2$: A color is considered to appear an even number of times in a path if its frequency in the set of edge colors that make up the path is even;
 - $1 \leq T \leq 200\ 000$;
 - The sum of $N$ values for all scenarios (denoted below as $S_N$) does not exceed $200\ 000$; 
 - $1 \leq c_i \leq N$;
 - $1 \leq u_i, v_i \leq N, u_i \neq v_i$ and there does not exist $i, j$ such that $u_i = u_j$ and $v_i = v_j$ (or vice versa);
 - It is guaranteed that the tree is connected;
 - It is recommended to calculate the answer using 64-bit data types.

# Subtasks

| # | Points | Constraints |
| - | - | -------- |
| 0 | 0 | Example |
| 1 | 9 | $1 \leq S_N \leq 200$ and $u_i = i, v_i = i+1$ (the tree is a path) |
| 2 | 10 | $1 \leq S_N \leq 200$ |
| 3 | 13 | $1 \leq S_N \leq 2\ 000$ and $u_i = i, v_i = i+1$ (the tree is a path) |
| 4 | 14 | $1 \leq S_N \leq 2\ 000$ |
| 5 | 23 | $1 \leq c_i \leq 50$ |
| 6 | 31 | Without additional constraints |

# Example 1

`stdin`
```
2
8
1 5 7
8 1 1
8 6 1
2 7 4
1 4 7
1 2 4
1 3 7
16
2 8 14
1 16 6
3 4 7
15 7 16
6 15 14
1 11 6
15 3 1
8 9 16
3 10 14
11 14 12
8 1 14
9 6 16
9 12 9
5 13 9
3 5 1
```

`stdout`
```
6
8
