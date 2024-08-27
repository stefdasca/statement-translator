Escape

Story and ## Task... A directed graph with $N$ nodes is given. From each node exactly $K$ arcs of costs $1,2,\dots,K$ depart (One arc of each cost). Multiple arcs between 2 nodes and arcs from a node to the same node can exist. A path is a sequence of arcs... which can pass through the same node and through the same edge multiple times. The cost of a path of length $L$ is calculated as follows: The cost of the first arc multiplied by $(K+1)^0$ , added to the cost of the second arc multiplied by $(K+1)^1$, $\dots$ added to the cost of the $L$-th arc multiplied by $(K+1)^{L-1}$. For example, for the path from $1$ to $4$ in the graph from the figure, the cost of this path for $K = 3$ is: $3*4^0 + 1*4^1 + 2*4^2 = 39$. The nodes are colored in $2$ colors: white and black. There are $M$ white nodes, and the rest are black. Two nodes are symmetrical if for any possible cost $S$, the paths of exact cost $S$ departing from the two nodes end in nodes of the same color. (If nodes $A$ and $B$ are symmetrical, then there is no path of cost $S$ from node $A$ and a path of the same cost from node $B$ that end in nodes of different colors). A set of nodes is called perfect if no matter which two nodes are chosen from this set, they are symmetrical. A set is called a perfect maximal cardinality set if any other node is added to the respective set, it no longer meets the condition of being perfect. Your goal is to display all perfect sets of maximal cardinality. Display the sets in lexicographical order, one per line. (within a set, elements must be sorted in ascending order).

## Input data

In the input file `escape.in`, the first line will contain $3$ natural numbers: $N$, $M$ and $K$, in this order. The next line will contain $M$ distinct numbers, representing the indices of the white nodes in the graph. Following is a matrix $A$ with $N$ rows and $K$ columns where $A_{i,j}$ represents an arc that starts from node $i$ and arrives at node $A_{i,j}$ and has cost $j$.

## Output data

In the output file `escape.out` display, in lexicographical order, one per each line, all perfect sets of maximal cardinality (elements within the sets should be sorted in ascending order).

## Constraints and clarifications

$30$ pts:
$1 \leq K \leq 10$
$1 \leq M \leq N \leq 15$
$1 \leq A_{i,j} \leq N$

$60$ pts:
$1 \leq K \leq 30$
$1 \leq M \leq N \leq 50$
$1 \leq A_{i,j} \leq N$

$100$ pts:
$1 \leq K \leq 50$
$1 \leq M \leq N \leq 500$
$1 \leq A_{i,j} \leq N$

## Example

`escape.in`
```
3 1 2
3
2 3
1 3
3 3
```

`escape.out`
```
1 2 3
```

## Explanation

...