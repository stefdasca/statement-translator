Given is a directed graph with $N$ nodes (numbered from $1$ to $N$) and $M$ edges (numbered from $1$ to $M$). Each edge $i$ is directed from $a_i$ to $b_i$ and has a cost $c_i$ (positive, zero, or negative). A cycle is a sequence of distinct edges $mu(1), mu(2), \dots, mu(q)$ such that $b_{mu(i)}=a_{mu(i+1)} (1 \leq i \leq q-1)$ and $b_{mu(q)}=a_{mu(1)}$. The cost of a cycle is equal to the sum of the costs of the edges forming the cycle.

# Task

Knowing that there are no negative cost cycles in the graph, determine how many of the $M$ edges of the graph are part of at least one zero cost cycle.

# Input data

The first line of the input file `zeroc.in` contains the natural numbers $N$ and $M$, separated by a space. Each of the next $M$ lines contains three integers, $a_i$, $b_i$, and $c_i$, separated by spaces, having the meaning that there is an edge directed from node $a_i$ to node $b_i$, with cost $c_i$.

# Output data

In the output file `zeroc.out` you will print a single number, representing the number of edges of the graph that are part of at least one zero cost cycle.

# Constraints and clarifications

* $1 \leq N \leq 2\ 000$
* $0 \leq M \leq 15\ 000$
* The cost of an edge is an integer between $-10\ 000$ and $10\ 000$
* Multiple edges can exist between the same pair of nodes, possibly even in the same direction (and they can have different costs)

# Example

`zeroc.in`
```
6 8
1 2 -2
2 3 6
3 4 -2
4 1 -2
4 5 -7
5 2 7
5 6 3
6 1 8
```

`zeroc.out`
```
4
```

## Explanation

The only edges that are part of a zero cost cycle are the first $4$ edges in the file.