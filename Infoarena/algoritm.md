# Por Costel and the Algorithm

Even though he's not a first-year student at FMI, Por Costel started studying Graph Algorithms. Today, he is learning about the Bellman-Ford algorithm, which calculates the shortest paths from a source node (in this case, node $1$) to all other nodes in a directed graph with edge costs. Por Costel, using his minimal computer science knowledge, managed to write the following C++ code that represents a variation of the Bellman-Ford algorithm:

```cpp
for (int i = 1; i \leq n; ++i) 
    d[ i ] = infinit;  		// GUITZZZ! 
d[ 1 ] = 0;  
bool ok = 0;  
while (ok == 0) { 
    ok = 1;  
    for (int i = 0; i < E.size(); ++i)      		        // OINK! 
    { 
        if (d[ E[i].x ] + E[i].cost < d[ E[i].y ]) { 
            ok = 0; 
            d[ E[i].y ] = d[ E[i].x ] + E[i].cost;  		// I like corn! 
        } 
    } 
}
```

We notice several deficiencies in the above code. Besides the rudimentary documentation, Por Costel also stores the graph using an array of edges (the array $E$). An edge is stored as a triplet with the meaning that the edge goes from $x$ to $y$ and has the cost $cost$. But most likely, the worst issue is that the program is SLOW! Since we want our friend with hooves to leave with a good impression of computer science, we want him to score $100$ points with this source, and even run as fast as possible. It is clear that the number of iterations of the $while()$ loop is directly influenced by the order of the edges in the edge array $E$. Given a directed graph with $n$ nodes and $m$ edges, you are required to display an ordering of the edges such that the Bellman-Ford algorithm written by Por Costel finishes after exactly two iterations (i.e., enters the $while()$ loop only twice).

## Input data

The input file `algoritm.in` will contain on the first line $T$, the number of tests. Each of the $T$ tests has the following format: the first line contains two numbers $n$ and $m$, the number of nodes, and respectively the number of edges in the graph. Following that are $m$ lines describing the edges, each containing exactly $3$ numbers $x$, $y$, $cost$, indicating that there is an edge from node $x$ to node $y$ with the cost $cost$. 

## Output data

The output file `algoritm.out` will display $T$ lines, each with $m$ numbers, the $i$-th line will contain a permutation of the edge indices, representing the order in which they will appear in Por Costel's array $E$. The edges are considered indexed by their order in the input file (e.g., the first edge read is the edge with index $1$). 

## Constraints and clarifications

$n \leq 1000$
$m \leq 10000$
$1 \leq x, y \leq n$
$1 \leq$ the cost of an edge $\leq 1000$
It is guaranteed that there is at least one edge that exits node $1$
In Por Costel's program, $infinit$ is defined as being greater than any integer
Any solution that meets the task is accepted
Note! The graph can contain two edges from $x$ to $y$, or an edge from $x$ to $y$

## Example

`algoritm.in`

```
1
4 4
1 2 1
3 4 2
2 3 3
1 3 1
```

`algoritm.out`

```
1 3 4 2
```

## Explanation

The order of the edges in Por Costel's array $E$ will be in this case: $(1, 2, 1)$, $(1, 3, 1)$, $(3, 4, 2)$, $(2, 3, 3)$. You can test that the algorithm will finish in two iterations. There are multiple solutions that could be displayed. Another example is: $1, 3, 4, 2$.