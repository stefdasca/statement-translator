# Coloring

Consider a graph with $N$ nodes and $M$ edges. A valid coloring of the nodes of the graph is defined as a coloring where any two adjacent nodes are colored differently.

## Task

Determine the minimum number of colors needed for a valid coloring. For this minimum number of colors, determine the number of valid colorings of the graph's nodes.

## Input data

In the input file `colorare.in`, the first line will contain two integers $N$ and $M$. The next $M$ lines will contain two integers, separated by a space, $X$ and $Y$, indicating that there is an edge in the graph between nodes $X$ and $Y$.

## Output data

In the output file `colorare.out`, the first line will contain a pair of integers $p$ and $c$, which represent the minimum number of colors needed to color the graph's nodes while respecting the problem's condition, and the number of valid colorings of the graph with $p$ distinct colors, respectively.

## Constraints and clarifications

$1 \leq N \leq 15$ 

$0 \leq M \leq \frac{N(N-1)}{2}$

## Example

`colorare.in` 
```
3 
1 
1 2 
```

`colorare.out`
```
2 4
```