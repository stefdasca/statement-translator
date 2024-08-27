## and space before key expressions and variables

Levels2

Given a tree with $N$ nodes rooted at node $1$. Display the tree by levels in the following format:

level $1$: $x_1$ $x_2$ $\dots$ $x_{K_1}$

level $2$: $x_{K_1+1}$ $x_{K_1+2}$ $\dots$ $x_{K_1+K_2}$

$\dots$

$K_i$ represents the number of nodes at level $i$, and $x$ represents any node from the tree. For each level, any two consecutive nodes will be separated by exactly one space.

## Input data

The input file `nivele2.in` contains the natural number $N$ on the first line. Each of the following $N-1$ lines contains a pair of numbers $(A,B)$, indicating that there is an edge between node $A$ and node $B$ in the tree.

## Output data

In the output file `nivele2.out`, for each level all nodes on that level will be printed, in the format described above.

## Constraints

$1 \leq N \leq 100\ 000$

$1 \leq A, B \leq N$

$A \ne B$

The levels need to be displayed in order, from $1$ to the maximum level. Nodes can be displayed in any order within the same level.

For 30% of the tests $N \leq 1\ 000$.

## Example

`nivele2.in`

```
5
1 2
1 3
1 5
3 4
```

`nivele2.out`

```
level 1: 1
level 2: 2 3 5
level 3: 4
```

## Explanation
