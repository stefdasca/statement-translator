
# Task

You are given a tree (a connected graph with $N$ nodes and $N-1$ edges) with $N$ nodes that have costs on the edges. Two sequences of length $N$, $st$ and $dr$, are also provided. You are required to choose some edges from the $N-1$ edges such that each node $i$ has between $le_i$ and $ri_i$ $\textbf{chosen}$ adjacent edges and the sum of the costs of the chosen edges is minimal. If it is not possible to choose any edges such that the conditions for each node are met, $-1$ will be displayed.

# Input data

The first line of the input file `arbore.in` contains a number $N$.  
The second line contains $N$ numbers, with the $i$-th of them being $le_i$.  
The third line contains $N$ numbers, with the $i$-th of them being $ri_i$.  
The following $N-1$ lines contain three numbers $a_i$, $b_i$, $c_i$, representing an edge with cost $c_i$ between nodes $a_i$ and $b_i$.

# Output data

The first line of the output file `arbore.out` will contain a single integer, the minimal cost of choosing some edges or -1 if they cannot be chosen.

# Constraints and clarifications

* $1 \leq N \leq 100\ 000$
* $0 \leq le_i \leq ri_i \leq N$
* $0 \leq c_i \leq 10^9$
* $cnt_i$ is the number of edges connected to node $i$

| # | Points | Constraints |
| - | - | ------------|
|0|0|Example.|
|1|10|$1 \leq N \leq 17$|
|2|20|$cnt_i \leq 10$|
|3|70|No additional constraints.|

# Example

`arbore.in`
```
5
1 1 1 1 0
1 2 5 1 4
1 2 1
1 3 1
2 4 2
2 5 3
```

`arbore.out`
```
3
```

## Explanation

A correct solution is to choose the first and third edges, which have costs 1 and 2, respectively, $1 + 2 = 3$.
