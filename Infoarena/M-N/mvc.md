# Mvc

You are given a connected undirected graph with $N$ nodes and $N$ edges, each node having a cost. You are asked to find a subset of nodes with minimal cost such that each edge in the graph has at least one endpoint in the subset. The cost of a subset is defined as the sum of the costs of each node in the subset.

## Input data

The input file `mvc.in` will contain on the first line a single integer $N$, representing both the number of nodes and the number of edges. The second line will contain exactly $N$ values, specifically the costs of the nodes $1, 2, \dots, N$. The following $N$ lines will each contain $2$ values, $x, y$ indicating that there is an (undirected) edge from $x$ to $y$.

## Output data

In the output file `mvc.out`, there should be a single integer representing the minimum cost of a subset such that every edge has at least one endpoint in that subset.

## Constraints and clarifications

$1 \leq N \leq 100000$  
$0 \leq \text{cost of a node} \leq 10000$ 

## Example

`mvc.in`  
`5`  
`0 9 1 2 0`  
`5 4`  
`2 1`  
`1 3`  
`3 4`  
`4 2`  
`2` 

## Explanation

Nodes $1$ and $4$ are chosen. We observe that all edges have exactly one endpoint in the subset $\{1, 4\}$. We also note that the subset $\{1, 4, 5\}$ is also correct and has the same cost $2$.