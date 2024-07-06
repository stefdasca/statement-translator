A graph is called bipartite if the set of all its nodes can be divided into two disjoint subsets such that any edge has one endpoint in one subset and the other endpoint in the other subset. We call a graph a cycle if its nodes are labeled with distinct natural numbers, let's say $e_1, e_2, ..., e_k$ and we have exactly the edges: $e_1 - e_2, e_2 - e_3, ... , e_k - e_1$. Moreover, the labels follow the order $e_1 < e_2 < ... < e_k$. In other words, the cycle graph has all nodes and edges arranged to form a cycle. Several cycle graphs are given, and it is required to form a bipartite graph using them while respecting the following rules:

* If the first cycle graph has $x$ nodes and the second has $y$ nodes, the labels of the nodes of the first graph are considered from $1$ to $x$ and those of the second graph are considered from $x + 1$ to $x + y$. The labeling of the nodes of the following given cycle graphs is done similarly, using consecutive numbers continuing with the first available label from the previous graph.
* The bipartite graph must be formed from the given cycle graphs, considering them in the order of input.
* The current cycle graph is added to the previously formed graph by overlapping one of its edges with an edge of the last grafted cycle graph. During overlapping, we have the following two options: the new edge (formed from the two overlapping ones) is either retained further or eliminated.
* We further explain the way of overlapping of two edges. Consider edge $m_1$ labeled $v_1 - v_2$ and edge $m_2$ labeled $v_3 - v_4$. We assume $v_1 < v_2 < v_3 < v_4$. Node $v_2$ will overlap with node $v_4$ and node $v_1$ with node $v_3$. The new nodes will further have the labels $v_1$ and $v_2$. In short, the nodes with the larger label from $m_1$ and $m_2$ will overlap (and the label that remains is the smaller of the two) and similarly for the other two.
* When adding the new cycle graph, the following method will be applied: from it, choose the edge formed with the two maximum labels. Choose an edge that belongs to the previously added cycle graph; if there are several options, choose the edge containing the node with the maximum label at that moment and among the two that contain that label, choose the one with the higher value for the other label.

# Input data
The first line of the input file will contain a number $n$ representing the number of given cycle graphs. The second line contains $n$ numbers representing, in order, the number of nodes of each cycle graph.

# Output data
The first line of the output file will contain $m$, representing the minimum number of overlapping edges that need to be eliminated to obtain a bipartite graph. The second and third lines respectively contain the labels of the component nodes of the two subsets describing the bipartite graph, separated by spaces and in ascending order on the same line. The first of the two lines contains the label $1$ (it is observed that during the period of the applications of additions, in the set of remaining labels, not necessarily all numbers from $1$ to $n$ are found, but the number $1$ will remain). If the problem has no solution, the output will contain only the number $\text{-}1$.

# Constraints
* $1 \leq n \leq 1 \ 000$
* The given cycle graphs may have between $3$ and $100$ nodes
* If the resulting edge from the current cycle graph addition is not eliminated, it cannot be used for another later addition.

## Subtask 1 (10 points)
* $n = 1$.
## Subtask 2 (15 points)
* All cycle graphs have $3$ nodes.
## Subtask 3 (15 points)
* All cycle graphs have $4$ nodes.
## Subtask 4 (60 points)
* No other constraints.

# Example
`stdin`
```
3
3 3 4
```
`stdout`
```
1
1 4 8
2 3 7
```

Explanation
---

* According to the explanations in the statement, the given cycle graphs in the above example are initially labeled as follows:
~[1.jpg]
* We start with the first cycle graph and join the second to it. The overlapped edge will be eliminated.
~[2.jpg]
* Now add the third cycle graph and we need to make the overlap as in the drawing below. This time we decide not to eliminate the edge.
~[3.jpg]
* The resulting graph is:
~[4.jpg]
* We notice it more easily as a bipartite graph by visualizing it like this:
~[5.jpg]