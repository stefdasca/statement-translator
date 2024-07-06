A **directed acyclic graph** (DAG) is a directed graph with no cycles.

Let `G` be a simple directed acyclic graph (that is, it does not contain multiple edges between the same nodes or edges from a node to itself) in which the nodes are labeled with the first `N` natural numbers.

A topological sort of the nodes of a directed acyclic graph `G` is an ordering of the nodes such that, if there is an arc `(i, j) ∈ G`, then `i` appears before `j` in this ordering. Such an ordering can be represented as a permutation `P` of the labels of the nodes of the graph `G`.

Among all the topological sorts of a graph, the minimum lexicographical topological sort is the topological sort whose permutation is lexicographically smaller than the permutation of any other topological sort.

A permutation $a_1, a_2, ..., a_N$ is lexicographically smaller than another permutation $b_1, b_2, ..., b_N$ if there exists an integer `S` less than or equal to `N` such that: $a_1 = b_1, a_2 = b_2, ..., a_{S−1} = b_{S−1}$, and $a_S < b_S$.

# Task
Given a permutation `P` of length `N`. How many directed acyclic graphs labeled with the first `N` natural numbers have the property that `P` is their minimum lexicographical topological sort?

# Input data
The file `dag.in` contains the number `N` on the first line. The second line contains `N` distinct numbers with values between `1` and `N` representing the permutation `P`.

# Output data
The file `dag.out` must contain a single number representing the number of directed acyclic graphs of `N` nodes for which `P` is their minimum lexicographical topological sort. Since this value can be very large, you are required to print only the remainder modulo `1 000 000 007` of this value.

# Constraints and clarifications
* `2 \leq N \leq 200 000`
* For tests worth `10` points, `N \leq 6`
* For other tests worth `55` points, `N \leq 2 500`

# Examples
`dag.in`
```
3
3 1 2
```
`dag.out`
```
3
```

Explanations
---
In the first example, there are `3` simple directed acyclic graphs with `3` nodes whose minimum lexicographical topological sort is $P_1 = 3, P_2 = 1, P_3 = 2$.
\\
~[image.png]
\\
`dag.in`
```
10
1 2 3 5 4 6 7 8 10 9
```
`dag.out`
```
92960636
```

