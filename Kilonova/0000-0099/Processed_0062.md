We call a *directed graph* a pair of sets, denoted by `G = (V, A)`, where `V` is a set of elements called vertices, and `A` is a collection of ordered pairs of elements from `V` called arcs. We call a *path* in a graph a sequence of vertices $x_1, x_2, ..., x_p$ with the property that for any `1 \leq i < p`, there exists an arc $(x_i, x_{i+1})$ in the graph. A directed graph is called *strongly connected* if for any vertices `x` and `y` in the graph, there exists at least one path from `x` to `y` and at least one path from `y` to `x`.

# Task
Write a program that successively reads the arcs of a directed graph with `N` vertices and checks after each arc read if the current partial graph (the graph formed from the `N` vertices and the arcs read up to that point) is or is not strongly connected.

# Interaction protocol
Your program will not read from or write to any file and will not implement the `main` function. Instead, it will implement the function

```cpp
int solve(int N, int M)
```
which will interact with the function `getEdge`, where `N` represents the number of vertices in the graph, and `M` represents the number of arcs in the graph. The interaction proceeds according to the protocol described below.

Initially, consider that the current partial graph has `N` vertices and `0` arcs. You can then call the function

```cpp
std::pair<int, int> getEdge()
```
to obtain the next arc. Once the obtained partial graph is strongly connected, `solve` should no longer call the `getEdge` function and should return `1`.

# Constraints and clarifications
* `1 \leq N \leq 10\ 000`
* `1 \leq M \leq 40\ 000`
* The problem has been adapted
* The "getedge.h" file must be included
* It is guaranteed that the given graph is strongly connected.
* The arcs are not necessarily distinct.

# Example of interaction
* We have `N = 4, M = 8`
* The partial graph is not strongly connected, the `getEdge()` function is called, and we obtain `1 2`
* The partial graph is not strongly connected, the `getEdge()` function is called, and we obtain `3 1`
* The partial graph is not strongly connected, the `getEdge()` function is called, and we obtain `2 4`
* The partial graph is not strongly connected, the `getEdge()` function is called, and we obtain `2 3`
* The partial graph is not strongly connected, the `getEdge()` function is called, and we obtain `4 3`
* The partial graph is strongly connected, `solve` returns `1