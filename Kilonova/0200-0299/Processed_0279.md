## Task
Given `G`, a **directed acyclic** graph without edge weights. In this problem, we will analyze what happens if we use depth-first search to calculate the minimum path length between node `1` and node `N`. More precisely, we will run the algorithm described by the following pseudocode:

```
visited[x] = 0, for any x
dist[1] = 0 

DFS(node):
	visited[node] = 1
	for all neighbors v in the adjacency list of node:
		if visited[v] is 0:
			dist[v] = dist[node] + 1
			DFS(v)

DFS(1)
print dist[N]
```

The formation of the graph's adjacency lists follows the following pseudocode (where `list[x]` represents the list of neighbors of `x`):

```
list[x] = [], for any x

read n, m

for i from 1 to m:
	read a, b
	add b to the end of list[a]
```

Of course, this algorithm is not always correct, because the computed distance depends on the order in which a node's neighbors are processed during reading.

For example, if during the construction of the graph the edge `(1 → 2)` is read first and then the edge `(1 → 3)`, then when the neighbors of `1` are processed, the first neighbor will be `2`, and the second will be `3`. Thus, the distance computed with the first algorithm above may differ, depending on the order in which the edges are added during reading.

Therefore, for a given graph, we are curious to know for how many of the `M!` permutations of its edges, the `DFS` algorithm will yield the minimum distance.

## Input data
The input file `shuffle.in` will contain two natural numbers `N`, the number of nodes, and `M`, the number of edges on the first line. On the next `M` lines, there will be two numbers `x` and `y`, representing the directed edge from `x` to `y` in the graph.

## Output data
The output file `shuffle.out` will contain a single number on the first line, which represents the number of acceptable permutations modulo `1 000 000 007`.

## Constraints and clarifications
* $1 \leq N \leq 100\ 000$
* $1 \leq M \leq 200\ 000$
* **The tests are not from the competition** 
* It is guaranteed that an edge will not appear twice in the input file.
* It is guaranteed that each edge belongs to at least one path from `1` to `N`.

### Subtask 1 (10 points)
* $N, M \leq 10$

### Subtask 2 (15 points)
* $N \leq 20, M \leq 60$

### Subtask 3 (35 points)
* $N \leq 1400, M \leq 4000$

### Subtask 4 (40 points)
* $1 \leq N \leq 100\ 000$, $1 \leq M \leq 200\ 000$

## Examples
`shuffle.in`
```
3 3
1 2
1 3
2 3
```

`shuffle.out`
```
3
```

### Explanation

The three permutations for which the minimum distance is obtained are:
`(1→3)` `(1→2)` `(2→3)`
`(1→3)` `(2→3)` `(1→2)`
`(2→3)` `(1→3)` `(1→2)`

`shuffle.in`
```
4 5
1 2
1 3
2 3
2 4
3 4
```

`shuffle.out`
```
90
```

### Explanation

The minimum distance from `1` to `4` is `2`, and there are `90` permutations of the `5` edges that give this minimum distance.

`shuffle.in`
```
7 11
2 4
3 2
1 3
2 6
6 7
4 5
4 6
6 5
5 7
2 5
3 4
```

`shuffle.out`
```
24948000
```

### Explanation

The minimum distance is calculated for the example provided.

