```markdown
Albinuța `D` has `N` favorite flowers and a unique way of collecting their pollen. She has crafted a map of the flowers in the form of a directed graph with `N` nodes and `M` edges, where the flowers are the graph's nodes and are numbered `1,2,...,N`. For each node, the adjacency list sorted based on the bee's preferences is known.

The path followed by the bee to collect pollen starts at node `1` at time `T=1`. At every moment of time `T`, the bee opts for the `T`-th node in the adjacency list, counting `T` positions circularly starting with the first node in the list. She will arrive at node `T+1` at the chosen node. For example, if at time `T=12`, the current node's adjacency list, sorted according to the bee's preferences, is: `1 6 2 9 5`, then at time `T=13` the bee will arrive at node `6`.

A beekeeper discovered the map used by the bee and wonders in which flower the bee will be at specific times $T_i$ (`1\leq i \leq Q`).

# Task
Write a program to determine for each given moment of time $T_i$ the flower on which the bee will be located.

# Input data
The input file `albinuta.in` will contain on the first line two natural numbers `N` and `Q`, separated by a single space. Each line `k`, among the next `N` lines, contains the natural number $L_k$, representing the number of nodes adjacent to node `k`, followed by $L_k$ natural numbers representing its adjacency list, sorted according to the bee's preferences. The numbers in the `N` lines are separated by a space. The next `Q` lines will contain, in order, the numbers $T_1, T_2,... ,T_Q$, one per line.

# Output data
The output file `albinuta.out` will contain `Q` lines. Each line `i` will contain the number of the node where the bee will be at time $T_i$.

# Constraints and clarifications
* $M = L_1 + L_2 +...+L_N$
* `1 \leq N, M, Q \leq 50`
* $1 \leq L_k \leq M$, `1\leq k \leq N`
* $1 \leq T_i \leq 10^9$, `1\leq i \leq Q`
* In an adjacency list, a node can appear multiple times.
* A node can appear in its own adjacency list.
* For `30%` of tests, $1 \leq T_i \leq 10^6$

# Example

`albinuta.in`
```
6 5
2 2 1
2 1 3
3 4 5 6
1 5
1 6
1 1
1
2
3
4
5
```

`albinuta.out`
```
1
2
3
6
1
```

Explanation
---

The bee will follow the path: `1 2 3 6 1` at the moments of time `1,2,3,4,5`.
```