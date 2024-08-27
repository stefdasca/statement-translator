## Task

An tree with $N$ nodes and $M$ guards is given. To hire guard $i$ you must pay the cost $Z_i$. If you hire guard $i$, then this guard will protect all nodes on the path from node $A_i$ to node $B_i$. You need to determine the minimum cost to guard the entire tree. A node cannot be guarded by more than one guard. 

## Input data

The input file `paznici3.in` will contain on the first line 2 natural numbers $N$ and $M$ as described above. On the next $N - 1$ lines, there will be 2 numbers $a$ and $b$ indicating that there is an edge from $a$ to $b$. On the following $M$ lines, there will be 3 numbers $Z_i$, $A_i$, and $B_i$. 

## Output data

The output file `paznici3.out` will contain a single natural number representing the minimum required cost. 

## Constraints and clarifications

$1 \leq N \leq 100\,000$ 

$1 \leq M \leq 200\,000$ 

The values of the elements are up to $10\,000$

It is guaranteed that there is a solution 

## Example

`paznici3.in`

```
7 6
1 2
2 3
2 4
1 5
5 6
5 7
8 3 7
7 4 4
8 6 6
9 3 4
10 6 7
5 1 1
```

`paznici3.out`

```
23
```