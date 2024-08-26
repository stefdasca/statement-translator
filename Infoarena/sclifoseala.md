## Fanciness

Marcel has learned about shapes. Shapes can be round or complicated. Marcel likes that when they are complicated, at least they should be small, as irrelevant as possible. For example, a graph can have multiple biconnected components, each of which is either representable as a simple round elegant cycle or very small in size. Thus, a fancy graph is an undirected, connected graph without double edges or edges from a node to itself, where node $1$ has a degree of $1$ (therefore the graph has at least $2$ nodes), and all its biconnected components are either representable as a simple cycle without other edges between those nodes or contain at most $8$ nodes. Determine in how many ways a fancy graph can be partitioned into two non-empty connected subgraphs.

## Input data

The input file `sclifoseala.in` contains on the first line the number $T$ of tests. The structure of each test is as follows: The first line contains the number $N$ of nodes, respectively $M$ of edges. The following $M$ lines contain pairs of natural numbers $a$ and $b$ representing the fact that there is a bidirectional edge from $a$ to $b$.

## Output data

The output file `sclifoseala.out` will contain a single number for each of the $T$ tests, namely the number of partitions of the given graph into two non-empty connected subgraphs.

## Constraints

$1 \leq T \leq 3$  
$1 \leq a, b \leq N \leq 30000$  

Scoring  
For evaluation, $5$ tests will be used, each worth $20$ points. Some of them have the following additional constraints:  
in the first test, $N \leq 15$  
in the second test, there is only one biconnected component in the form of a simple cycle, and the rest have $2$ nodes each  
in the third test, the biconnected components are either of size $2$ or in the form of a simple cycle  
in the fourth test, the biconnected components contain at most $8$ nodes  
in the fifth test, there are no additional constraints  

Clarifications  
If you are curious about what a biconnected component is, Marcel recommends you learn: Biconnected Components.  
The degree of a node is equal to the number of edges containing it as a vertex.  
Partitioning into sets $A, B$ is different from partitioning into sets $B, A$ (see example).

## Example

`sclifoseala.in`  
```
2
6 6
1 2
2 3
3 4
4 5
5 6
6 2
6 9
1 2
2 3
3 4
4 5
5 6
6 2
5 3
5 2
4 6
```

`sclifoseala.out`  
```
22
28
```

## Explanation

For the second example, the desired partitions are: $1/234$, $12/34$, $123/4$, $124/3$, $234/1$, $34/12$, $4/123$, $3/124$