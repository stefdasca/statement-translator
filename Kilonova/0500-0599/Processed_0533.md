*Ranuto has a training program over several days in which he wants to learn a new technique: "11th Gate Super Convincing Chakra Dual-Core Rasengan." For objective reasons, he wants to know in advance what his training might consist of on a specific day (Kasura comes to watch him).*\

Given a tree with $N$ nodes, numbered from $1$ to $N$. The tree is rooted at node $1$.

We want to traverse the tree starting from the root. For each node, we can consider its children in any desired order.

There are two types of tasks, represented by a number $C$:
- For $C = 1$, the traversal will be a **depth-first (DFS) pre-order**;
- For $C = 2$, the traversal will be a **breadth-first (BFS)**.

\

The pseudocode for the traversals can be found below:
\
**Algorithm 1** Depth-first (DFS) pre-order traversal
- *p* $\\leftarrow$ empty list (will contain nodes from the traversal)
- **procedure** DFS(*tree*, *node*):
  - **add** *node* at the back of *p*
  - **for each** child *x* of *node*:
    - DFS(*tree*, *x*)
- DFS(*tree*, 1)

\
**Algorithm 2** Breadth-first (BFS) traversal
- *p* $\\leftarrow$ empty list (will contain nodes from the traversal)
- **procedure** BFS(*tree*):
  - q $\\leftarrow$ empty queue
  - **add** node 1 at the back of *q*
  - **while** *q* is not empty:
    - *f* $\\leftarrow$ node at the front of *q*
    - **remove** *f* from the front of *q*
    - **add** *f* at the back of *p*
    - **for each** child *x* of *f*:
      - **add** node *x* at the back of *q*
- BFS(*tree*)

# Task
Which nodes in the tree can be at position $K$ in any of the possible traversals?

# Input data
The first line contains three numbers, $C$, $N$, and $K$. The next $N - 1$ lines contain $2$ numbers each, $A$ and $B$, indicating the existence of an edge in the tree between nodes $A$ and $B$.

# Output data
Print on one line, with a space between them, in ascending order, all the nodes that can be at position $K$ in any traversal of the type specified by $C$. The number of nodes should not be printed.

# Constraints and clarifications
- $1 \\leq N \\leq 10\ 000$
- $1 \\leq K \\leq N$

|# | Points | Constraints|
| - | - | ------------|
|1|5|$C = 1$, $N \\leq 10$|
|2|5|$C = 2$, $N \\leq 10$|
|3|5|$C = 1$. The tree is completely binary, with $N$ of the form $2^p - 1$, $p$ a non-zero natural number|
|4|5|$C = 2$. The tree is completely binary, with $N$ of the form $2^p - 1$, $p$ a non-zero natural number|
|5|20|$C = 1$, $N \\leq 500$|
|6|20|$C = 2$, $N \\leq 500$|
|7|15|$C = 1$, $N \\leq 3\ 500$|
|8|10|$C = 2$, $N \\leq 5\ 000$|
|9|15|$C = 1$, $N \\leq 10\ 000$|

# Example 1
`keidei.in`
```
1 8 5
1 2
1 3
1 4
2 5
2 6
3 7
5 8
```
`keidei.out`
```
2 5 6 8
```
## Explanation

For the first example: Because we can consider the children of any node in the tree in any order we want, we can assume that our depth-first traversal visits the children of a node from left to right after establishing the order.
\
~[1.png] Figure 1: If we rearrange the given tree to look like the figure above, the traversal will produce the following result: $1, 3, 7, 4, {\\bf 2}, 5, 8, 6$.
\
~[2.png] Figure 2: Here, the traversal will be $1, 3, 7, 2, {\\bf 5}, 8, 6, 4$.
\
~[3.png] Figure 3: Here, the traversal will be $1, 3, 7, 2, {\\bf 6}, 5, 8, 4$.
\
~[4.png] Figure 4: Here, the traversal will be $1, 4, 2, 5, {\\bf 8}, 6, 3, 7$.
\
We can verify any other arrangement to guarantee that any other node besides $2, 5, 6, 8$ cannot be at the 5th position in a pre-order depth-first traversal.

# Example 2
`keidei.in`
```
1 17 15
1 2
1 3
1 4
2 5
3 6
3 7
4 8
5 9
5 10
8 11
8 12
8 13
8 14
9 15
10 16
10 17
```
`keidei.out`
```
3 10 11 12 13 14 16 17
```

# Example 3
`keidei.in`
```
2 8 5
1 2
1 3
2 4
2 5
2 7
2 8
3 6
```
`keidei.out`
```
4 5 7 8
```

## Explanation
For the third example, we can observe that no matter how we arrange the tree, the first $3$ nodes in the traversal will be either $1, 2, 3$ or $1, 3, 2$. If $2$ comes before $3$ in the traversal, then $6$ will definitely be the last node in the traversal. If $3$ comes before $2$, then $6$ will definitely be in the fourth position in the traversal. Thus, the only nodes that can be at the 5th position are $4, 5, 7, 8$.