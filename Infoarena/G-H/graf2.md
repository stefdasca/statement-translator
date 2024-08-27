# Graf2

Given a directed graph $A=(V, E)$, we say there is a path from $X$ to $Y$ $(X, Y \in V)$ if starting from $X$ and following the graph's edges, one can reach $Y$. The task is to find the minimum number of edges in a graph $B=(V,E_2)$ such that there is a path from $X$ to $Y$ in graph $B$ if and only if there is a path from $X$ to $Y$ in graph $A$.

## Task

## Input data

The input file `graf2.in` contains in the first line two integers $N$ and $M$ representing the number of nodes and respectively the number of edges of graph $A$. The next $M$ lines contain two integers $X$ and $Y$ each, representing that there is an edge from $X$ to $Y$ in graph $A$. 

## Output data

The output file `graf2.out` will contain a single number representing the minimum number of edges of graph $B$.

## Constraints and clarifications

$1 \leq N \leq 600$  
$1 \leq M \leq 10000$

## Example

`graf2.in`  
``` 
3 3
1 2
2 3
1 3
```

`graf2.out`  
``` 
2
```

## Explanation

Graph $B$ can be created with the edges $1 \to 2$ and $2 \to 3$, preserving the graph property.