During the geography class, our friend Bobby receives a tricky problem from his colleague, Fischer. Being totally out of ideas and not wanting to disappoint Fischer, he asks for your help. Fischer's tricky problem is the following.

# Task

Given a sequence of values representing the costs of $M$ bidirectional edges, construct a connected graph using only these edges so that the cost of its maximum cost minimum spanning tree is maximized.

# Input data

The first line of the input file `bobby.in` contains two integers, $N$ and $M$, representing the number of nodes and respectively the number of edges that the constructed graph should have. The second line contains six integers, $X$, $Y$, $A$, $B$, $C$ and $D$, which will generate the sequence of $M$ values, noted as $V$, using the following rules:
* $\\displaystyle V_1 = X$;
* $\\displaystyle V_2 = Y$;
* $\\displaystyle V_i = (A \cdot V_{i-2} + B \cdot V_{i-1} + C)\text{ mod }D$, for any $i$ with $3 \leq i \leq M$.

# Output data

The first line of the output file `bobby.out` will contain a single integer, the cost of the maximum cost minimum spanning tree of the constructed graph, or $-1$ if it's not possible to construct a graph that respects the task.

# Constraints and clarifications

* $2 \leq N, M \leq 1\ \\000\ \\000$;
* $0 \leq X, Y, A, B, C, D \leq 1\ \\000\ \\000\ \\000$, $D \neq 0$;
* Between any two nodes in the constructed graph there should be at most one edge.

# Example

`bobby.in`
```
4 5
1 1 1 1 1 3
```

`bobby.out`
```
1
```

## Explanation

The sequence of $M$ edges is: $1\ \\1\ \\0\ \\2\ \\0$.
We construct the graph as follows:
* Between nodes $1$ and $2$, an edge of cost $2$.
* Between nodes $1$ and $3$, an edge of cost $0$.
* Between nodes $1$ and $4$, an edge of cost $0$.
* Between nodes $2$ and $3$, an edge of cost $1$.
* Between nodes $3$ and $4$, an edge of cost $1$.