We call a multigraph $k$-complete of order $n$ a graph with $n$ nodes, labeled with $1, 2, \dots, n$ in which there exist exactly $k$ edges between any two different nodes. For example, the $2$-complete multigraph of order $3$ is shown in the figure below.

# Task

Given $n$ and $k$, determine the number of spanning trees of a $k$-complete multigraph of order $n$.

# Input data

The first line of the input file `multigraf.in` contains two positive natural numbers $n$ and $k$.

# Output data

The first line of the output file `multigraf.out` will contain a single natural number, representing the required number modulo 7919.

# Constraints and clarifications

* $1 \leq n, k \leq 15\ 000$;
* $20\%$ of tests have $k = 1$ and $n \leq 20$!
* $A$ modulo $x$ is $A\ \%\ x$.

# Example

`multigraf.in`
```
3 2
```

`multigraf.out`
```
12
```

## Explanation

The spanning trees for $n = 3$ and $k = 2$ are drawn in the figure below!

~[multigraf.png|align=center|width=90]