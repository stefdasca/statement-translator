Cătălin, after playing enough at his grandparents' place, came back home, but he didn't come empty-handed; he brought with him the most beautiful tree he had in the game ["TreeGCD"](https://kilonova.ro/problems/11), drawn on a piece of paper. At home, his younger brother found this sheet and thought of trying his hand at drawing. He wants to transform the tree into a graph in the following way: each edge from the initial tree becomes a node in the new graph, two nodes in the new graph are connected by an edge if and only if the two corresponding edges in the initial tree have a common node.

After constructing this graph, he threw away the paper with the initial tree. When he returned from school, Cătălin, seeing what had happened, was not very happy. Fortunately, he found out that you can reconstruct the initial tree if you are given the graph.

# Task
The number of nodes `N`, the number of edges `M`, and the `M` edges of the graph are given. Reconstruct the initial tree.
It is possible that Cătălin's brother drew the graph incorrectly and there may not be an associated tree.

# Input data
In the input file `linegraph.in`, the first line contains a number `T`, which represents the number of tests in the file. For each test, the first line contains two natural numbers `N` and `M` separated by space with the meanings from the description, and on the next `M` lines, there are two numbers separated by space, representing the nodes that have an edge between them.

# Output data
In the output file `linegraph.out`, the first line should contain the word `NU`, if there is no associated tree for the given graph, or the word `DA`, if there is an associated tree, and in this case on the next line, a number `E`, representing the number of nodes in the tree, and on the next `E-1` lines will be displayed two numbers representing the pairs of nodes in the tree that have an edge between them.

# Constraints and clarifications
* `1 \ \leq \ T \ \leq \ 10000`;
* `1 \ \leq \ N \ \leq \ 1000`;
* $0 \ \leq \ M \ \leq \ \frac{N(N-1)}{2}$ 
* The sum of the squares of all `N` in the input file does not exceed `1000000`;
* For tests worth `15` points, it is guaranteed that there is a solution and that the tree from which the graph was constructed either has a chain shape, or it has `N-1` leaves;
* For other tests worth `55` points, it is guaranteed that `N \leq 100` and the sum of the squares of all N in the input file does not exceed `10000`;
* If there are multiple solutions, any of them can be displayed;
* The tree in the output file with `E` nodes will have the nodes numbered `1,2,...,E`;
* The actual numbering of nodes in the output file is not important – any solution that renumbers the nodes will be considered a correct response.

# Example

`linegraph.in`

```
2
5 7
3 2
3 5
3 1
2 5
2 1
1 5
1 4
3 1
1 2
```

`linegraph.out`

```
DA
6
1 2
1 3
3 4
3 5
3 6
NU
```

Explanations
---
In the input file, we have a graph. Each edge of this graph corresponds to a node in the tree from the output file. Thus: the edge `(1,3)` becomes node `1`, the edge `(1,2)` becomes node `4`, the edge `(3,4)` becomes node `3`, the edge `(3,5)` becomes node `2`, and the edge `(3,6)` becomes node `5`. 
The edges `(1,3), (3,4), (3,5), (3,6)` all have the common node `3`, so their corresponding nodes in the graph `(1,3,2,5)` all have edges between them.

In the second test, node `3` is isolated and the graph cannot come from any tree.