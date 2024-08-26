## Task

We are given $N$ points with real coordinates in the plane. Some pairs of points are connected by an edge (a straight line segment). It is guaranteed that two such edges do not intersect (except possibly at a vertex). This system of points and edges forms a planar graph. Find a circulation in this graph such that for any edge, the value of the flow is an integer between $1$ and $5$. We define circulation as an orientation of edges accompanied by the assignment of a quantity of flow to each edge. A circulation is considered valid if for each node in the graph, the inflow equals the outflow. It is guaranteed that such a circulation exists for each graph in the test files.

## Input data

The input file `nowhere-zero.in` will contain on the first line $2$ natural numbers $N$ and $M$. The next $N$ lines will each contain $2$ real values with at most $6$ decimal places representing the coordinates of the $i$-th point. The following $M$ lines will contain $2$ distinct numbers between $1$ and $N$ indicating that there is an edge between the points with those indices.

## Output data

The output file `nowhere-zero.out` will contain $M$ lines, one for each edge in the input. Each line should be of the form $x$ $y$ $z$, $1 \leq z \leq 5$ with the meaning that $z$ units of flow are sent from point $x$ to point $y$ through the edge $(x, y)$ in that direction.

## Constraints and clarifications

$1 \leq N \leq 100\ 000$  
$-1\ 000\ 000\ 000 \leq X[i], Y[i] \leq 1\ 000\ 000\ 000$

## Example

`nowhere-zero.in`  
```
4 5
0 1.5
2 2
2 0
3 1
1 2
1 3
2 3
2 4
3 4
```

`nowhere-zero.out`  
```
2 3 2
3 1 1
1 2 1
4 2 1
4 3 1
```