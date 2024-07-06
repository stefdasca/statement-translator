Here is the translated text with the specified formatting and corrections:

An undirected tree (acyclic connected graph) with $N$ nodes is given. We want to remove nodes (along with their adjacent edges) from the given tree so that the number of connected components of the remaining graph is maximized.

# Task
Find out the maximum number of connected components we can obtain and how many distinct subsets of nodes can be removed from the tree so that, in the end, this maximum number of connected components remains.

# Input data
The input file `arbore.in` will contain the natural number $N$, representing the number of nodes in the tree, on the first line. On the next $N-1$ lines, there will be two numbers $X$ and $Y$, indicating that there is an edge between nodes $X$ and $Y$.

# Output data
The output file `arbore.out` will contain two natural numbers on the first line: the maximum number of connected components that we can obtain, and the number of ways we can obtain this number of connected components modulo $10^9+7$ (i.e., the remainder of the division of this number by $1\ 000\ 000\ 007$).

# Constraints and clarifications
* $1 \le N \le 100\ 000$
* $40\%$ of a test’s score will be awarded if the maximum number of connected components is correctly found.
* $60\%$ of a test’s score will be awarded if the number of ways is correctly found.
* For $20\%$ of the tests, $N \le 20$.
* For another $30\%$ of the tests, $N \le 1000$.

# Example 1

`arbore.in`
```
6 
1 2 
1 3 
1 4 
4 5 
4 6 
```

`arbore.out`
```
4 1
```

## Explanation
Nodes $1$ and $4$ are removed. No other subset of removed nodes produces $4$ or more connected components.

# Example 2
`arbore.in`
```
4 
1 2 
2 3 
3 4
```

`arbore.out`
```
2 5
```

## Explanation
The following subsets of nodes can be removed to obtain $2$ connected components: $\{2\}$, $\{3\}$, $\{2, 3\}$, $\{2, 4\}$, $\{1, 3\}$.