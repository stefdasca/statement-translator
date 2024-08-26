Treemis

Tassadar has a tree with $N$ nodes numbered from $0$ to $N - 1$, each node having an associated integer value. Each path is assigned a sequence of numbers formed from the values associated with the nodes on it, in the order they are traversed. An increasing subsequence of a path is defined as an increasing subsequence of the value sequence associated with that path. Tassadar wants to find the longest increasing subsequence of any path in the tree and asks for your help.

## Input data

The input file `treemis.in` contains on the first line an integer $N$ with the meaning described in the statement. The next line contains $N$ integers $V_i$, $0 \leq i < N$, representing the values associated with the nodes. The next $N - 1$ lines contain two integers $x$ and $y$ indicating that there is an edge between nodes $x$ and $y$.

## Output data

The output file `treemis.out` will contain a single integer, representing the length of the longest increasing subsequence.

## Constraints

$1 \leq N \leq 100000$
$-1000000000 \leq V_i \leq 1000000000$
the subsequence does not have to be strictly increasing 

## Example

`treemis.in`
```
7
1 2 9 3 -1 5 4
0 1
1 2
2 3
3 4
2 5
5 6
```

`treemis.out`
```
3
```

## Explanation

The maximal increasing subsequence has a length of $3$. One of these subsequences can be found on the path from node $0$ to node $6$, which has the associated value sequence ${1, 2, 9, 5, 4}$, and an example of an increasing subsequence of length $3$ from this path is ${1, 2, 4}$.