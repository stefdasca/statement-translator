# PScArb

Consider a tree with $N$ nodes, out of which $K$ are leaves. Each node has one of the colors $R$, $G$, or $B$. The tree obeys the property: the path between any two leaves must contain each color an odd number of times. Generate such a tree.

## Input data

The input file `pscarb.in` will contain two natural numbers separated by a space, $N$ and $K$.

## Output data

The output file `pscarb.out` will contain on the first $N-1$ lines, the edges of the tree. An edge is described by the indices of the two nodes separated by a space. On the next line, there will be a string consisting of the characters $R$, $G$, and $B$, which describes the colors of the nodes (the $i$-th value describes the color of node $i$). In case there is no solution, print $-1$. 

## Constraints and clarifications

$2 \leq K$  
$K \leq N$  
$N \leq 100$  

Three colors are known to the world...

## Example

`pscarb.in`  
```
3 2
```

`pscarb.out`  
```
1 2
2 3
RGB
```

`100 100`
```
-1
```

## Explanation

First example: On the path between leaves $1$ and $3$, the colors $R$, $G$, and $B$ each appear once.
Second example: It is not possible to construct a tree with $100$ nodes and $100$ leaves.