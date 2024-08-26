## Task

You are given $3$ non-zero natural numbers: $K$, $N$, and $M$. You need to construct an undirected graph with $K$ nodes, having the following properties:
The number of connected components of the graph is $N$.
The number of connected components of the complement of the graph is $M$.

## Input data

The input file `grafc.in` will contain on the first line $3$ non-zero natural numbers $K$, $N$, and $M$, with the meanings described above, separated by a space.

## Output data

In the output file `grafc.out`, print either $-1$ if such a graph does not exist, or otherwise print on the first line the number of edges in the graph, followed by the edges of the graph, one per line.

## Constraints

$1 \leq N$
$M \leq K \leq 100$ 

If there are multiple solutions, any can be printed. 
Double edges or self-loops are not allowed.
The complement of an undirected graph is a graph that contains exactly those edges which are not in the given graph (in other words, the union of the edge sets of the two graphs is exactly the edge set of a complete graph with $K$ nodes, and their intersection is empty).

## Example

`grafc.in`
```
3 3 1
```

`grafc.out`
```
0
```

`grafc.in`
```
3 2 1
```

`grafc.out`
```
1
1 2
```

`grafc.in`
```
3 3 3
```

`grafc.out`
```
-1
```