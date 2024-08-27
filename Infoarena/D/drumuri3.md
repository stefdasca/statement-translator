## Task

Bercea has just acquired (by questionable means) $Q$ limousines. Now, to show off his new acquisitions, he has decided to take several rides around the city, which is actually an undirected graph with $N$ nodes and $M$ edges. A path is defined as a sequence of nodes $a_1, a_2, \dots, a_k$ such that there exists an edge $(a_i, a_{i+1})$ for any $1 \leq i \leq k-1$. Thus, any node can be used any number of times in a path, as well as any edge. The length of a path is the number of nodes that are part of that path. However, Bercea does not want to take paths longer than $K$ nodes, because then he could leave his sphere of influence in the city. Therefore, given $Q$ pairs of nodes $i$ and $ji$, find the number of paths that start at node $i$, end at node $ji$, and the length of each path is $\leq K$. Since the number of paths can be very large and Bercea only knows how to count to the number of millions of € he has, display the answer modulo $10\ 007$.

## Input data

The input file `drumuri3.in` will contain on the first line the natural numbers $N, M, K$, and $Q$ with the above meaning. The next $M$ lines will contain two natural numbers each, representing two nodes between which there is an edge. The following $Q$ lines will contain two natural numbers $i$ and $ji$ representing the pairs of cities between which Bercea wants to travel.

## Output data

In the output file `drumuri3.out` will contain $Q$ lines with the desired numbers modulo $10\ 007$.

## Constraints and clarifications

$1 \leq N \leq 100$  
$1 \leq K \leq 5\ 000$  
$1 \leq Q \leq 2\ 500$

The graph is connected (there is at least one path between any two pairs of nodes).

An edge will not appear more than once in the input file.

There will be no edge from a node to itself in the input file.

$i \ne ji$

## Example

`drumuri3.in`
```
6 15 4 2 
1 2 
1 3 
1 4 
1 5 
1 6 
2 3 
2 4 
2 5 
2 6 
3 4 
3 5 
3 6 
4 5 
4 6 
5 6 
1 2 
1 6
```

`drumuri3.out`
```
26 
26
```