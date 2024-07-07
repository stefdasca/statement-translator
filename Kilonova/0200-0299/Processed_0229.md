Here is the translated text:

A connected graph with `N` nodes and `M` edges can be viewed as an hourglass with the center at node `X`, $1 \leq X \leq N$, if we can split all the nodes, except node `X`, into two non-empty subsets such that any path from a node in one subset to a node in the other subset passes through node `X`. You need to determine the number of distinct ways to view the graph as an hourglass for each of the `N` nodes chosen as the center, modulo `666013`. Two ways are considered distinct if the two associated subsets are different. The order of the subsets in a way is relevant, but the order of the nodes within a subset is not. For example, the solutions `({1,2,3}, {4,5})` and `({4,5}, {1,2,3})` are distinct, but the solutions `({4,5}, {1,2,3})` and `({4,5}, {1,3,2})` are not distinct.

# Input data
The input file `clepsidra.in` contains on the first line two natural numbers, `N` and `M`, representing the number of nodes and the number of edges in the graph, respectively. The next `M` lines will contain two natural numbers separated by a space, representing an edge.

# Output data
The output file `clepsidra.out` will contain `N` lines. The `i`-th line, $1 \leq i \leq N$, will contain the number of ways we can view the graph as an hourglass with the center at node `i`, modulo `666013`.

# Constraints and clarifications
* $2 \leq N \leq 200\ 002$
* $1 \leq M \leq 250\ 002$
* For `40%` of the tests, we have the constraints $2 \leq N \leq 1002$ and $1 \leq M \leq 1502$.
* **Attention!** The graph is connected.

# Example

`clepsidra.in`

```
6 7
4 3
1 3
5 4
4 1
3 2
1 5
5 6
```

`clepsidra.out`

```
0
0
2
0
2
0
```
Explanation
---

For the node with index `3`, the solutions are: `({2}, {1,4,5,6})` and `({1,4,5,6}, {2})`

For the node with index `5`, the solutions are: `({6}, {1,2,3,4})` and `({1,2,3,4},{6})