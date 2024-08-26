## Colorare2

We consider a bipartite graph. A graph is bipartite if there exist two sets, $A$ and $B$, such that every edge has one endpoint in set $A$ and the other in set $B$. The task is to color the edges of the graph with the minimum number of colors so that any two edges sharing a common endpoint are colored differently.

## Input data

The input file `colorare2.in` contains on the first line three values $N$, $M$, and $K$ representing the number of vertices in set $A$, the number of vertices in set $B$, and the number of edges in the graph. The vertices in set $A$ will be labeled with values between $1$ and $N$. The vertices in set $B$ will be labeled with values between $N + 1$ and $N + M$.

The following $K$ lines contain two integer values each, representing the nodes that determine the edges.

## Output data

The output file `colorare2.out` will contain on the first line the number of colors used. This number will be denoted by $C$. On each of the next $K$ lines, there will be an integer from the interval $[1, C]$, representing the colors of the edges, in the order they appear in the input file.

If there are multiple correct solutions, any of them can be displayed.

## Constraints and clarifications

$1 \leq N, M \leq 100$

$1 \leq K \leq 2 \ 500$

## Example

`colorare2.in`

``` 
6 6 10 
1 7 
1 8 
2 8 
2 10 
3 8 
3 9 
3 11 
4 12 
5 9 
6 11 
```

`colorare2.out`
```
3 
3 
2 
1 
3 
3 
1 
2 
1 
3 
3 
```

## Explanation