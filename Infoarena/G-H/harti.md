## Task

Lorena, Miruna's little sister, recently learned at the computer science club that any map can be colored using a maximum of four colors. Since the girl was not convinced without a demonstration, she spent the last two weeks trying to find a counterexample. Finally, tired of so much work without results, she decided to be content with demonstrating the property on a much more specific case. Thus, the following problem was born: Given a graph with nodes of the form $(x_i, y_i)$ where any two edges intersect only, possibly, at one of the ends. Any edge $u-v$ satisfies one of the following conditions: $x_v = x_u$, $y_v = y_u$, $|x_v - x_u| = |y_v - y_u|$. Find a coloring of the nodes of the graph, using a maximum of $K$ colors, so that there are no two nodes with the same color connected by an edge.

## Input data

The input file `harti.in` will have the following format:
$N$ $M$ $K$ $x_1$ $y_1$ $x_2$ $y_2$ $\dots$ $x_N$ $y_N$ $u_1$ $v_1$ $\dots$ $u_M$ $v_M$. The first line contains three numbers, $N$, $M$, and $K$, representing the number of nodes, the number of edges, and the number of available colors, respectively. The nodes are numbered from 1 to $N$. The next $N$ lines contain two numbers each, $x_i$ and $y_i$, representing the coordinates of node $i$. The next $M$ lines contain two numbers each, $u_i$ and $v_i$, indicating that there is an edge between nodes $u_i$ and $v_i$.

## Output data

The output file `harti.out` will contain $N$ lines. Each line contains a number between 1 and $K$, indicating the color of node $i$.

## Constraints

1 $\leq N \leq 2000$

1 $\leq M \leq 5000$

0 $\leq x_i$, $y_i \leq 1000$, for any 1 $\leq i \leq N$

1 $\leq u_i$, $v_i \leq N$, for any 1 $\leq i \leq M$

$u_i \ne v_i$, for any 1 $\leq i \leq M$

Nodes are distinct in pairs

Edges are distinct in pairs (no duplicate edges)

There is no edge from a node to itself

It is guaranteed that there exists a solution

## Constraints and clarifications

1 10 points $K = 9$

2 15 points $K = 6$

3 25 points $K = 5$

4 50 points $K = 4$

## Example

`harti.in`
```
5 8 4
0 2
2 2
0 0
1 1
2 0
1 2
1 3
1 4
2 5
3 4
3 5
4 5
1 2
2 3
1 6
```
`harti.out`
```
1
2
3
4
```