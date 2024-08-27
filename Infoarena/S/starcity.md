# StarCity

A star graph is a graph in which one of the nodes (node $1$, called the center of the graph) is connected by an edge to each of the other nodes, and each of the $N - 1$ remaining nodes is connected only to the center of the graph. If you want to imagine it, it looks like a bicycle wheel where the edges of the graph are the spokes of the bicycle.

## Task

A star graph with $N$ nodes is given. $N - 2$ nodes out of the $N$ have a unique value assigned from $1$ to $N - 2$, and the remaining $2$ are free. A move consists of selecting a node occupied by a value and moving this value to an adjacent free node. Determine the minimum number of moves to transform the initial graph into another given graph.

## Input data

The input file `starcity.in` contains $3$ lines. The first line contains the natural number $N$. The second line contains the numbers associated with each node in the graph, starting from node $1$ (the center) up to $n$. If a node is initially empty, the number associated with it is $0$. The third line contains $n$ numbers: for each node, the number that should be in it after the moves, or $0$ if the node is supposed to be empty.

## Output data

The output file `starcity.out` will contain on the first line the minimum number of moves $K$. On each of the next $K$ lines, two natural numbers $x$ and $y$ will be displayed, representing the movement of the value from node $x$ to node $y$. Nodes $x$ and $y$ must be adjacent, node $x$ must contain a number, and node $y$ must be empty for the move to be valid.

## Constraints and clarifications

$3 \leq N \leq 100\ 000$

If the given solution is valid, but the number of moves is not minimal, $40\%$ of the score will be awarded.

## Example

`starcity.in`
```
4
0 0 1 2
0 0 2 1
```

`starcity.out`
```
6
3 1
1 2
4 1
1 3
2 1
1 4
```

## Explanation

The star graph will go through the following states:

```
0 0 1 2 
1 0 0 2 
0 1 0 2 
2 1 0 0 
0 1 2 0 
1 0 2 0 
0 0 2 1 
```