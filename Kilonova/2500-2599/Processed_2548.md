# Task

We all know that a tree is beautifully colored if all nodes of the same color are accessible by traversing only through nodes of their color.
It is also known that a tree is Cracked if for every node, its parent node has a label value smaller than the label value of the node (Thus, it is rooted at $1$).

Let $F(X,K)=$ the number of beautiful colorings of tree $X$ with $K$ colors.
What is $\\sum F(A,K)$, where $A$ is a Cracked tree with $N$ nodes?

# Input data

Given $N$ and $K$.

# Output data

Print the required sum mod $10^9+7$.

# Constraints and clarifications

* $1 \leq N,K \leq 10^6$;

# Example 1

`stdin`
```
3 2
```

`stdout`
```
12
```

## Explanation

All Cracked trees with $3$ nodes are:
~[Screenshot 2024-03-25 211341.png]
~[Screenshot 2024-03-25 211557.png]

We have $2$ colors available, for the first tree the coloring:
Node $1$ color $1$.
Node $2$ color $2$.
Node $3$ color $1$.
is a correct coloring. Whereas the coloring:
Node $1$ color $1$.
Node $2$ color $2$.
Node $3$ color $2$.
is not correct because nodes $2$ and $3$ have the same color and the path between them contains a different color than $2$.

# Example 2

`stdin`
```
69 420
```

`stdout`
```
50524947
```