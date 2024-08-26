# AVD

A tree is an undirected, connected graph with $N$ nodes and $N-1$ edges. A tree is called an AVD tree if for every partition of $N = n_1 + n_2 + \dots + n_k$, the nodes of the tree can be divided into $k$ sets such that set $i$ has $n_i$ nodes and each set remains connected, $n_i \leq n_j$ for $i < j$. The AVD degree of a tree is the number of partitions that satisfy the previous conditions divided by the total number of existing partitions for $N$.

## Task

Given a tree with $N$ nodes, calculate its AVD degree.

## Input data

The first line of the input file `avd.in` contains $T$, the number of tests in the file, then the $T$ tests will follow. Each test's first line contains $N$, the number of nodes, followed by $N-1$ lines containing two numbers $x, y$, signifying an edge between nodes $x$ and $y$.

## Output data

The file `avd.out` will contain $T$ lines each containing the AVD degree of the tree described in the respective test case.

## Constraints and clarifications

$1 \leq N \leq 13$

$1 \leq T \leq 50$

The result will be displayed to 5 decimal places (rounded).

## Example

`avd.in`
```
3
4
1 2
1 3
1 4
5
1 2
2 3
3 4
4 5
1
```

`avd.out`
```
0.80000
1.00000
1.00000
```

## Explanations

For the first test, there are a total of 5 partitions for 4: $1+1+1+1$, $1+1+2$, $1+3$, $2+2$, $4$ from which only the partition $2+2$ cannot be achieved. Thus, the AVD degree of the tree is $4/5=0.80000$.