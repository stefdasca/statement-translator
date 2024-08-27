## Task

You are given a tree with costs on its edges. This tree needs to be "linearized" on the real number axis in the following sense: Each node in the tree will be associated with exactly one point on the axis. The $N$ points do not necessarily need to be distinct. If there is an edge between two nodes $X$ and $Y$ in the tree, then the distance between the points associated with these nodes must be equal to the cost of the edge between them. The maximum distance between any two points associated with nodes must be minimized. You must find this minimum distance.

## Input data

The input file `oxificare.in` will contain on its first line the integer value $T$, representing the number of tests in the file. The structure of a test is as follows: The first line will contain the value $N$, representing the number of nodes in the tree. The second line will contain the array $parent$. This array is composed of $N - 1$ values, $parent[i]$ representing the parent of node $i + 1$ in the tree. Node 1 is the root of the tree and has no parent. Note that the tree is described this way only to simplify the input, the root being irrelevant in the process of linearizing the tree. The third line will itself contain an array $cost$ of $N - 1$ values, where $cost[i]$ represents the cost of the edge between node $i + 1$ and its parent.

## Output data

The output file `oxificare.out` will contain $T$ lines, with the $i$-th line representing the solution for test $i$.

## Constraints and clarifications

$1 \leq N \leq 1000$

$1 \leq cost[i] \leq 5000$

$1 \leq parent[i] \leq i$

The sum of the values of $N$ within the same input file does not exceed the value 3000.

All values in the input are natural numbers.

For tests worth 50 points, it is additionally guaranteed that $parent[i] = i$ for all $1 \leq i \leq N - 1$. In other words, the tree is a chain.

Of these, for tests worth 20 points, it is additionally guaranteed that $1 \leq N, cost[i] \leq 100$, and $1 \leq T \leq 25$.

## Example

`oxificare.in`
```
2
4
1 2 3
5 5 5
4
1 2 3
5 4 5 5
```

`oxificare.out`
```
6
6
```

## Explanation

A solution for the first test is the list of points $\{1,\ 6,\ 1,\ 6\}$.

A solution for the second test is the list of points $\{0,\ 5,\ 1,\ 6\}$.