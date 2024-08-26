## Task

An undirected connected graph $G$ is given, with $N$ nodes and $M$ edges. You are required to determine a coloring of this graph using $3$ colors from the set $\{1,2,3\}$ such that:
1. If we look at each color separately, each graph is connected (only the edges between nodes of the respective color are taken into account).
2. For any two colors $C_1$ and $C_2$, it is possible to travel from any node colored with $C_1$ to any node colored with $C_2$ without passing through nodes colored with $C_3$.
3. There is at least one node of each color.

## Input data

The input file `something.in` contains on the first line $N$ - the number of nodes, $M$ the number of edges. The following $M$ lines contain $2$ numbers $x$ $y$ separated by a space, indicating that there is an edge between nodes $x$ and $y$.

## Output data

The output file `something.out` will contain the number $-1$ if a coloring according to the above rules is not possible in the given graph. Otherwise, it will contain $N$ numbers from the set $\{1,2,3\}$ separated by a space, with the $i$-th of these numbers indicating the color of the $i$-th node. Any correct solution is accepted.

## Constraints and clarifications

$1 \leq N, M \leq 100\ 000$

## Example

`something.in`
```
3 3
1 2
2 3
3 1
```

`something.out`
```
1 2 3
```

## Explanation