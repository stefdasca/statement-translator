### Arbore9

X wants to take a trip in a tree-shaped city with $N$ nodes. For each edge from $u$ to $v$, the beauty coefficient $a$ of traversing the edge from $u$ to $v$ and the beauty coefficient $b$ of traversing the edge from $v$ to $u$ are known ($a$ and $b$ are integers). X can travel in any direction along the tree’s edges, but in the end, they will only remember the last time they visited each edge. The total coefficient is the sum of the coefficients of the edges that X remembers visiting. To decide from which node to start the trip, X asks you to find the maximum total coefficient that can be obtained starting from each of the $N$ nodes.

## Input data

The input file `arbore9.in` contains on the first line the number $N$ of tree nodes. The next $N-1$ lines contain 4 numbers representing an edge: $u_i$, $v_i$, $a_i$, $b_i$.

## Output data

The output file `arbore9.out` will contain, on a single line, $N$ numbers separated by a space, the $i$-th number representing the maximum cost obtained starting from node $i$.

## Constraints and clarifications

$1 \leq N \leq 100\ 000$

$1 \leq u_i , v_i \leq N$

$-1\ 000\ 000\ 000 \leq a_i , b_i \leq 1\ 000\ 000\ 000$

For 30 points,

$1 \leq N \leq 1000$

For another 20 points,

$0 \leq a_i , b_i \leq 1\ 000\ 000\ 000$

## Example

`arbore9.in`
```
8
1 2 2 2
2 3 0 -5
2 4 -1 3
4 5 5 5
2 4 6 4
2 1 7 3
1 7 8 -1 -3
```

`arbore9.out`
```
12 12 10 12 12 12 12 11
```

## Explanation

Starting from node $1$, a path with the maximum total coefficient is: $1 \rightarrow 2 \rightarrow 4 \rightarrow 5 \rightarrow 4 \rightarrow 6 \rightarrow 4 \rightarrow 2 \rightarrow 1 \rightarrow 7 \rightarrow 1 \rightarrow 7$

Only the coefficients of the bolded edges will be added to the total coefficient.