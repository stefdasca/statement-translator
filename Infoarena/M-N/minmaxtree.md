## Task

Tanaka recently solved a classic problem: given a tree with $N$ vertices and values on the edges, he found the maximum or minimum value on $K$ paths in the tree. Interestingly, all these results were distinct! Unfortunately, the initial values were lost. Given Tanaka's results and the original tree structure, can you find a plausible assignment of values for all edges? If you can, Groot will fall in love with the created tree, and you will receive 100 points.

## Input data

The first line of the input file `minmaxtree.in` will contain the number $N$.

The next $N - 1$ lines will contain pairs of numbers $x$ $y$, with $1 \leq x, y \leq N$, which signify that the tree has an edge from node $x$ to node $y$. The tree nodes are indexed from $1$ to $N$.

The next line of the input will contain the number $K$.

The next $K$ lines will contain a description of Tanaka's results, one result per line. A result signifying that the maximum on the path from $x$ to $y$ was $z$ will be represented by $M$ $x$ $y$ $z$, and one signifying that the minimum on the path from $x$ to $y$ was $z$ will be represented by $m$ $x$ $y$ $z$.

It is guaranteed that the given edges form a tree, and that all values $z$ are distinct.

## Output data

The output file `minmaxtree.out` will contain $N - 1$ lines. Each line will contain three numbers $x$ $y$ $v$ indicating that in your value assignment, there exists an edge from $x$ to $y$ with weight $v$. These edges should match the edges from the input file, ignoring the order of the edges. Furthermore, the order of $x$ and $y$ within an edge does not matter. This assignment should lead to the described results. It is guaranteed that there exists a value assignment that leads to the described results.

## Constraints and clarifications

$1 \leq N \leq 70000$

$1 \leq K \leq 70000$

$1 \leq z \leq 1000000000$

For 7 points, $N \leq 1000$ and $z \leq 1000$.

For another 22 points, Tanaka only found maxima.

For another 29 points, any two paths for which Tanaka found maxima do not intersect.

Also, any two paths for which Tanaka found minima do not intersect.

## Example

`minmaxtree.in`

```
4
1 2
2 3
3 4
3
M 1 2 1
m 1 4 0
M 2 3 100
```

`minmaxtree.out`

```
3 2 100
1 2 1
4 3 0
```