## Luff

Bluff found an undirected graph this time with $N$ nodes and $M$ edges, each having an associated value. She asks $Q$ questions of the form $(node, k)$ and wants to find the following answer for each of these: what is the maximum value $VAL$ such that considering only edges with value $\geq VAL$, there exists a tree included in the graph that contains at least $k$ nodes, including the node $node$.

## Input data

The input file `luff.in` will contain on the first line three numbers, $N,M,Q$ with the meaning described in the statement. The following $M$ lines will contain three integers $X_i , Y_i , D_i$ with the meaning that in the graph there is a bidirectional edge between the nodes $X_i$ and $Y_i$, having the value $D_i$. Next, there are $Q$ lines, each containing the description of a query: $node_i , k_i$.

## Output data

In the output file `luff.out` there will be $Q$ lines, representing the answer to each question, in the order they appear in the input file. If there is no solution for a query, $-1$ will be printed.

## Constraints

$N \leq 200\ 000$   
$M \leq 200\ 000$   
$Q \leq 100\ 000$   

$1 \leq X_i, Y_i, node_i \leq N$  
$2 \leq k_i \leq N$  
$1 \leq D_i \leq 1\ 000\ 000\ 000$

## Example

`luff.in`
```
7 7 3
1 2 12
2 3 15
3 4 11
4 5 12
5 7 8
6 7 7
5 6 4
2 5
7 2
4 3
```

`luff.out`
```
11
8
11
```