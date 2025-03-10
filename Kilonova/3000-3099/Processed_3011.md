File Contents:
Let $N, K, P$ be three non-zero natural numbers. We will consider all directed graphs that have $N$ vertices and $K$ arcs, represented by the list of their arcs ordered lexicographically.
We will then sort the graphs lexicographically and number them starting from $1$.

# Task

Write a program that, given $N$, $K$, and $P$, solves the following two tasks:
1. Determine $NR$, the number of directed graphs with $N$ vertices and $K$ arcs.
2. Determine the directed graph with $N$ vertices and $K$ arcs having the order number $P$. 

# Input data

The input file `nkgraf.in` contains on the first line the task that needs to be solved ($1$ or $2$). The second line contains three natural numbers separated by a space $N \\ K \\ P$, having the significance stated in the problem.

# Output data

If the task is $1$, the output file `nkgraf.out` will contain a single line where $NR$, the number of directed graphs with $N$ vertices and $K$ arcs, will be written.
If the task is $2$, the output file `nkgraf.out` will contain $K$ lines where the $K$ arcs of the graph having the order number $P$ will be written in lexicographical order, one arc per line; for each arc, two vertices separated by a space will be written, representing the initial and the final endpoint of the arc, respectively.

# Constraints and clarifications

* $2 \leq N \leq 30$
* $1 \leq P \leq \min (NR, 10^{6})$
* Every arc in the graph will have the initial endpoint different from the final endpoint.
* For tests worth $30$ points the task is $1$ and $N \leq 8$.
* For tests worth $30$ points the task is $1$ and $8 < N \leq 30$.
* For tests worth $30$ points the task is $2$.
* $10$ points are awarded by default.

# Example 1

`nkgraf.in`
```
1
3 2 6
```

`nkgraf.out`
```
15
```

# Example 2

`nkgraf.in`
```
2
3 2 6
```

`nkgraf.out`
```
1 3
2 1
```

## Explanations

There are $15$ graphs with $3$ vertices and two arcs. In lexicographical order they are:

~[graphs.png]