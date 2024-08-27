# Weight Graph

## Task

The holidays are approaching and you need to buy gifts! We are given an undirected connected graph with $N$ nodes and $M$ edges. You are located at node $1$ and you want to collect $K$ gifts. We define a valid path as a path that starts from node $1$, contains an arbitrary number of nodes, and does not contain $2$ consecutive identical edges. The cost of such a path is the product of the values of the edges that form the path. The total number of gifts you will obtain is equal to the sum of the costs of all valid paths in this graph (which can also be infinite). Thus, you need to assign a cost greater than or equal to $0$ to each edge such that the total number of gifts you will obtain is exactly $K$, and among all these possible assignments, you must display an assignment that has the edge with the maximum cost as minimal as possible (the edge with the maximum cost needs to be minimized).

## Input data

The input file `weightgraph.in` contains on the first line $N$, $M$, and $K$. The following $M$ lines each contain $2$ numbers, $X_i$ and $Y_i$, indicating that there is an edge from node $X_i$ to node $Y_i$.

## Output data

The output file `weightgraph.out` will contain $M$ numbers, each on a new line, such that the number on the $i^{th}$ line represents the cost associated with the edge between nodes $X_i$ and $Y_i$ from the input file.

## Constraints and clarifications

$2 \leq N \leq 100000$

$1 \leq M \leq 200000$

$1 \leq K \leq N - 1$

$0 \leq$ cost of an edge $\leq 10^9$

For 20% of the points, the graph will have the form of a chain.

For another 20% of the points, $N \leq 1000$ and $M \leq 2000$.

For another 60% of the points, initial constraints apply.

There will not be more than one edge between any two nodes, nor edges from a node to itself.

If there are multiple solutions, you can display any of them.

It can be shown that, under these conditions, a solution always exists.

## Example

`weightgraph.in` 
```
5 4 4
2 3
2 4
1 2
5 1
```
`weightgraph.out`
```
1
1
1
1
```

`weightgraph.in` 
```
5 6 3
5 3
5 4
4 2
4 3
3 1
2 1
```
`weightgraph.out`
```
1
0
0
1
0
1
```

## Explanation

For the first example, the valid paths are: $1 \rightarrow 2$, $1 \rightarrow 2 \rightarrow 3$, $1 \rightarrow 2 \rightarrow 4$, $1 \rightarrow 5$. All of these have a cost of $1$, and the total cost will be $4$. We could have assigned the edge $(1, 2)$ a cost of $4$ and the rest of the edges a cost of $0$, but the edge with the maximum cost (cost $4$) is not minimal possible (the edge with the maximum cost is $1$ in the assignment above).