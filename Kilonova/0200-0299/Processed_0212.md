Here is the translated text:

---

An undirected graph is considered, initially having `N` isolated nodes numbered from `1` to `N` (thus the graph initially has `0` edges). On this graph, `4` types of operations can be performed, such as adding a new edge, deleting an edge, and two types of queries. However, there is a constraint: at any moment in time, the connected components of the graph must have the structure of a path (i.e., each node has at most `2` neighbors and the graph does not contain cycles). The `4` types of operations are as follows:
* Type `1`: Add an edge between nodes `i` and `j`. This operation is performed successfully if it does not violate the constraint. Otherwise, the operation will not be performed.
* Type `2`: Remove the edge between nodes `i` and `j`. This operation is performed successfully if there is an edge between nodes `i` and `j`.
* Type `3`: Determine all nodes at distance `D` from node `i`. The distance between two nodes is equal to the minimum number of edges of a path in the graph that connects the two nodes. Due to the constraint, there can be at most two nodes at distance `D` from another node.
* Type `4`: Determine the end nodes of the path (connected component) in which node `i` resides (`i` could be one of the ends or the only end if it is an isolated node).

# Task 
Given a sequence of `M` operations starting from a graph with no edges, display the result of each operation in sequence (in the order they are given).

# Input data
The input file `drumuri.in` contains:
* The first line contains the numbers `N` and `M` separated by a space.
* Each of the following `M` lines describes an operation, via a sequence of integers separated by spaces. The first number on the line represents the type of operation (from `1` to `4`).
* If the operation is of type `1`, then it is followed by two integers `i` and `j`, indicating that an edge will be added between nodes `i` and `j` in the graph (if it does not violate the constraint).
* If the operation is of type `2`, then it is followed by two integers `i` and `j`, meaning that the edge between nodes `i` and `j` in the graph will be removed (if it exists).
* If the operation is of type `3`, then it is followed by two integers `i` and `D`, indicating that the goal is to determine all nodes at distance exactly `D` from node `i`.
* If the operation is of type `4`, then it is followed by a single integer `i`, meaning that we want to determine the ends of the path in which node `i` resides.

# Output data
The output file `drumuri.out` will contain `M` lines. The `i`-th line will contain the result of the `i`-th operation from the input file. If the operation is of type `1` or `2`, its result will be `1` if the operation was performed successfully, or `0` otherwise. In the case of operations of type `3` and `4`, the result consists of a set of nodes. First print the number of nodes in the set, then, on the same line, the elements of the set in ascending order.

# Constraints and clarifications
* `1 \leq N \leq 40\ 000`
* `1 \leq M \leq 400\ 000`
* `0 \leq D \leq N-1`
* `1 \leq i, j \leq N`
* Edges will not be added from a node to itself.
* For `40\%` of the tests `N \leq 5000` and `M \leq 20\ 000`.

# Example

`drumuri.in`

```
6 14
1 2 4
1 6 5
4 1
1 1 5
1 1 6
4 5
3 6 1
4 4
4 3
3 3 1
3 3 0
2 3 2
2 5 6
3 6 1
```

`drumuri.out`

```
1
1
1 1
1
0
2 1 6
1 5
2 2 4
1 3
0
1 3
0
1
0
```

Explanations
---

The graph has `N=6` nodes and `M=14` operations are performed:
1) An edge is added between nodes `2` and `4` successfully.
2) An edge is added between nodes `6` and `5` successfully.
3) Node `1` is part of a path with a single node: `1`.
4) An edge is added between nodes `1` and `5` successfully.
5) Adding the edge between nodes `1` and `6` fails because it would form a cycle in the graph.
6) Node `5` is part of a path with `2` ends: `1` and `6`.
7) There is a single node at distance `1` from node `6`: node `5`.
8) Node `4` is part of a path with `2` ends: `2` and `4`.
9) Node `3` is part of a path with a single node: `3`.
10) There are zero nodes at distance `1` from node `3`.
11) There is a single node at distance `0` from node `3`: node `3`.
12) Deleting the edge between nodes `3` and `2` fails because this edge does not exist.
13) Deleting the edge between nodes `5` and `6` is performed successfully.
14) There are zero nodes at distance `1` from node `6`.

